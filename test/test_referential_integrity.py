import os
import sys
import yaml
import pytest

# Add the project root to sys.path to allow importing from src
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, base_dir)

def load_data(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def test_referential_integrity():
    """
    Test that all IDs referenced in the framework data exist.
    """
    data_path = os.path.join(base_dir, "src", "data", "fusion_framework.yaml")
    data = load_data(data_path)
    framework = data['framework']

    # Collect all existing IDs
    role_ids = {r['id'] for r in framework['roles']}
    deliv_ids = {d['id'] for d in framework['deliverables']}
    step_ids = {s['id'] for s in framework['process_steps']}

    errors = []

    # Check deliverables
    for d in framework['deliverables']:
        if d['accountability_id'] not in role_ids:
            errors.append(f"Deliverable '{d['id']}' references unknown role '{d['accountability_id']}'")

    # Check process steps
    for s in framework['process_steps']:
        if s['primary_role_id'] not in role_ids:
            errors.append(f"Step '{s['id']}' references unknown primary role '{s['primary_role_id']}'")

        for inp in s.get('inputs', []):
            if inp not in deliv_ids:
                errors.append(f"Step '{s['id']}' references unknown input deliverable '{inp}'")

        for outp in s.get('outputs', []):
            if outp not in deliv_ids:
                errors.append(f"Step '{s['id']}' references unknown output deliverable '{outp}'")

    assert not errors, "Referential integrity errors found:\n" + "\n".join(errors)

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
