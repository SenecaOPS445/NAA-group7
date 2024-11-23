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
def check_disk_usage(disk):
    "Check the usage of the disk"
    try:
        print(f"Checking disk usage for {disk}...")
        usage = shutil.disk_usage(disk)
        print(f"Total: {usage.total // (1024 ** 3)} GB")
        print(f"Used: {usage.used // (1024 ** 3)} GB")
        print(f"Free: {usage.free // (1024 ** 3)} GB\n")
    except Exception as e:
        print(f"Error checking for disk usage: {e}")
        
def main():
    if len(sys.argv) < 3:
        print("Usage: monitor.py <partition> <disk>")
        print("Example: sudo ./monitor.py / /dev/sda")
        sys.exit(1)

    # Command-line arguments
    partition = sys.argv[1]  # e.g., "/"
    disk = sys.argv[2]       # e.g., "/dev/sda"

    print("\n--- Hard Drive Usage Monitoring ---")
    check_disk_usage(partition)

    print("\n--- Hard Drive Health Check ---")
    check_disk_health(disk)

if __name__ == "__main__":
    main()
