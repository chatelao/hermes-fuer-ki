import json
import yaml
import jsonschema
import sys
import os

def validate_schema(yaml_path, schema_path):
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
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    schema_file = os.path.join(base_dir, "src", "schema", "framework.schema.json")

    if len(sys.argv) > 1:
        yaml_files = sys.argv[1:]
    else:
        # Default to all yaml files in src/data if no arguments provided
        data_dir = os.path.join(base_dir, "src", "data")
        yaml_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(('.yaml', '.yml'))]

    overall_success = True
    for yaml_file in yaml_files:
        if not validate_schema(yaml_file, schema_file):
            overall_success = False

    if not overall_success:
        sys.exit(1)
