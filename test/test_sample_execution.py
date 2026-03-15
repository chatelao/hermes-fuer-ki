import os
import sys
import subprocess
import pytest

# Add the project root to sys.path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_execute_project_script():
    """
    Test that the execute_project.py script runs successfully for the sample project.
    """
    script_path = os.path.join(base_dir, "src", "scripts", "execute_project.py")
    manifest_path = os.path.join(base_dir, "src", "data", "samples", "project_phoenix", "project_manifest.yaml")
    report_path = os.path.join(base_dir, "src", "docs", "samples", "project_phoenix_report.md")

    # Run the script
    result = subprocess.run([sys.executable, script_path, manifest_path], capture_output=True, text=True)

    assert result.returncode == 0, f"Script failed with error: {result.stderr}"
    assert os.path.exists(report_path), "Project report was not generated."
    assert os.path.getsize(report_path) > 0, "Generated report is empty."

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
