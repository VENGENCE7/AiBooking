# core/schemas/__init__.py

# Import important classes and objects to make them available at the package level
from .llm import tagging_chain,chain,user_flight_details

# Define package-level constants or configurations
API_VERSION = "1.0"
DEBUG_MODE = False

# Perform any package-level initialization if needed
import logging

# Configure package-level logging
logging.basicConfig(level=logging.INFO)

# You can add more package-level configurations or initialization code as needed.
