# core/schemas/__init__.py

# Import important classes and objects to make them available at the package level
from .tequilaSchema import GetFlightInPeriodCheckInput, RequestBody

# Perform any package-level initialization if needed
import logging

# Configure package-level logging
logging.basicConfig(level=logging.INFO)

# You can add more package-level configurations or initialization code as needed.
