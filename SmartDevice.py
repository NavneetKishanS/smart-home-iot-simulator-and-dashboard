class SmartDevice:
    def __init__(self, device_id):
        """
        Initialize a SmartDevice object.

        Args:
        - device_id (int or str): Identifier for the smart device.
        """
        self.device_id = device_id
        self.status = False

    def turn_on(self):
        """
        Turns on the smart device.
        """
        self.status = True

    def turn_off(self):
        """
        Turns off the smart device.
        """
        self.status = False

    def toggle_device(self):
        """
        Toggles the status of the smart device (switches it on if it's off and vice versa).
        """
        self.status = not self.status

    def get_status(self):
        """
        Returns the current status of the smart device.

        Returns:
        - bool: Current status of the device (True for on, False for off).
        """
        return self.status
