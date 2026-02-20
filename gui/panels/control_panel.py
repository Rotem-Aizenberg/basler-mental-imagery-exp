"""Dynamic experiment control buttons."""

from __future__ import annotations

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
)

from core.enums import ExperimentState


class ControlPanel(QGroupBox):
    """Experiment control buttons with dynamic visibility."""

    start_clicked = pyqtSignal()
    pause_clicked = pyqtSignal()
    resume_clicked = pyqtSignal()
    stop_clicked = pyqtSignal()
    confirm_clicked = pyqtSignal()
    skip_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__("Controls", parent)
        self._is_paused = False
        self._preparing = False  # True between Start and first WAITING_CONFIRM
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        self._start_btn = QPushButton("Start")
        self._start_btn.setStyleSheet(
            "font-weight: bold; padding: 10px 20px; font-size: 13px;"
        )
        self._start_btn.clicked.connect(self.start_clicked)
        btn_layout.addWidget(self._start_btn)

        self._pause_btn = QPushButton("Pause")
        self._pause_btn.setStyleSheet("padding: 10px;")
        self._pause_btn.clicked.connect(self._on_pause_toggle)
        self._pause_btn.hide()
        btn_layout.addWidget(self._pause_btn)

        self._confirm_btn = QPushButton("Confirm Next")
        self._confirm_btn.setStyleSheet(
            "background-color: #2e7d32; color: white; padding: 10px; font-weight: bold;"
        )
        self._confirm_btn.clicked.connect(self.confirm_clicked)
        self._confirm_btn.hide()
        btn_layout.addWidget(self._confirm_btn)

        self._skip_btn = QPushButton("Skip")
        self._skip_btn.setStyleSheet("padding: 10px;")
        self._skip_btn.clicked.connect(self.skip_clicked)
        self._skip_btn.hide()
        btn_layout.addWidget(self._skip_btn)

        self._stop_btn = QPushButton("Stop")
        self._stop_btn.setStyleSheet(
            "background-color: #c62828; color: white; padding: 10px; font-weight: bold;"
        )
        self._stop_btn.clicked.connect(self.stop_clicked)
        self._stop_btn.hide()
        btn_layout.addWidget(self._stop_btn)

        self._wait_label = QLabel("Please wait.. preparing the experiment...")
        self._wait_label.setAlignment(Qt.AlignCenter)
        self._wait_label.setStyleSheet(
            "font-size: 13px; font-weight: bold; color: #1565c0; padding: 10px;"
        )
        self._wait_label.hide()
        btn_layout.addWidget(self._wait_label)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def _on_pause_toggle(self) -> None:
        if self._is_paused:
            self.resume_clicked.emit()
            self._pause_btn.setText("Pause")
            self._is_paused = False
        else:
            self.pause_clicked.emit()
            self._pause_btn.setText("Resume")
            self._is_paused = True

    def set_preparing(self) -> None:
        """Show 'Please wait' instead of buttons while engine initializes."""
        self._preparing = True
        self._start_btn.hide()
        self._pause_btn.hide()
        self._confirm_btn.hide()
        self._skip_btn.hide()
        self._stop_btn.hide()
        self._wait_label.show()

    def update_for_state(self, state: ExperimentState) -> None:
        """Show/hide buttons based on experiment state."""
        # Hide all first
        self._start_btn.hide()
        self._pause_btn.hide()
        self._confirm_btn.hide()
        self._skip_btn.hide()
        self._stop_btn.hide()
        self._wait_label.hide()

        if state == ExperimentState.IDLE:
            self._start_btn.show()

        elif state == ExperimentState.RUNNING:
            if self._preparing:
                # Still initializing — keep showing "Please wait"
                self._wait_label.show()
                return
            self._pause_btn.show()
            self._stop_btn.show()

        elif state == ExperimentState.PAUSED:
            self._pause_btn.show()
            self._pause_btn.setText("Resume")
            self._is_paused = True
            self._stop_btn.show()

        elif state == ExperimentState.WAITING_CONFIRM:
            self._preparing = False  # Engine is ready
            self._confirm_btn.show()
            self._skip_btn.show()
            self._stop_btn.show()

        elif state in (ExperimentState.COMPLETED, ExperimentState.ABORTED, ExperimentState.ERROR):
            self._preparing = False
            pass

    def set_idle(self) -> None:
        """Reset to idle state."""
        self._is_paused = False
        self._pause_btn.setText("Pause")
        self._start_btn.setText("Start")
        self.update_for_state(ExperimentState.IDLE)
