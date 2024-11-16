def check_disk_health(disk):
    """Responsible for health checkup of the disk (opearting system), with human readable output."""
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