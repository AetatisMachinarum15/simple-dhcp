# file:			config.py
# description:	Manages simple-dhcp configuration data.
# author:		AetatisMachinarum15
# date:			08-15-2026
#
import os
import shutil
import xml.etree.ElementTree as ET

from common import LOGGER

class Configuration:
	"""
		Singleton, static, class which manages the context of the underlying
		XML configuration file which provides user-defined data to simple-dhcp.
	"""
	TEMPLATE_FILE		= os.path.join(__file__, 'template.xml')
	CONFIG_FILE			= os.path.join('/etc', 'simple-dhcp', 'config.xml')

	@classmethod
	def setup(cls):
		"""
			Loads XML configuration from disk and prepares the *Configuration*
			class in generate to serve data.

			Returns *True* if successful, *False* otherwise.
		"""
		if os.path.exists(cls.CONFIG_FILE) is False:
			if os.path.exists(cls.TEMPLATE_FILE) is False:
				LOGGER.critical('Unable to access config or template file.')
				return False
			os.makedirs(os.path.dirname(cls.CONFIG_FILE))
			shutil.copy(cls.TEMPLATE_FILE, cls.CONFIG_FILE)
		# Load configuration file into internal members
		try:
			cls.tree = ET.parse(cls.CONFIG_FILE)
		except Exception as e:
			LOGGER.critical('Exception occurred while loading configuration.')
			LOGGER.error(f'\t{e}')
			return False
		cls.root = cls.tree.getroot()
		return True

	def get(cls, *args, first_only = False):
		"""
			Passthrough to Element.findall (or Element.find,
			if first_only is specified).
		"""
		if first_only: return cls.root.find(*args)
		return cls.root.findall(*args)
