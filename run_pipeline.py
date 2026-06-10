"""
Bluestock Mutual Fund Analytics Capstone
Master Pipeline Runner

Executes all major data processing scripts sequentially.
"""

import subprocess


def run_script(script_path):
    """Execute a Python script and display execution status."""
    print(f"\nRunning: {script_path}")
    subprocess.run(["python", script_path], check=True)
    print(f"Completed: {script_path}")


def main():
    """Run the complete ETL pipeline."""

    scripts = [
        "scripts/data_ingestion.py",
        "scripts/load_to_sqlite.py",
        "scripts/load_star_schema.py"
    ]

    for script in scripts:
        run_script(script)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()

