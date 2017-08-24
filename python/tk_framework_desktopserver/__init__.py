# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys

python_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../resources/python"))

distributions_path = os.path.join(python_path, "dist")
if sys.platform == "darwin":
    sys.path.insert(0, os.path.join(distributions_path, "mac"))
elif os.platform == "win32":
    sys.path.insert(0, os.path.join(distributions_path, "windows"))
elif os.platform.startswith("linux"):
    sys.path.insert(0, os.path.join(distributions_path, "linux"))

from .server import Server
from .settings import Settings
from .process_manager import ProcessManager
from .certificates import get_certificate_handler
from .logger import get_logger
from .shotgun import get_shotgun_api
from .errors import MissingCertificateError, PortBusyError, MissingConfigurationFileError, BrowserIntegrationError
