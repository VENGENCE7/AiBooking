# core/schemas/__init__.py

# Import important classes and objects to make them available at the package level
from .promptTemplate import promptTemplate
from .requiredBookingDetails import requiredBookingDetails
# Perform any package-level initialization if needed
import logging

# Configure package-level logging
logging.basicConfig(level=logging.INFO)

# You can add more package-level configurations or initialization code as needed.
