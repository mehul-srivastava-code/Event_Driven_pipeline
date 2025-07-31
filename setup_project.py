import os

folders = [
    "data",
    "processed",
    "scripts",
    "terraform",
    ".github/workflows"
]

files_to_create = [
    "scripts/ingest.py",
    "scripts/process.py",
    "scripts/report.py",
    "terraform/main.tf",
    ".github/workflows/ci.yml",
    "Jenkinsfile",
    "README.md"
]

def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

def create_files():
    for file in files_to_create:
    
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass
            print(f"Created empty file: {file}")
        else:
            print(f"File already exists: {file}")

if __name__ == "__main__":
    create_folders()
    create_files()
