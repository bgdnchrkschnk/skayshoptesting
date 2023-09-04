from enum import Enum

# Base class for all locator classes
class BaseLocators(Enum):
    def __init__(self, by, locator):
        self.by = by
        self.locator = locator