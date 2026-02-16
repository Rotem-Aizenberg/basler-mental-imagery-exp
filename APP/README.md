# LSCI Experiment - Standalone Windows Application

This folder contains the standalone Windows executable version of the LSCI Visual Mental Imagery Experiment application.

## 🎯 Purpose

The APP folder allows you to build and distribute a standalone Windows executable that can run on any Windows 11 PC **without requiring Python or Python packages to be installed**. The only requirement is the Basler Pylon SDK (for Lab Mode with Basler cameras).

---

## 📋 Prerequisites for Building

### On the Build Machine (Windows 11)

1. **Python 3.11.x** - Download from [python.org](https://www.python.org/downloads/)
2. **Basler Pylon SDK** (optional, but recommended for Lab Mode) - Download from [baslerweb.com](https://www.baslerweb.com/en/downloads/software-downloads/)
3. **Git** (to clone the repository) - Download from [git-scm.com](https://git-scm.com/)

---

## 🔨 Building the Executable

### Step 1: Clone the Repository

```bash
git clone https://github.com/Rotem-Aizenberg/basler-mental-imagery-exp.git
cd basler-mental-imagery-exp
```

### Step 2: Run the Build Script

Simply double-click `build.bat` in the APP folder, or run from command prompt:

```cmd
cd APP
build.bat
```

### Step 2.5: (Optional) Validate Environment

Before building, you can optionally validate that your environment is ready:

```cmd
python validate_environment.py
```

This will check:
- Python version
- Required files
- Audio files
- Disk space
- Dependencies

The build script will:
1. Install PyInstaller (the tool that creates the executable)
2. Install all application dependencies
3. Build the standalone executable
4. Package everything into `APP\dist\LSCIExperiment\`

**Build time:** Approximately 5-10 minutes depending on your system.

### Step 3: Test the Executable

After building, navigate to:
```
APP\dist\LSCIExperiment\
```

Double-click `LSCIExperiment.exe` to launch the application.

---

## 📦 Distributing the Application

### What to Distribute

After building successfully, copy the **entire** `APP\dist\LSCIExperiment\` folder to:
- A USB drive
- Network share
- Or zip it for download

### On the Target Windows 11 PC

**Requirements:**
- Windows 11 (or Windows 10)
- Basler Pylon SDK installed (for Lab Mode only - not needed for Dev Mode)
- No Python installation required! ✅
- No pip packages required! ✅

**Installation Steps:**
1. Copy the entire `LSCIExperiment` folder to any location on the PC (e.g., Desktop, Documents, C:\Programs)
2. Ensure Basler Pylon SDK is installed if using Lab Mode
3. Navigate into the folder
4. Double-click `LSCIExperiment.exe` to run

---

## 📂 What's Inside the Executable Package

The `dist\LSCIExperiment\` folder contains:

```
LSCIExperiment/
├── LSCIExperiment.exe          # Main application executable
├── external_instruction_recordings/  # MP3 audio instruction files
│   ├── close_your_eyes.mp3
│   ├── starting.mp3
│   ├── Open_your_eyes.mp3
│   ├── next_participant_please.mp3
│   └── We_have_successfully_completed.mp3
├── config/
│   └── defaults.json           # Default experiment configuration
├── [Various DLL files]          # Python runtime and dependencies
└── [Other support files]        # PyQt5, OpenCV, PsychoPy, etc.
```

**Important:** Users should run the application from within the `LSCIExperiment` folder. Do not move just the .exe file alone.

---

## 🎮 Running the Application

### First Launch

1. Navigate to the `LSCIExperiment` folder
2. Double-click `LSCIExperiment.exe`
3. The 5-step wizard will guide you through setup:
   - Mode Selection (Lab Mode or Dev Mode)
   - Experiment Settings
   - Camera Setup
   - Display & Audio
   - Subject Names

### Subsequent Launches

The application remembers your previous settings, so setup is faster on subsequent runs.

### Command Line Options (Optional)

You can also run from Command Prompt with options:

```cmd
# Launch in Dev Mode (webcam, no Basler camera needed)
LSCIExperiment.exe --dev-mode

# Use a custom configuration file
LSCIExperiment.exe --config path\to\config.json
```

---

## ⚙️ Application Features

### Lab Mode
- Uses Basler industrial camera (requires Pylon SDK)
- High-speed video recording (up to 500+ fps)
- Full experimental protocol support

### Dev Mode
- Uses system webcam (no Pylon needed)
- Lower frame rate (typically 30 fps)
- Perfect for testing and demonstrations
- **To use Dev Mode, launch with `--dev-mode` flag or select it in the wizard**

### Data Output

The application creates session folders with:
- Video recordings (.avi files)
- Event logs (CSV with millisecond timestamps)
- Session logs (Excel workbooks)
- Configuration snapshots

All data is saved to the output folder you specify in the wizard.

---

## 🔧 Troubleshooting

### "This app can't run on your PC"
- Make sure you're running on Windows 10 or 11
- Try running as Administrator (right-click → Run as administrator)

### "VCRUNTIME140.dll was not found"
- Install Microsoft Visual C++ Redistributable
- Download from [Microsoft](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

### "pypylon error" or "No camera detected"
- Install Basler Pylon SDK from [baslerweb.com](https://www.baslerweb.com/en/downloads/software-downloads/)
- Or use Dev Mode instead (select in wizard or use `--dev-mode` flag)

### Application won't start / crashes immediately
- Check Windows Event Viewer for error details
- Ensure all files in the LSCIExperiment folder are present
- Try running from Command Prompt to see error messages:
  ```cmd
  cd path\to\LSCIExperiment
  LSCIExperiment.exe
  ```

### Audio not playing / wrong output device
- Select the correct audio device in the "Display & Audio" wizard step
- Check Windows Sound settings

---

## 🔄 Updating the Application

To update to a newer version:

1. **On the build machine:**
   ```bash
   git pull
   cd APP
   build.bat
   ```

2. **On target PCs:**
   - Delete the old `LSCIExperiment` folder
   - Copy the new `APP\dist\LSCIExperiment\` folder

---

## 📝 Technical Details

### Build Tool
- **PyInstaller** - Packages Python applications into standalone executables

### Bundled Components
- Python 3.11 runtime
- PyQt5 (GUI framework)
- PsychoPy (stimulus presentation)
- OpenCV (video recording)
- NumPy (numerical operations)
- openpyxl (Excel logging)
- sounddevice (audio device selection)
- pypylon (Basler camera SDK - dynamically loaded)
- All application code and resources

### Executable Size
Approximately 300-500 MB (includes Python runtime and all libraries)

### Startup Time
First launch: 5-10 seconds (unpacking and initialization)
Subsequent launches: 2-5 seconds

---

## 🛡️ Security Notes

- The executable is not digitally signed. Windows SmartScreen may show a warning on first run.
- To bypass: Click "More info" → "Run anyway"
- For organizational deployment, consider code signing the executable

---

## 📞 Support

For issues or questions:
- Check the main repository README: [GitHub Repository](https://github.com/Rotem-Aizenberg/basler-mental-imagery-exp)
- Review the troubleshooting section above
- Contact the repository maintainer

---

## 📄 License

Same license as the main repository. This is a packaged distribution of the same application, not a separate product.

---

**Built with ❤️ for neuroscience research**
