# core/schemas/__init__.py

# Import important classes and objects to make them available at the package level
from .bookingDetails import booking_details
from .getFlights import get_flight_in_period
from .updateDetails import updateDetails

# Perform any package-level initialization if needed
import logging

# Configure package-level logging
logging.basicConfig(level=logging.INFO)

# You can add more package-level configurations or initialization code as needed.
