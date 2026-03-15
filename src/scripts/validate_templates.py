import json
import yaml
import jsonschema
import sys
import os

def validate_yaml(yaml_path, schema_path):
    print(f"Validating {yaml_path} against {schema_path}...")

    if not os.path.exists(yaml_path):
        print(f"Error: YAML file not found at {yaml_path}")
        return False

    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return False

    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)

        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)

        jsonschema.validate(instance=data, schema=schema)
        print("Validation successful!")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Schema validation error: {e.message}")
        print(f"At: {e.json_path}")
        return False
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    template_dir = os.path.join(base_dir, "src", "data", "templates")
    schema_dir = os.path.join(base_dir, "src", "schema")

    manifest_schema = os.path.join(schema_dir, "project_manifest.schema.json")
    deliverable_schema = os.path.join(schema_dir, "deliverable_instance.schema.json")

    overall_success = True

    # Validate Manifest
    manifest_file = os.path.join(template_dir, "project_manifest.yaml")
    if not validate_yaml(manifest_file, manifest_schema):
        overall_success = False

    # Validate Deliverables
    for f in os.listdir(template_dir):
        if f == "project_manifest.yaml" or not f.endswith(".yaml"):
            continue

        deliverable_file = os.path.join(template_dir, f)
        if not validate_yaml(deliverable_file, deliverable_schema):
            overall_success = False

    if not overall_success:
        print("\nSome templates failed validation!")
        sys.exit(1)
    else:
        print("\nAll templates validated successfully!")

if __name__ == "__main__":
    main()
