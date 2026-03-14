import os
import sys
import subprocess
import pytest

# Add the project root to sys.path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_generate_deliverables_script():
    """
    Test that the generate_deliverables.py script runs successfully and produces the expected files.
    """
    script_path = os.path.join(base_dir, "src", "scripts", "generate_deliverables.py")
    docs_dir = os.path.join(base_dir, "src", "docs")
    images_dir = os.path.join(base_dir, "src", "images")

    # Expected output files in docs
    expected_docs = [
        "framework_overview.md",
        "raci_matrix.md",
        "process_flow.mmd"
    ]

    # Expected output files in images
    expected_images = [
        "process_flow.png",
        "process_flow.svg"
    ]

    # Run the script
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)

    assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    # Check if doc files were created
    for filename in expected_docs:
        filepath = os.path.join(docs_dir, filename)
        assert os.path.exists(filepath), f"Expected file '{filename}' was not generated in docs."
        assert os.path.getsize(filepath) > 0, f"Generated file '{filename}' is empty."

    # Check if image files were created
    for filename in expected_images:
        filepath = os.path.join(images_dir, filename)
        assert os.path.exists(filepath), f"Expected image '{filename}' was not generated."
        assert os.path.getsize(filepath) > 0, f"Generated image '{filename}' is empty."

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
