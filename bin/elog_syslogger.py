"""
elog_syslogger
written by: Kurt J. Strosahl (strosahl@jlab.org)

reads the elog using ipmitool sel elog and writes the results into the syslogger for transfer to graylog
"""

import datetime
import subprocess
import logging
import logging.handlers

def read_elog():
    """
    runs ipmitool sel elog to get the list of errors
    """

    p = subprocess.Popen(['/usr/bin/ipmitool', 'sel', 'elist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    if stderr:
        raise Exception(stderr)

    return stdout

def parse_elog(rawelog):
    """
    Takes in the raw elog data and trims it so that only the entries from today carry on to be written to the syslog
    """
    #converts the raw bytes from ipmitool into a list 
    listelog = (rawelog.decode("utf-8")).split('\n')

    #grabs the date for yesterday
    yesterday = (datetime.date.today()-datetime.timedelta(1)).strftime("%m/%d/%Y")

    dailymessages = []

    for elog in listelog:
        if yesterday in elog:
            dailymessages.append(elog)

    return dailymessages


def write_log():
    """
    writes the elog to the system logger
    """
    return 0


if __name__ == "__main__":
    print("placeholder")

