#!/usr/bin/env python3
import os    
import shutil
import sys
from datetime import datetime  # import datetime, add timestamp


def check_disk_health(disk):
    #check SMART health status of a disk, will display the appropriate message depending if PASSED, FAILED or status UNKNOWN
    # will run smartctl -h, reads the output
    # prints health status output
    try:
        print(f"Checking disk health for {disk}...")
        result = os.popen(f"sudo smartctl -H {disk}").read()
        if "PASSED" in result:
            health_status = "Disk Health Status: PASSED\n"
        elif "FAILED" in result:
            health_status = "Disk Health Status: FAILED\n"
        else:
            health_status = "Disk Health Status: UNKNOWN\n"
        print(health_status)
        print(result)
        return health_status + result
    except Exception as e:
        error_message = f"Error checking disk health: {e}\n"
        print(error_message)
        return error_message


def check_disk_usage(partition):

    #check the disk usage of given partition
   # uses shutil.disk_usage to get the free space information
   # aftewards, signified by values such as 1024, it will convert the values from bytes, to gigabytes
   # will print the disk usage result
    try:
        # Acquires disk usage statistics
        usage = shutil.disk_usage(partition)
        result = (
            f"Disk Usage for {partition}:\n"
            f"  Total: {usage.total // (1024**3)} GB\n"
            f"  Used: {usage.used // (1024**3)} GB\n"
            f"  Free: {usage.free // (1024**3)} GB\n"
            f"  Usage Percentage: {usage.used / usage.total * 100:.2f}%\n"
        )
        print(result)
        return result
    except FileNotFoundError:
        error_message = f"Error: Partition '{partition}' not found.\n"
        print(error_message)
        return error_message
    except Exception as e:
        error_message = f"An error occurred while checking disk usage: {e}\n"
        print(error_message)
        return error_message



def save_to_log(content):

    # Saves content and appends output to a file for logging purposes
    # creates file named 'disk_monitor_log.txt'
    # adds the current date and time to the file entry.
    # appends the content and closes the file.
    
    try:
        with open("disk_monitor_log.txt", "a") as log_file:  # opens file (append mode).
            log_file.write(f"\n--- Log Entry at {datetime.now()} ---\n")  # adds timestamp.
            log_file.write(content)  # writes content to the file.
            log_file.write("\n")  # adds newline.
        print("Results saved to 'disk_monitor_log.txt'")
    except Exception as e:
        print(f"Error saving to log file: {e}")


def main():

    if len(sys.argv) < 3:  # check if arguments are passed, if not, print debug msg and exit
        print("Usage: monitor.py <partition> <disk>")
        print("Example: sudo ./monitor.py / /dev/sda")
        sys.exit(1)

    partition = sys.argv[1]  # 1st arg will be the partition ex. (/)
    disk = sys.argv[2]  # second arg is the disk ex. (/dev/sda).

    print("\n--- Hard Drive Usage Monitoring ---")
    usage_result = check_disk_usage(partition)  # call disk usage 

    print("\n--- Hard Drive Health Check ---")
    health_result = check_disk_health(disk)  # call disk health

    # creating file with logging results
    combined_result = f"{usage_result}\n{health_result}"
    save_to_log(combined_result)  

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
