"""Audio package — configures PsychoPy audio backend before first import.

IMPORTANT: This module MUST be imported before any ``psychopy.sound``
import anywhere in the codebase.  The preference must be set before
PsychoPy initialises its audio subsystem.
"""

import logging

_configured_device = None
_logger = logging.getLogger(__name__)


def configure_audio(device_name: str = "") -> None:
    """Set up PsychoPy audio preferences.

    Args:
        device_name: Specific audio output device name. Empty string
            for system default.
    """
    global _configured_device
    try:
        from psychopy import prefs
        prefs.hardware['audioLib'] = ['ptb', 'sounddevice', 'pygame']
        prefs.hardware['audioLatencyMode'] = 3  # aggressive low-latency

        if device_name:
            prefs.hardware['audioDevice'] = [device_name]
            _configured_device = device_name
        # Otherwise leave audioDevice unset — let PsychoPy/PTB pick the
        # system default.  Previous code tried to resolve device names
        # via sounddevice, but those names don't always match what PTB
        # expects (e.g. "SONY TV (Intel(R) Display Audio)" vs PTB's own
        # enumeration), causing DeviceNotConnectedError on other PCs.
    except ImportError:
        pass


def reconfigure_audio_fallback() -> None:
    """Re-configure audio to try alternative backends after a device error.

    Called automatically by AudioManager when the primary backend fails.
    Switches to sounddevice backend which has broader device compatibility.
    """
    global _configured_device
    try:
        from psychopy import prefs
        prefs.hardware['audioLib'] = ['sounddevice', 'pygame']
        prefs.hardware['audioLatencyMode'] = 0  # safe mode
        if 'audioDevice' in prefs.hardware:
            prefs.hardware['audioDevice'] = []
        _configured_device = None
        _logger.info("Audio reconfigured to sounddevice fallback")
    except Exception:
        pass


def list_audio_devices():
    """Return list of available audio output device names.

    Filters out legacy Windows virtual devices (MME Sound Mapper etc.)
    that PTB cannot use.
    """
    _LEGACY = {"Microsoft Sound Mapper", "Primary Sound Driver"}
    try:
        import sounddevice as sd
        devices = sd.query_devices()
        output_devices = []
        seen = set()
        for d in devices:
            if d['max_output_channels'] > 0:
                name = d['name']
                if name not in seen and not any(leg in name for leg in _LEGACY):
                    output_devices.append(name)
                    seen.add(name)
        return output_devices
    except Exception:
        return []


# Auto-configure on import with system default
configure_audio()
