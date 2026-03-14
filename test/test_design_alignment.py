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

def test_mandatory_roles_present():
    """
    Test that all mandatory roles defined in design/unified_roles.md are present in the data.
    """
    data_path = os.path.join(base_dir, "src", "data", "fusion_framework.yaml")
    data = load_data(data_path)
    framework = data['framework']

    role_names = {r['name'] for r in framework['roles']}

    mandatory_roles = [
        "Handler of the Start (Strategic)",
        "Handler of Conflicts (Governance)",
        "Handler of Exceptions (Tactical)",
        "AI Orchestrator (Operational)",
        "Delivery Specialist (Technical)"
    ]

    for role in mandatory_roles:
        assert role in role_names, f"Mandatory role '{role}' is missing from framework data."

def test_mandatory_deliverables_present():
    """
    Test that key deliverables defined in design/unified_process_deliverables.md are present.
    """
    data_path = os.path.join(base_dir, "src", "data", "fusion_framework.yaml")
    data = load_data(data_path)
    framework = data['framework']

    deliv_names = {d['name'] for d in framework['deliverables']}

    mandatory_delivs = [
        "Project Vision",
        "Business Case",
        "Strategic Backlog",
        "Governance Guardrails",
        "Risk Register",
        "Tolerance Baseline",
        "Integrated Operational Plan",
        "Automated Status Feed",
        "Unified Traceability Ledger",
        "System Architecture",
        "Implementation Specs",
        "Deliverable Increment",
        "Quality & Compliance Evidence"
    ]

    for deliv in mandatory_delivs:
        assert deliv in deliv_names, f"Mandatory deliverable '{deliv}' is missing from framework data."

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
