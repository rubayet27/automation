from pathlib import Path
import sys

# Get the module name from the VS Code task
if len(sys.argv) < 2:
    print("Please provide a module name.")
    sys.exit(1)

module_name = sys.argv[1].strip().lower()

# Allow only valid Python module names
if not module_name.isidentifier():
    print("Invalid module name. Use letters, numbers, and underscores.")
    sys.exit(1)

# Project folders and their corresponding filenames
file_structure = {
    "manager": f"{module_name}_manager.py",
    "model": f"{module_name}_model.py",
    "routes": f"{module_name}_route.py",
    "schemas": f"{module_name}_schema.py",
}

# Create files inside the app directory
app_dir = Path.cwd() / "app"

for folder, filename in file_structure.items():
    directory = app_dir / folder
    directory.mkdir(parents=True, exist_ok=True)

    file_path = directory / filename

    if file_path.exists():
        print(f"Already exists: {file_path}")
    else:
        file_path.touch()
        print(f"Created: {file_path}")

print(f"\nModule '{module_name}' setup completed!")