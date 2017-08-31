#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from xoxzo.api import XoxzoApi


# standard nagios return codes
NAGIOS_OK = 0
NAGIOS_WARN = 1
NAGIOS_CRITICAL = 2
NAGIOS_UNKNOWN = 3


class WarningException(Exception):
    pass


class CriticalException(Exception):
    pass


class UnknownException(Exception):
    pass


class Plugin(object):

    def __init__(self):
        """
        Initialize all variables here
        """

    def start(self):
        """
        Start your check/monitoring here
        """
        return ""


def main():
    xoxzo = XoxzoApi()

    try:
        plugin = Plugin()
        status = plugin.start()
        print "OK: %s" % status
        sys.exit(NAGIOS_OK)
    except WarningException as e:
        print "WARNING: %s" % str(e)
        sys.exit(NAGIOS_WARN)
    except CriticalException as e:
        print "CRITICAL: %s" % str(e)
        xoxzo.call("+60123456789", "+60123456789", "DEFCON alert, check end to end is in critical state")
        sys.exit(NAGIOS_CRITICAL)
    except UnknownException as e:
        print "UNKNOWN: %s" % str(e)
        sys.exit(NAGIOS_UNKNOWN)


if __name__ == '__main__':
    main()
