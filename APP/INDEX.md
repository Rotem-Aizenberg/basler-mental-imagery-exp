# APP Folder - Documentation Index

Welcome to the APP folder! This folder contains everything needed to create and distribute a standalone Windows executable of the LSCI Visual Mental Imagery Experiment.

## 📚 Which Document Should I Read?

### For End Users (Who Received the Pre-built Application)
👉 **Start here:** [INSTALLATION.md](INSTALLATION.md)
- Simple installation instructions
- How to run the application
- Troubleshooting guide
- No Python or technical knowledge required

### For Quick Overview
👉 **Start here:** [QUICKSTART.md](QUICKSTART.md)
- Brief summary
- Quick decision guide (download vs build)
- Links to detailed docs

### For Developers (Building the Executable)
👉 **Start here:** [README.md](README.md)
- Complete build instructions
- Technical details
- Distribution guide
- Troubleshooting for build process

## 📁 Files in this Folder

### Documentation
- **INSTALLATION.md** - For end users receiving the pre-built app
- **README.md** - For developers building the executable
- **QUICKSTART.md** - Brief overview for everyone
- **INDEX.md** - This file

### Build Scripts
- **build.bat** - Windows batch script to build the executable
- **build.py** - Python script to build the executable (cross-platform)
- **build_exe.spec** - PyInstaller specification file

### Validation
- **validate_environment.py** - Checks if your environment is ready to build

## 🎯 Common Tasks

### I want to use the application
1. Receive the pre-built `LSCIExperiment` folder from the maintainer
2. Follow [INSTALLATION.md](INSTALLATION.md)
3. Run `LSCIExperiment.exe`

### I want to build the executable
1. Read [README.md](README.md)
2. (Optional) Run `python validate_environment.py`
3. Run `build.bat` or `python build.py`
4. Wait 5-10 minutes
5. Find the result in `dist/LSCIExperiment/`

### I want to distribute the application
1. Build the executable (see above)
2. Copy the entire `dist/LSCIExperiment/` folder
3. Share it with end users
4. Direct them to [INSTALLATION.md](INSTALLATION.md)

### I want to understand the technical details
1. Read [README.md](README.md) - full technical documentation
2. Review `build_exe.spec` - PyInstaller configuration
3. Check the main repository README - application functionality

## 🔗 Related Documentation

- **Main Repository README:** `/README.md` - Full application documentation
- **Requirements:** `/requirements.txt` - Python dependencies
- **Default Config:** `/config/defaults.json` - Default experiment settings

## ❓ Still Have Questions?

- **For application usage:** See the main repository README
- **For build issues:** See troubleshooting section in README.md
- **For installation issues:** See troubleshooting section in INSTALLATION.md
- **For development questions:** Contact the repository maintainer

---

**Quick Links:**
- 🌐 Repository: https://github.com/Rotem-Aizenberg/basler-mental-imagery-exp
- 📦 Basler Pylon SDK: https://www.baslerweb.com/en/downloads/software-downloads/
- 🐍 Python 3.11: https://www.python.org/downloads/
