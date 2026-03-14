import json
import yaml
import jsonschema
import sys
import os

def validate(data_path, schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    with open(data_path, 'r') as f:
        if data_path.endswith('.yaml') or data_path.endswith('.yml'):
            data = yaml.safe_load(f)
        else:
            data = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"Validation successful for {data_path} against {schema_path}")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation failed for {data_path} against {schema_path}")
        print(f"Error: {e.message}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_schema.py <data_path> <schema_path>")
        sys.exit(1)

    success = validate(sys.argv[1], sys.argv[2])
    if not success:
        sys.exit(1)
