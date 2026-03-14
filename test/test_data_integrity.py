import os
import sys

# Add the project root to sys.path to allow importing from src
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

from src.scripts.validate_schema import validate_schema

def test_data_validation():
    """
    Test that all YAML files in src/data are valid according to the framework schema.
    """
    schema_file = os.path.join(base_dir, "src", "schema", "framework.schema.json")
    data_dir = os.path.join(base_dir, "src", "data")

    # Get all YAML files in src/data
    yaml_files = [f for f in os.listdir(data_dir) if f.endswith(('.yaml', '.yml'))]

    assert len(yaml_files) > 0, "No data files found in src/data"

    overall_success = True
    for yaml_file in yaml_files:
        file_path = os.path.join(data_dir, yaml_file)
        if not validate_schema(file_path, schema_file):
            overall_success = False

    assert overall_success, "One or more YAML files failed schema validation."

import pytest

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
