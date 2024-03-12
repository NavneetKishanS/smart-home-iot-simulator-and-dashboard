import tkinter as tk
import tkinter.ttk as ttk
from SmartDevice import SmartDevice
from SecurityCamera import SecurityCamera
from SmartLight import SmartLight
from Thermostat import Thermostat


class SmartDeviceGUI:
    def __init__(self, master):
        """
        Initialize the SmartDeviceGUI.

        Args:
        - master: Parent widget.
        """
        self.master = master
        self.devices = []
        self.device_labels = {}
        self.master_temperature_frame = None  # Initialize master_temperature_frame

        self.setup_default_devices()
        self.create_dashboard()
        #self.setup_master_brightness_control()
        #self.setup_master_temperature_control()
        self.create_add_device_button()

    def setup_default_devices(self):
        # Create default instances of each device type
        self.devices.append(SmartLight("SmartLight1"))
        self.devices.append(SecurityCamera("SecurityCamera1"))
        self.devices.append(Thermostat("Thermostat1"))

    def create_dashboard(self):
        """
        Create default instances of each device type and add them to the devices list.
        """
        self.master.title("Smart Home Dashboard")

        for device in self.devices:
            frame = tk.Frame(self.master)
            frame.pack(fill=tk.BOTH, expand=True)

            # Toggle button on the left
            toggle_frame = tk.Frame(frame)
            toggle_frame.pack(side=tk.LEFT, padx=10)

            toggle_button = tk.Button(toggle_frame, text="Toggle " + type(device).__name__,
                                      command=lambda d=device: self.toggle_device(d))
            toggle_button.pack()

            # Device information on the right
            info_frame = tk.Frame(frame)
            info_frame.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)

            device_info = tk.Label(info_frame,
                                   text=f"Device: {type(device).__name__}\nID: {device.device_id}\nStatus: OFF")
            device_info.pack()

            if isinstance(device, SmartLight):
                self.setup_brightness_controls(device, info_frame)
            elif isinstance(device, Thermostat):
                self.setup_temperature_controls(device, info_frame)

            self.device_labels[device.device_id] = device_info  # Add device label to device_labels

        self.update_existing_smartlights()  # Update existing devices to ensure labels are properly set

    def setup_temperature_controls(self, device, info_frame):
        """
        Set up temperature controls for a Thermostat device.

        Args:
        - device: The Thermostat device.
        - info_frame: The frame to place the controls in.
        """
        temperature_frame = tk.Frame(info_frame)
        temperature_frame.pack(anchor=tk.E, padx=10)

        temperature_label = tk.Label(temperature_frame, text="Temperature:")
        temperature_label.pack(side=tk.LEFT)

        temperature_value = tk.StringVar()
        temperature_value.set(str(device.get_temperature()))

        temperature_entry = tk.Entry(temperature_frame, textvariable=temperature_value, width=5)
        temperature_entry.pack(side=tk.LEFT)

        temperature_scrollbar = ttk.Scale(temperature_frame, orient=tk.HORIZONTAL,
                                          from_=0, to=40, command=lambda v, d=device, tv=temperature_value:
            self.change_temperature(v, d, tv))
        temperature_scrollbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        temperature_scrollbar.set(device.get_temperature())  # Set the initial temperature


    def setup_master_temperature_control(self):
        """
        Set up master temperature control for all Thermostat devices.
        """
        master_temperature_frame = tk.Frame(self.master)
        master_temperature_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        master_temperature_label = tk.Label(master_temperature_frame, text="Master Temperature:")
        master_temperature_label.pack(side=tk.LEFT)

        master_temperature_value = tk.StringVar()
        master_temperature_value.set("22")

        master_temperature_entry = tk.Entry(master_temperature_frame, textvariable=master_temperature_value, width=5)
        master_temperature_entry.pack(side=tk.LEFT)

        master_temperature_scrollbar = ttk.Scale(master_temperature_frame, orient=tk.HORIZONTAL,
                                                  from_=0, to=40, command=self.change_master_temperature)
        master_temperature_scrollbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def change_master_temperature(self, val):
        """
        Change the temperature for all Thermostat devices based on the master temperature control value.

        Args:
        - val: New temperature value.
        """
        master_temperature = int(float(val))
        for device in self.devices:
            if isinstance(device, Thermostat):
                device.set_temperature(master_temperature)

    def change_temperature(self, val, device, temperature_value):

        temperature = int(float(val))
        temperature_value.set(str(temperature))
        device.set_temperature(temperature)

    def toggle_device(self, device):
        device.toggle_device()
        device_id = device.device_id

        if device_id in self.device_labels:
            device_label = self.device_labels[device_id]
            status_text = f"Device: {type(device).__name__}\nID: {device_id}\nStatus: {'ON' if device.get_status() else 'OFF'}"
            device_label.config(text=status_text)

    def add_device(self, device_type, device_id):
        """
        Add a new device based on the provided type and ID.

        Args:
        - device_type: Type of the device to add.
        - device_id: ID of the new device.
        """
        new_device = None
        if device_type == "SmartLight":
            new_device = SmartLight(device_id)
        elif device_type == "SecurityCamera":
            new_device = SecurityCamera(device_id)
        elif device_type == "Thermostat":
            new_device = Thermostat(device_id)

        if new_device:
            self.devices.append(new_device)
            frame = tk.Frame(self.master)
            frame.pack(fill=tk.BOTH, expand=True)

            # Toggle button on the left
            toggle_button_frame = tk.Frame(frame)
            toggle_button_frame.pack(side=tk.LEFT, padx=10)

            toggle_button = tk.Button(toggle_button_frame, text="Toggle " + type(new_device).__name__,
                                      command=lambda d=self.devices[-1]: self.toggle_device(d))
            toggle_button.pack()

            # Device information on the right
            info_frame = tk.Frame(frame)
            info_frame.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)

            device_info = tk.Label(info_frame,
                                   text=f"Device: {type(new_device).__name__}\nID: {new_device.device_id}\nStatus: OFF")
            device_info.pack()

            if isinstance(new_device, SmartLight) or isinstance(new_device, SecurityCamera) or isinstance(new_device,Thermostat):
                self.device_labels[new_device.device_id] = device_info

            if isinstance(new_device, SmartLight):
                self.setup_brightness_controls(new_device, info_frame)
            elif isinstance(new_device, Thermostat):
                self.setup_temperature_controls(new_device, info_frame)


    def setup_brightness_controls(self, device, info_frame):
        brightness_frame = tk.Frame(info_frame)
        brightness_frame.pack(anchor=tk.E, padx=10)

        brightness_label = tk.Label(brightness_frame, text="Brightness:")
        brightness_label.pack(side=tk.LEFT)

        brightness_value = tk.StringVar()
        brightness_value.set(str(device.get_brightness()))

        brightness_entry = tk.Entry(brightness_frame, textvariable=brightness_value, width=5)
        brightness_entry.pack(side=tk.LEFT)

        brightness_scrollbar = ttk.Scale(brightness_frame, orient=tk.HORIZONTAL,
                                         from_=0, to=100, command=lambda v, d=device, bv=brightness_value:
                                         self.change_brightness(v, d, bv))
        brightness_scrollbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        brightness_scrollbar.set(device.get_brightness())  # Set the initial brightness

    def setup_master_brightness_control(self):
        self.master_brightness_frame = tk.Frame(self.master)
        self.master_brightness_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

    def change_master_brightness(self, val):
        master_brightness = int(float(val))
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.set_brightness(master_brightness)

    def change_brightness(self, val, device, brightness_value):
        """
        Change the brightness level for a SmartLight device.

        Args:
        - val: New brightness value.
        - device: The SmartLight device.
        - brightness_value: Tkinter StringVar for the brightness value.
        """
        brightness = int(float(val))
        brightness_value.set(str(brightness))
        device.set_brightness(brightness)

    def update_existing_smartlights(self):
        """
        Update existing SmartLight devices to ensure labels are properly set.
        """
        smartlight_devices = [device for device in self.devices if isinstance(device, SmartLight)]
        for device in smartlight_devices:
            if device.device_id in self.device_labels:
                device_label = self.device_labels[device.device_id]
                brightness_controls = [child for child in device_label.master.winfo_children() if
                                       isinstance(child, ttk.Scale)]
                if len(brightness_controls) > 1:
                    brightness_controls[-1].destroy()  # Remove the last (newly added) brightness control

    def add_from_input(self, device_type, device_id, window):
        """
        Add a new device based on user input from the prompt window.

        Args:
        - device_type: Type of the device to add.
        - device_id: ID of the new device.
        - window: The prompt window.
        """
        self.add_device(device_type, device_id)
        self.update_existing_smartlights()
        window.destroy()

    def change_brightness(self, val, device, brightness_value):
        brightness = int(float(val))
        brightness_value.set(str(brightness))
        device.set_brightness(brightness)

        # If the light was off and brightness is changed, turn it on
        if not device.get_status() and brightness > 0:
            device.toggle_device()  # Turn the light on

        if isinstance(device, SmartLight) and len(device.device_id) > 12:  # Assuming default IDs are shorter
            return

    def create_add_device_button(self):
        add_device_button = tk.Button(self.master, text="Add Device", command=self.prompt_add_device)
        add_device_button.pack(side=tk.BOTTOM, pady=10)

    def prompt_add_device(self):
        """
        Open a window to prompt the user for device type and ID to add a new device.
        """
        add_device_window = tk.Toplevel(self.master)

        device_type_label = tk.Label(add_device_window, text="Select Device Type:")
        device_type_label.pack()

        device_types = ["SmartLight", "SecurityCamera", "Thermostat"]
        selected_device = tk.StringVar(add_device_window)
        selected_device.set(device_types[0])

        device_type_dropdown = tk.OptionMenu(add_device_window, selected_device, *device_types)
        device_type_dropdown.pack()

        device_id_label = tk.Label(add_device_window, text="Device ID:")
        device_id_label.pack()

        device_id_entry = tk.Entry(add_device_window)
        device_id_entry.pack()

        add_button = tk.Button(add_device_window, text="Add", command=lambda: self.add_from_input(
            selected_device.get(), device_id_entry.get(), add_device_window))
        add_button.pack()

    def add_from_input(self, device_type, device_id, window):
        self.add_device(device_type, device_id)
        window.destroy()

def main():
    """
    Main function to initialize the GUI and start the application.
    """
    root = tk.Tk()
    gui = SmartDeviceGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()