#!/usr/bin/env python3
"""
Cross-platform build script for LSCI Experiment Windows Executable.
This script can be run on Windows to build the standalone executable.
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60 + "\n")

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"→ {description}...")
    try:
        result = subprocess.run(cmd, check=True, shell=True)
        print(f"✓ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - Failed")
        print(f"  Error: {e}")
        return False

def main():
    print_header("LSCI Experiment - Build Script")
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 11):
        print("⚠️  Warning: Python 3.11+ is recommended for this application")
    elif python_version.major == 3 and python_version.minor >= 12:
        # Python 3.12+ may have PsychoPy compatibility issues
        print("⚠️  Warning: Python 3.12+ detected. PsychoPy may have compatibility issues.")
        print("   Recommended: Python 3.11.x")
    
    # Get paths
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    
    print(f"Project root: {project_root}")
    print(f"APP folder: {script_dir}")
    
    # Step 1: Install PyInstaller
    print_header("Step 1: Installing PyInstaller")
    if not run_command(
        f"{sys.executable} -m pip install pyinstaller",
        "Installing PyInstaller"
    ):
        print("\n❌ Failed to install PyInstaller. Please install manually:")
        print(f"   {sys.executable} -m pip install pyinstaller")
        return 1
    
    # Step 2: Install application dependencies
    print_header("Step 2: Installing Application Dependencies")
    requirements_file = project_root / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"⚠️  Warning: requirements.txt not found at {requirements_file}")
        print("Continuing without installing dependencies...")
    else:
        if not run_command(
            f"{sys.executable} -m pip install -r {requirements_file}",
            "Installing dependencies from requirements.txt"
        ):
            print("\n⚠️  Warning: Some dependencies may have failed to install")
            print("The build will continue, but the executable may not work correctly")
    
    # Step 3: Build with PyInstaller
    print_header("Step 3: Building Executable")
    spec_file = script_dir / "build_exe.spec"
    
    if not spec_file.exists():
        print(f"❌ Error: Spec file not found at {spec_file}")
        return 1
    
    os.chdir(script_dir)
    if not run_command(
        f"pyinstaller {spec_file} --clean --noconfirm",
        "Building executable with PyInstaller"
    ):
        print("\n❌ Build failed. Check the error messages above.")
        return 1
    
    # Success
    print_header("Build Complete! ✓")
    
    dist_folder = script_dir / "dist" / "LSCIExperiment"
    exe_file = dist_folder / "LSCIExperiment.exe"
    
    print(f"📦 Application package created at:")
    print(f"   {dist_folder}")
    print()
    
    if exe_file.exists():
        print(f"🚀 Executable created:")
        print(f"   {exe_file}")
        print()
        print("To run the application:")
        print(f"   1. Navigate to {dist_folder}")
        print(f"   2. Double-click LSCIExperiment.exe")
    else:
        print(f"⚠️  Warning: LSCIExperiment.exe not found at expected location")
        print("The build may have completed but with a different output structure")
    
    print()
    print("To distribute the application:")
    print(f"   Copy the entire '{dist_folder.name}' folder to the target PC")
    print()
    print("For more information, see APP/README.md")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nPress Enter to exit...")
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n❌ Build cancelled by user")
        input("\nPress Enter to exit...")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)
