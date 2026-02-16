# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for LSCI Visual Mental Imagery Experiment.
This spec file bundles the entire application into a standalone Windows executable.
"""

import os
import sys
from pathlib import Path

# Get the project root directory (parent of APP folder)
project_root = Path(SPECPATH).parent.absolute()

block_cipher = None

# Collect data files
datas = []

# Add MP3 audio files
audio_dir = project_root / 'external_instruction_recordings'
if audio_dir.exists():
    for mp3_file in audio_dir.glob('*.mp3'):
        datas.append((str(mp3_file), 'external_instruction_recordings'))

# Add config file
config_file = project_root / 'config' / 'defaults.json'
if config_file.exists():
    datas.append((str(config_file), 'config'))

# Collect all Python files from the project
a = Analysis(
    [str(project_root / 'main.py')],
    pathex=[str(project_root)],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'numpy',
        'cv2',
        'openpyxl',
        'pypylon',
        'psychopy',
        'psychopy.visual',
        'psychopy.sound',
        'psychopy.core',
        'sounddevice',
        'soundfile',
        'psychopy.hardware',
        'psychopy.data',
        'psychopy.event',
        'psychopy.monitors',
        'PIL',
        'scipy',
        'matplotlib',
        'pandas',
        'json',
        'logging',
        'threading',
        'queue',
        'pathlib',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',  # Excludes tk and tcl automatically
        'jupyter',
        'IPython',
        'notebook',
        'sphinx',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LSCIExperiment',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window (GUI application)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Can add an icon file later if needed
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LSCIExperiment',
)
