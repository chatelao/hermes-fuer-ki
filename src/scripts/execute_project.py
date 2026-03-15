import yaml
import json
import jsonschema
import os
import sys

def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def validate(data, schema):
    jsonschema.validate(instance=data, schema=schema)

def generate_report(project_data, framework_data, deliverables_data, output_path):
    project = project_data['project']
    framework = framework_data['framework']

    with open(output_path, 'w') as f:
        f.write(f"# Project Execution Report: {project['name']}\n\n")
        f.write(f"- **Version**: {project['version']}\n")
        f.write(f"- **Framework**: {framework['name']} (v{framework['version']})\n\n")

        f.write("## Deliverable Status\n\n")
        f.write("| Framework ID | Name | Status | Content Summary |\n")
        f.write("|--------------|------|--------|-----------------|\n")

        delivered_ids = set()
        for df in project['deliverables']:
            fid = df['framework_id']
            d_inst = deliverables_data[fid]['deliverable']
            delivered_ids.add(fid)
            content_summary = (d_inst['content'][:50] + '...') if len(d_inst['content']) > 50 else d_inst['content']
            f.write(f"| `{fid}` | {d_inst['name']} | {d_inst['status']} | {content_summary} |\n")
        f.write("\n")

        f.write("## Process Alignment\n\n")
        for step in framework['process_steps']:
            f.write(f"### {step['name']} (`{step['id']}`)\n")

            # Check inputs
            inputs = step.get('inputs', [])
            missing_inputs = [i for i in inputs if i not in delivered_ids]

            # Check outputs
            outputs = step.get('outputs', [])
            missing_outputs = [o for o in outputs if o not in delivered_ids]

            status = "Ready"
            if not missing_inputs and not missing_outputs:
                status = "Completed"
            elif missing_inputs:
                status = "Blocked (Missing Inputs)"
            elif not missing_inputs and missing_outputs:
                status = "In Progress (Missing Outputs)"

            f.write(f"- **Status**: {status}\n")
            if missing_inputs:
                f.write(f"- **Missing Inputs**: {', '.join(missing_inputs)}\n")
            if missing_outputs:
                f.write(f"- **Missing Outputs**: {', '.join(missing_outputs)}\n")
            f.write("\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python execute_project.py <path_to_project_manifest>")
        sys.exit(1)

    manifest_path = sys.argv[1]
    project_dir = os.path.dirname(manifest_path)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    schema_dir = os.path.join(base_dir, "src", "schema")
    data_dir = os.path.join(base_dir, "src", "data")
    docs_dir = os.path.join(base_dir, "src", "docs", "samples")

    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    manifest_schema = load_json(os.path.join(schema_dir, "project_manifest.schema.json"))
    deliv_schema = load_json(os.path.join(schema_dir, "deliverable_instance.schema.json"))

    # Load and validate manifest
    project_data = load_yaml(manifest_path)
    validate(project_data, manifest_schema)

    # Load framework
    framework_path = os.path.join(data_dir, project_data['project']['framework_ref'])
    framework_data = load_yaml(framework_path)

    # Load and validate deliverables
    deliverables_data = {}
    for d_entry in project_data['project']['deliverables']:
        d_path = os.path.join(project_dir, d_entry['file'])
        d_data = load_yaml(d_path)
        validate(d_data, deliv_schema)
        deliverables_data[d_entry['framework_id']] = d_data

    # Generate report
    project_name_slug = project_data['project']['name'].lower().replace(" ", "_")
    report_path = os.path.join(docs_dir, f"{project_name_slug}_report.md")
    generate_report(project_data, framework_data, deliverables_data, report_path)

    print(f"Project executed successfully. Report generated at: {report_path}")

if __name__ == "__main__":
    main()
