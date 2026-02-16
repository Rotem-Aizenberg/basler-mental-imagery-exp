# Installation Guide for Windows 11 Users

## 📥 Receiving the Pre-built Application

If you received the `LSCIExperiment` folder from the repository maintainer, follow these simple steps to get started.

---

## ✅ Prerequisites

### Required (for Lab Mode with Basler Camera)
- **Windows 11** (or Windows 10)
- **Basler Pylon SDK** - Download and install from [baslerweb.com](https://www.baslerweb.com/en/downloads/software-downloads/)
  - This is ONLY needed if you want to use a Basler camera (Lab Mode)
  - For testing with a webcam (Dev Mode), this is NOT required

### NOT Required
- ❌ Python installation
- ❌ pip packages
- ❌ Development tools
- ❌ Git

---

## 🚀 Installation Steps

### Step 1: Copy the Application

Copy the entire `LSCIExperiment` folder to your Windows 11 PC. You can place it:
- On your Desktop
- In your Documents folder
- In `C:\Program Files\` (may require administrator rights)
- On any drive with sufficient space (at least 1 GB free)

**Important:** Keep all files together in the same folder. Do not move just the .exe file alone.

### Step 2: Install Pylon SDK (Lab Mode Only)

If you plan to use a Basler camera:

1. Download Basler Pylon SDK from: https://www.baslerweb.com/en/downloads/software-downloads/
2. Run the installer
3. Follow the installation wizard (default settings are fine)
4. Restart your computer if prompted

**Skip this step** if you only want to use Dev Mode (webcam).

### Step 3: First Run

1. Open the `LSCIExperiment` folder
2. Double-click `LSCIExperiment.exe`
3. If Windows shows a security warning:
   - Click "More info"
   - Click "Run anyway"
   - This warning appears because the application is not digitally signed

The application should start and show the setup wizard.

---

## 🎮 Using the Application

### First Launch - Setup Wizard

The first time you run the application, a 5-step wizard will guide you through setup:

1. **Mode Selection**
   - **Lab Mode**: Uses Basler camera (requires Pylon SDK)
   - **Dev Mode**: Uses webcam (no Pylon needed) - Great for testing!

2. **Experiment Settings**
   - Select shapes (circle, square, triangle, star)
   - Set repetitions and timing
   - Choose output folder for data

3. **Camera Setup**
   - Live preview
   - Adjust resolution, exposure, gain, frame rate

4. **Display & Audio**
   - Select participant screen (if multiple monitors)
   - Select audio output device

5. **Subjects**
   - Add participant names
   - Can load names from previous sessions

### Running an Experiment

After setup:
1. The main operator window appears with:
   - Session queue (left panel)
   - Control buttons and progress (center)
   - Live camera preview (right panel)

2. Click **Start** to begin the experiment
3. Use **Pause** if needed (interrupts current trial)
4. Use **Resume** to continue
5. Click **Stop** to end the session

### Command Line Options (Advanced)

You can also run from Command Prompt with options:

```cmd
# Open the folder in Command Prompt
cd C:\path\to\LSCIExperiment

# Launch in Dev Mode directly
LSCIExperiment.exe --dev-mode

# Use a custom configuration file
LSCIExperiment.exe --config C:\path\to\config.json
```

---

## 📂 Data Output

The application saves data to the output folder you specified in the wizard:

```
YourOutputFolder/
├── session_YYYY-MM-DD_HH-MM-SS/
│   ├── event_log.csv              # Detailed event timestamps
│   ├── session_log.xlsx           # Per-trial summary
│   ├── session_config.json        # Configuration snapshot
│   └── subjects/
│       └── [participant folders with video recordings]
└── MAIN_experiment_monitoring.xlsx  # Cross-session monitoring
```

**Video files:** Saved as `.avi` files in each subject's folder, organized by repetition and shape.

---

## 🔧 Troubleshooting

### "Windows protected your PC" message
- Click "More info"
- Click "Run anyway"
- This is a SmartScreen warning for unsigned applications

### "This app can't run on your PC"
- Ensure you're on Windows 10 or 11 (64-bit)
- Try running as Administrator (right-click → Run as administrator)

### "VCRUNTIME140.dll was not found"
- Install Microsoft Visual C++ Redistributable
- Download from: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist

### "pypylon error" or "Camera not detected"
**Option 1:** Install Basler Pylon SDK
- Download from: https://www.baslerweb.com/en/downloads/software-downloads/

**Option 2:** Use Dev Mode instead
- Run with: `LSCIExperiment.exe --dev-mode`
- Or select Dev Mode in the wizard

### Application crashes or won't start
1. Check that all files are present in the folder
2. Try running from Command Prompt to see error messages:
   ```cmd
   cd C:\path\to\LSCIExperiment
   LSCIExperiment.exe
   ```
3. Check Windows Event Viewer for error details

### No audio / wrong audio device
- In the wizard, select the correct audio output device
- Check Windows Sound settings
- Ensure the device is not muted

### Webcam not available in Dev Mode
- Close other applications using the webcam (Skype, Teams, etc.)
- Check Windows Camera Privacy settings
- Try a different webcam if available

---

## 💾 Saving Settings

The application remembers your settings between sessions:
- Last used output folder
- Subject name history
- Last experiment configuration
- Audio and display preferences

Settings are stored in a `.app_memory` folder created in the application directory.

---

## 🔄 Updating the Application

To update to a newer version:

1. **Before updating:**
   - Finish any ongoing experiments
   - Back up your data output folder
   - Note your current settings (they will be preserved if you don't delete the `.app_memory` folder)

2. **Update process:**
   - Delete the old `LSCIExperiment` folder
   - Copy the new `LSCIExperiment` folder to the same location
   - Your previous settings will be lost, but you can copy the `.app_memory` folder from the old version

---

## 📞 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review the main README in the application folder
3. Contact the repository maintainer
4. Visit: https://github.com/Rotem-Aizenberg/basler-mental-imagery-exp

---

## 🔒 Privacy & Security

- The application does not connect to the internet
- All data is stored locally on your computer
- No telemetry or usage tracking
- No personal data is collected beyond what you enter (participant names, etc.)

---

## 💡 Tips

- **Test first:** Use Dev Mode with a webcam to familiarize yourself with the interface before using Lab Mode
- **Dual monitors:** Recommended - one for operator (you), one for participant (fullscreen stimulus)
- **Output folder:** Choose a location with plenty of space - video files can be large
- **Backup data:** Regularly back up your experimental data to an external drive or cloud storage
- **Participant comfort:** Ensure participants are comfortable with the setup before starting

---

## 📄 License

This application is distributed under the same license as the source repository.

---

**Ready to conduct your experiment!** 🧠✨
