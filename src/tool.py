# file:			tool.py
# description:	Entry point of simple-dhcp.
# author:		AetatisMachinarum15
# date:			08-15-2026
#
import sys
import os
import logging

from common import LOGGER
from config import Configuration

def main():
	""" Program entry. Returns program result code to OS. """
	if Configuration.setup() is False: return os.EX_CONFIG
	if (log_lvl := Configuration.get('./log', first_only = True)) is None:
		LOGGER.setlevel(logging.WARNING)
	match log_lvl:
		case 0: LOGGER.setlevel(logging.ERROR)
		case 1: LOGGER.setlevel(logging.WARNING)
		case 2: LOGGER.setlevel(logging.INFO)
		case 3: LOGGER.setlevel(logging.DEBUG)
		case _:
			LOGGER.error(f'Unknown log-level: {log_lvl}')
			return os.EX_CONFIG

	return os.EX_OK

if __name__ == "__main__":
	sys.exit(main())
