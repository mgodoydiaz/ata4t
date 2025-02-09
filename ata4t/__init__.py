"""ATA4T: Automated Technical Analysis Trading Tool"""
# Add imports here

import os
from ata4t.tools import connection_tools, file_tools, xAPIConnector

ATA4T_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions