from SmartDevice import SmartDevice

class Thermostat(SmartDevice):
    def __init__(self, device_id, default_temperature=22):
        """
        Initialize a Thermostat object.

        Args:
        - device_id (int or str): Identifier for the thermostat.
        - default_temperature (int or float): Default temperature setting for the thermostat (default is 22).
        """
        super().__init__(device_id)
        self.temperature = default_temperature

    def set_temperature(self, temperature):
        """
        Set the temperature of the thermostat to a specific value.

        Args:
        - temperature (int or float): Temperature value to set.
        """
        self.temperature = temperature

    def increase_temperature(self, delta=1):
        """
        Increase the temperature of the thermostat by a specified delta.

        Args:
        - delta (int or float): Amount by which to increase the temperature (default is 1).
        """
        self.temperature += delta

    def decrease_temperature(self, delta=1):
        """
        Decrease the temperature of the thermostat by a specified delta.

        Args:
        - delta (int or float): Amount by which to decrease the temperature (default is 1).
        """
        self.temperature -= delta

    def get_temperature(self):
        """
        Get the current temperature setting of the thermostat.

        Returns:
        - int or float: Current temperature setting.
        """
        return self.temperature
