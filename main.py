import tkinter as tk
import tkinter.ttk as ttk
from SmartDevice import SmartDevice
from SecurityCamera import SecurityCamera
from SmartLight import SmartLight
from Thermostat import Thermostat
from SmartDeviceGUI import SmartDeviceGUI
from AutomationSystem import AutomationSystem  # Assuming AutomationSystem is in a separate file

def main():
    """
    Main function to initialize the GUI, automation system, link devices, and run the simulation loop.
    """
    # Initialize GUI
    root = tk.Tk()
    gui = SmartDeviceGUI(root)

    # Initialize automation system
    automation_system = AutomationSystem()

    # Link discovered devices between GUI and automation system
    for device in gui.devices:
        automation_system.discover_device(device)

    # Run simulation loop in automation system
    automation_system.run_simulation_loop(5)  # Run the simulation loop with an interval of 5 seconds

    # Start GUI
    root.mainloop()

if __name__ == "__main__":
    main()
