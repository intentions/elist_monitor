"""
elog_syslogger
written by: Kurt J. Strosahl (strosahl@jlab.org)

reads the elog using ipmitool sel elog and writes the results into the syslogger for transfer to graylog
"""

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

def write_log():
    """
    writes the elog to the system logger
    """

def wipe_elog():
    """
    clears the elog after writting it so that subsequent runs don't pick up the same errors
    """


if __name__ == "__main__":


