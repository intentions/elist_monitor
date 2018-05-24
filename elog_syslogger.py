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

    #converts the bytes to a string
    stringelog = rawelog.decode("utf-8")

    #split the string up by lines so each line can be checked individually
    listelog = stringelog.split('\n')

    #grabs the date for yesterday
    rawyesterday = datetime.date.today()-datetime.timedelta(1)
    yesterday = rawyesterday.strftime("%m/%d/%Y")

    for elog in listelog:



def write_log():
    """
    writes the elog to the system logger
    """
    return 0


if __name__ == "__main__":
    print("placeholder")

