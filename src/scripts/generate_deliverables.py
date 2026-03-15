import yaml
import os
import subprocess
import urllib.request

def load_data(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def generate_overview(data, output_path):
    framework = data['framework']
    with open(output_path, 'w') as f:
        f.write(f"# {framework['name']}\n\n")
        f.write(f"Version: {framework['version']}\n\n")

        f.write("## Roles\n\n")
        for role in framework['roles']:
            f.write(f"### [{role['name']}](roles/{role['id']}.md) (`{role['id']}`)\n")
            f.write(f"- **Description**: {role['description']}\n")
            f.write(f"- **Accountability**: {role['accountability']}\n")
            if 'human_interaction' in role:
                f.write(f"- **Human Interaction**: {role['human_interaction']}\n")
            f.write("\n")

        f.write("## Deliverables\n\n")
        f.write("| ID | Name | Description | Accountability |\n")
        f.write("|----|------|-------------|----------------|\n")
        roles_dict = {r['id']: r['name'] for r in framework['roles']}
        for deliv in framework['deliverables']:
            acc = roles_dict.get(deliv['accountability_id'], deliv['accountability_id'])
            f.write(f"| `{deliv['id']}` | {deliv['name']} | {deliv['description']} | {acc} |\n")
        f.write("\n")

        f.write("## Process Steps\n\n")
        for step in framework['process_steps']:
            f.write(f"### {step['name']} (`{step['id']}`)\n")
            f.write(f"- **Primary Role**: {roles_dict.get(step['primary_role_id'], step['primary_role_id'])}\n")
            f.write(f"- **Objective**: {step['objective']}\n")
            if 'activities' in step:
                f.write("- **Activities**:\n")
                for act in step['activities']:
                    f.write(f"  - {act}\n")
            if 'decision_point' in step:
                f.write(f"- **Decision Point**: **{step['decision_point']}**\n")
            f.write("\n")

def generate_role_pages(data, roles_dir):
    framework = data['framework']
    roles = framework['roles']
    roles_dict = {r['id']: r['name'] for r in roles}

    if not os.path.exists(roles_dir):
        os.makedirs(roles_dir)

    for role in roles:
        role_path = os.path.join(roles_dir, f"{role['id']}.md")
        with open(role_path, 'w') as f:
            f.write(f"# Role: {role['name']}\n\n")
            f.write(f"**ID**: `{role['id']}`\n\n")
            f.write(f"## Description\n{role['description']}\n\n")
            f.write(f"## Accountability\n{role['accountability']}\n\n")

            if 'human_interaction' in role:
                f.write(f"## Human Interaction\n{role['human_interaction']}\n\n")

            if 'responsibilities' in role:
                f.write("## Key Responsibilities\n")
                for resp in role['responsibilities']:
                    f.write(f"- {resp}\n")
                f.write("\n")

            if 'interactions' in role:
                f.write("## Interaction Guide\n")
                if 'interaction_guide' in role:
                    f.write(f"{role['interaction_guide']}\n\n")

                f.write("### Cross-Role Interactions\n")
                for interaction in role['interactions']:
                    other_role_name = roles_dict.get(interaction['role_id'], interaction['role_id'])
                    f.write(f"- **With {other_role_name}**: {interaction['description']}\n")
                f.write("\n")

            if 'mapping' in role:
                f.write("## Framework Mapping\n")
                for fw, mapped_role in role['mapping'].items():
                    f.write(f"- **{fw}**: {mapped_role}\n")
                f.write("\n")

def generate_raci(data, output_path):
    framework = data['framework']
    roles = framework['roles']
    deliverables = framework['deliverables']

    with open(output_path, 'w') as f:
        f.write("# RACI Matrix\n\n")
        header = "| Deliverable | " + " | ".join([r['name'] for r in roles]) + " |"
        f.write(header + "\n")
        f.write("|" + "---|" * (len(roles) + 1) + "\n")

        for d in deliverables:
            row = f"| {d['name']} |"
            for r in roles:
                if d['accountability_id'] == r['id']:
                    row += " A/R |"
                else:
                    row += " |"
            f.write(row + "\n")
        f.write("\n\n*A/R: Accountable & Responsible* (Simplified for this framework)\n\n")

def generate_mermaid(data, output_path):
    framework = data['framework']
    steps = framework['process_steps']

    # We generate the mermaid file without the code block markers for mmdc compatibility
    with open(output_path, 'w') as f:
        f.write("graph TD\n")
        for step in steps:
            # Nodes
            dp = step.get('decision_point', 'N/A')
            f.write(f"    {step['id']}[\"{step['name']}<br/>({dp})\"]\n")

        # Connections
        for i in range(len(steps) - 1):
            f.write(f"    {steps[i]['id']} --> {steps[i+1]['id']}\n")

        # Add a back link for loops if explicitly defined or by convention
        # For now, keeping the execution loop logic but making it safe
        execution_loop_id = "step_execution_loop"
        if any(s['id'] == execution_loop_id for s in steps):
            f.write(f"    {execution_loop_id} --> {execution_loop_id}\n")

def generate_images(mmd_path, images_dir):
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    base_name = os.path.splitext(os.path.basename(mmd_path))[0]

    formats = ["png", "svg"]
    for fmt in formats:
        output_path = os.path.join(images_dir, f"{base_name}.{fmt}")
        try:
            subprocess.run(
                ["mmdc", "-i", mmd_path, "-o", output_path],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"Generated {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to generate {output_path}: {e.stderr}")
        except FileNotFoundError:
            print("Error: 'mmdc' command not found. Please install mermaid-cli.")
            break

def generate_plantuml(docs_dir, images_dir, jar_path):
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    if not os.path.exists(jar_path):
        print(f"PlantUML JAR not found at {jar_path}. Attempting to download...")
        url = "https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-1.2024.3.jar"
        try:
            urllib.request.urlretrieve(url, jar_path)
            print(f"Downloaded PlantUML JAR to {jar_path}")
        except Exception as e:
            print(f"Failed to download PlantUML JAR: {e}")
            return

    for file in os.listdir(docs_dir):
        if file.endswith(".puml"):
            puml_path = os.path.join(docs_dir, file)
            print(f"Processing PlantUML file: {puml_path}")
            try:
                subprocess.run(
                    ["java", "-jar", jar_path, "-o", os.path.abspath(images_dir), puml_path],
                    check=True,
                    capture_output=True,
                    text=True
                )
                print(f"Generated images for {file} in {images_dir}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to generate PlantUML images for {file}: {e.stderr}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(base_dir, "src", "data", "fusion_framework.yaml")
    docs_dir = os.path.join(base_dir, "src", "docs")
    images_dir = os.path.join(base_dir, "src", "images")
    jar_path = os.path.join(base_dir, "src", "scripts", "plantuml.jar")

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    data = load_data(data_path)

    generate_overview(data, os.path.join(docs_dir, "framework_overview.md"))
    generate_role_pages(data, os.path.join(docs_dir, "roles"))
    generate_raci(data, os.path.join(docs_dir, "raci_matrix.md"))

    mmd_path = os.path.join(docs_dir, "process_flow.mmd")
    generate_mermaid(data, mmd_path)
    generate_images(mmd_path, images_dir)

    generate_plantuml(docs_dir, images_dir, jar_path)

    print("Deliverables and images generated successfully.")

if __name__ == "__main__":
    main()
