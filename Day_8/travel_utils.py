import re
from datetime import datetime as dt

def validate_destination(destination):
    """Validates that the destination only contains letters and spaces."""
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, destination))

def check_overlap(existing_itineraries, new_start, new_end):
    """Checks if the new itinerary overlaps with existing ones."""
    for itinerary in existing_itineraries:
        start, end = itinerary[2], itinerary[3]
        if (start <= new_start <= end) or (start <= new_end <= end) or (new_start <= start and new_end >= end):
            return True
    return False
