"""Quick validation script to check if the project is set up correctly."""
import os
import sys
from pathlib import Path


def check_file_exists(filepath: str, description: str) -> bool:
    """Check if a file exists."""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filepath}")
    return exists


def main():
    """Validate project setup."""
    print("Validating project setup...\n")
    
    required_files = [
        ("main.py", "Main entry point"),
        ("agent.py", "Agentic system"),
        ("data_loader.py", "Data loader"),
        ("config.py", "Configuration"),
        ("requirements.txt", "Dependencies"),
        (".gitignore", "Git ignore file"),
        ("README.md", "README"),
        ("env_template.txt", "Environment template"),
    ]
    
    optional_files = [
        ("EVAL_CHECKLIST.md", "Evaluation checklist"),
        ("generate_sample_data.py", "Sample data generator"),
        ("setup_github.sh", "GitHub setup script (Linux/Mac)"),
        ("setup_github.ps1", "GitHub setup script (Windows)"),
    ]
    
    all_good = True
    
    print("Required files:")
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_good = False
    
    print("\nOptional files:")
    for filepath, description in optional_files:
        check_file_exists(filepath, description)
    
    # Check for .env file (should exist but not be committed)
    print("\nConfiguration:")
    env_exists = os.path.exists(".env")
    if env_exists:
        print("✓ .env file exists (make sure it's in .gitignore)")
    else:
        print("⚠ .env file not found - create it from env_template.txt")
    
    # Check for data file
    data_exists = os.path.exists("synthetic_fb_ads_undergarments.csv")
    if data_exists:
        print("✓ Data file exists: synthetic_fb_ads_undergarments.csv")
    else:
        print("⚠ Data file not found - run generate_sample_data.py to create sample data")
    
    # Check for output directory
    output_exists = os.path.exists("output")
    if output_exists:
        print("✓ Output directory exists")
    else:
        print("ℹ Output directory will be created automatically")
    
    print("\n" + "=" * 50)
    if all_good:
        print("✅ All required files are present!")
        print("\nNext steps:")
        print("1. Create .env file from env_template.txt")
        print("2. Add your OpenAI API key to .env")
        print("3. Place synthetic_fb_ads_undergarments.csv in project root")
        print("4. Run: python main.py")
    else:
        print("❌ Some required files are missing!")
        sys.exit(1)


if __name__ == "__main__":
    main()

