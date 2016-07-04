# Save Mikrotik usage

Scripts in this repo can be used to retrieve usage from a Mikrotik device.
The aim initially will be to pull usage on intervals using the web access accounting interface,
but in the future might be expanded to rather use other methods, as this method is constrained
by the pair threshold set on the Mikrotik device (which means we might miss usage if the threshold
is hit between poll periods).

# Required environment variables

The following environment variables are required:

- `DATABASE_IP`: Ip of the database to save the usage data to.
- `DATABASE_NAME`: Name of the database to save the usage data to.
- `DATABASE_USERNAME`: Username to use when connecting to the database.
- `DATABASE_PASSWORD`: Password to use when connecting to the database.
- `MIKROTIK_IP`: Ip address of your mikrotik device.
- `PYTHON_SCRIPT_DIR`: Directory in which the python scripts are located - if scripts are located in /home/user/scripts/scriptname.py, set this as `/home/user/scripts`

# Scripts

These python scripts performs various tasks and are called by Jenkins jobs on a schedule.
The following scripts are included:

- `save_web_access_usage.py`: Uses the web-access reporting on a Mikrotik router to pull usage information based on ip addresses and saves this to a MySQL database.

# Jenkins

The configuration files for Jenkins jobs are included which you can use to execute the scripts on a schedule.
The following jobs are included:

- `collect_usage` - Used to execute the web-access based usage collection script.
