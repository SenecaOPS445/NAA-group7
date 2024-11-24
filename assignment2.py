def check_disk_health(disk):
    """Responsible for health checkup of the given os, with human readable output."""
        # Use os (popen), and smartctl to access operatin system
    try:
        print(f"Checking disk health for {disk}...")
        result = os.popen(f"sudo smartctl -H {disk}").read()
        if "PASSED" in result:
            print("Disk Health Status: PASSED\n")
        elif "FAILED" in result:
            print("Disk Health Status: FAILED\n")
        else:
            print("Disk Health Status: UNKNOWN\n")
        print(result)
   except Exception as e:
        print(f"Error checking disk health: {e}\n")


def check_disk_usage(partition):
    """Task performs the checkup for the disk usage of chosen partition"""
    try:
        # Block of code, responsible for disk usage stats, (GB based)
        usage = shutil.disk_usage(partition)
        print(f"Disk Usage for {partition}:")               
        print(f"  Total: {usage.total // (1024**3)} GB")
        print(f"  Used: {usage.used // (1024**3)} GB")
        print(f"  Free: {usage.free // (1024**3)} GB")
        print(f"  Usage Percentage: {usage.used / usage.total * 100:.2f}%\n")
    

     # Error checking, File missing or Exception occurance, will print a debug msg.
    except FileNotFoundError:
        print(f"Error: Partition '{partition}' not found.\n")
    
    
    except Exception as e:
        print(f"An error occurred while checking disk usage: {e}\n")
