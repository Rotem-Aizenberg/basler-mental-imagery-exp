#!/usr/bin/env python3
"""
Environment validation script for building the LSCI Experiment executable.
Run this before attempting to build to ensure all prerequisites are met.
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is suitable."""
    print("Checking Python version...")
    version = sys.version_info
    print(f"  Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3:
        print("  ✗ Python 3 is required")
        return False
    elif version.major == 3 and version.minor >= 12:
        # Python 3.12+ may have PsychoPy compatibility issues
        print("  ⚠ Python 3.12+ detected. PsychoPy may have compatibility issues.")
        print("    Recommended: Python 3.11.x")
        return True
    else:
        print("  ✓ Python version is suitable")
        return True

def check_pip():
    """Check if pip is available."""
    print("\nChecking pip...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"  ✓ pip is available: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("  ✗ pip is not available")
        return False

def check_required_files():
    """Check if all required project files exist."""
    print("\nChecking required project files...")
    
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    
    required_files = [
        project_root / "main.py",
        project_root / "requirements.txt",
        project_root / "config" / "defaults.json",
        project_root / "external_instruction_recordings",
        script_dir / "build_exe.spec",
    ]
    
    all_exist = True
    for file_path in required_files:
        if file_path.exists():
            print(f"  ✓ {file_path.relative_to(project_root)}")
        else:
            print(f"  ✗ {file_path.relative_to(project_root)} - NOT FOUND")
            all_exist = False
    
    return all_exist

def check_audio_files():
    """Check if all required audio files exist."""
    print("\nChecking audio files...")
    
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    audio_dir = project_root / "external_instruction_recordings"
    
    required_audio = [
        "close_your_eyes.mp3",
        "starting.mp3",
        "Open_your_eyes.mp3",
        "next_participant_please.mp3",
        "We_have_successfully_completed.mp3",
    ]
    
    all_exist = True
    for audio_file in required_audio:
        file_path = audio_dir / audio_file
        if file_path.exists():
            print(f"  ✓ {audio_file}")
        else:
            print(f"  ✗ {audio_file} - NOT FOUND")
            all_exist = False
    
    return all_exist

def check_pyinstaller():
    """Check if PyInstaller is installed."""
    print("\nChecking PyInstaller...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", "pyinstaller"],
            capture_output=True,
            text=True,
            check=True
        )
        print("  ✓ PyInstaller is installed")
        return True
    except subprocess.CalledProcessError:
        print("  ⚠ PyInstaller is not installed")
        print("    It will be installed automatically when you run the build script")
        return True  # Not a fatal error

def check_dependencies():
    """Check if project dependencies are installed."""
    print("\nChecking project dependencies...")
    
    script_dir = Path(__file__).parent.absolute()
    project_root = script_dir.parent
    requirements_file = project_root / "requirements.txt"
    
    if not requirements_file.exists():
        print("  ⚠ requirements.txt not found")
        return False
    
    # Read requirements
    with open(requirements_file) as f:
        packages = [line.split('>=')[0].split('==')[0].strip() 
                   for line in f if line.strip() and not line.startswith('#')]
    
    missing = []
    for package in packages:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "show", package],
                capture_output=True,
                check=True
            )
            print(f"  ✓ {package}")
        except subprocess.CalledProcessError:
            print(f"  ✗ {package} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n  ⚠ {len(missing)} package(s) missing")
        print("    They will be installed automatically when you run the build script")
        return True  # Not a fatal error
    else:
        print("\n  ✓ All dependencies are installed")
        return True

def check_disk_space():
    """Check if there's enough disk space."""
    print("\nChecking disk space...")
    
    script_dir = Path(__file__).parent.absolute()
    
    try:
        import shutil
        total, used, free = shutil.disk_usage(script_dir)
        free_gb = free // (2**30)  # Convert to GB
        
        print(f"  Available: {free_gb} GB")
        
        if free_gb < 2:
            print("  ⚠ Less than 2 GB available")
            print("    Building may fail due to insufficient disk space")
            print("    Recommended: At least 2-3 GB free")
            return False
        else:
            print("  ✓ Sufficient disk space")
            return True
    except Exception as e:
        print(f"  ⚠ Could not check disk space: {e}")
        return True

def main():
    """Run all validation checks."""
    print("=" * 60)
    print("LSCI Experiment - Build Environment Validation")
    print("=" * 60)
    
    checks = [
        ("Python version", check_python_version),
        ("pip availability", check_pip),
        ("Required files", check_required_files),
        ("Audio files", check_audio_files),
        ("Disk space", check_disk_space),
        ("PyInstaller", check_pyinstaller),
        ("Dependencies", check_dependencies),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print(f"\n  ✗ Error during check: {e}")
            results[name] = False
    
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    critical_checks = ["Python version", "pip availability", "Required files", "Audio files"]
    critical_failed = [name for name in critical_checks if not results.get(name, False)]
    
    if critical_failed:
        print("\n❌ Critical checks failed:")
        for name in critical_failed:
            print(f"  - {name}")
        print("\n⚠️  Please resolve these issues before building")
        return 1
    else:
        print("\n✓ All critical checks passed!")
        print("\nYou're ready to build the executable.")
        print("\nNext steps:")
        print("  1. Run build.bat (or: python build.py)")
        print("  2. Wait 5-10 minutes for the build to complete")
        print("  3. Find your executable in APP\\dist\\LSCIExperiment\\")
        return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        input("\nPress Enter to exit...")
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nValidation cancelled by user")
        input("\nPress Enter to exit...")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)
