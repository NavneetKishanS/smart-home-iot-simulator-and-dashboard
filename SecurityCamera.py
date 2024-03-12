import utils
from SmartDevice import SmartDevice

class SecurityCamera(SmartDevice):
    def __init__(self, device_id):
        """
        Initialize a SecurityCamera object.

        Args:
        - device_id (int or str): Identifier for the security camera.
        """
        super().__init__(device_id)
        self.is_recording = False
        self.motion_detected = False

    def start_recording(self):
        """
        Starts recording using the security camera.
        """
        self.is_recording = True

    def stop_recording(self):
        """
        Stops recording using the security camera.
        """
        self.is_recording = False

    def is_motion_detected(self):
        """
        Checks if motion is detected by the security camera.

        Returns:
        - bool: True if motion is detected, False otherwise.
        """
        return self.motion_detected

    def update_motion_detected(self):
        """
        Simulates motion detection using an external utility function and updates the motion detection status.

        Returns:
        - bool: True if motion is detected, False otherwise.
        """
        self.motion_detected = utils.random_motion_detection()
        return self.motion_detected
