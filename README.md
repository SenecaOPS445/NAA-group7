# Fall 2024 Assignment 2

Disk usage monitoring and Health Checkup (Report system)

This script will handle 2 tasks.

The first task will be the monitoring of disk usage on a specific partition (represented in %, making use of shutil() ), the end goal for this monitoring system is to give the administrator/user a report system that will log the daily changes in disk usage into a file, which later on can be used as a reference for system monitoring. The report will display the total, used and available space within the specified disk partition, alongside a date for easier archiving.

The second task will be a Health Checkup, making use of the os.popen() function to access the operating system and execute smartctl to get the checkup task done. This specific task will be responsible for identifying disk failures within the system, with the central piece in this part of the script being SMART (Self-Monitoring, Analysis, and Reporting Technology).


Requires sudo permission.
Uses smartctl tool.
Will append result to a file.
Will generate two outputs.
