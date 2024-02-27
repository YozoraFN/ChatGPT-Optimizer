import subprocess
import os
import platform

def update_drivers():
    try:
        if platform.system() == "Windows":
            subprocess.run(["C:\\Path\\To\\DriverUpdater.exe", "/silent", "/autoinstall"], check=True)
        elif platform.system() == "Linux":
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "upgrade", "-y"])
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating drivers: {e}")

def disable_startup_programs():
    try:
        if platform.system() == "Windows":
            subprocess.run(["C:\\Path\\To\\StartupManager.exe", "/disable"], check=True)
        elif platform.system() == "Linux":
            print("Linux: Disabling startup programs not implemented.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling startup programs: {e}")

def set_highest_performance_power_plan():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(["powercfg", "/query", "SCHEME_CURRENT", "SUB_SLEEP", "STANDBYIDLE"], universal_newlines=True)
            highest_performance_plan_line = [line for line in output.split('\n') if 'Ultimate Performance' in line][0]
            plan_guid = highest_performance_plan_line.split()[3]

            subprocess.run(["powercfg", "/setactive", plan_guid], check=True)
            print(f"Power plan set to highest performance: {plan_guid}")
        else:
            print("Setting power plan not supported on this platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting power plan: {e}")

def clean_temp_files():
    try:
        if platform.system() == "Windows":
            subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
        elif platform.system() == "Linux":
            subprocess.run(["sudo", "apt", "autoremove", "-y"])
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning temp files: {e}")

def disable_mouse_acceleration():
    try:
        if platform.system() == "Windows":
            subprocess.run(["reg", "add", "HKCU\\Control Panel\\Mouse", "/v", "MouseAccel_Level", "/t", "REG_DWORD", "/d", "0", "/f"], check=True)
        else:
            print("Mouse acceleration disable not supported on this platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling mouse acceleration: {e}")

def adjust_keyboard_repeat_rate():
    try:
        if platform.system() == "Windows":
            subprocess.run(["reg", "add", "HKCU\\Control Panel\\Keyboard", "/v", "KeyboardDelay", "/t", "REG_SZ", "/d", "0", "/f"], check=True)
            subprocess.run(["reg", "add", "HKCU\\Control Panel\\Keyboard", "/v", "KeyboardSpeed", "/t", "REG_SZ", "/d", "31", "/f"], check=True)
        else:
            print("Keyboard repeat rate adjustment not supported on this platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error adjusting keyboard repeat rate: {e}")

def optimize_network_settings():
    # Placeholder for a function to optimize network settings
    print("Optimizing network settings...")

def disable_superfetch():
    try:
        if platform.system() == "Windows":
            subprocess.run(["sc", "config", "SysMain", "start=disabled"], check=True)
        else:
            print("Superfetch disable not supported on this platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling Superfetch: {e}")

def adjust_graphics_settings():
    # Placeholder for a function to adjust graphics settings
    print("Adjusting graphics settings...")

def disable_cortana():
    try:
        if platform.system() == "Windows":
            subprocess.run(["reg", "add", "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search", "/v", "AllowCortana", "/t", "REG_DWORD", "/d", "0", "/f"], check=True)
        else:
            print("Cortana disable not supported on this platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling Cortana: {e}")

def main():
    print("PC Optimization Script")

    print("\nUpdating drivers...")
    update_drivers()

    print("\nDisabling startup programs...")
    disable_startup_programs()

    print("\nSetting power plan to highest performance...")
    set_highest_performance_power_plan()

    print("\nCleaning temporary files...")
    clean_temp_files()

    print("\nDisabling mouse acceleration...")
    disable_mouse_acceleration()

    print("\nAdjusting keyboard repeat rate...")
    adjust_keyboard_repeat_rate()

    print("\nOptimizing network settings...")
    optimize_network_settings()

    print("\nDisabling Superfetch...")
    disable_superfetch()

    print("\nAdjusting graphics settings...")
    adjust_graphics_settings()

    print("\nDisabling Cortana...")
    disable_cortana()

    # Add more function calls here...

    print("\nOptimization complete.")

if __name__ == "__main__":
    main()
