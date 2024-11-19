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
            


