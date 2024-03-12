from SmartDevice import SmartDevice

class SmartLight(SmartDevice):
    def __init__(self, device_id):
        """
        Initialize a SmartLight object.

        Args:
        - device_id (int or str): Identifier for the smart light.
        """
        super().__init__(device_id)
        self.brightness = 0

    def set_brightness(self, level):
        """
        Sets the brightness level of the smart light and updates its status accordingly.

        Args:
        - level (int): Brightness level to be set.
        """
        self.brightness = level
        self.status = level > 0

    def get_brightness(self):
        """
        Returns the current brightness level of the smart light.

        Returns:
        - int: Current brightness level.
        """
        return self.brightness
