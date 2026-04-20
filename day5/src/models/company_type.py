#crate company type enum

from enum import Enum
class CompanyType(str, Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    NON_PROFIT = "Non-Profit"
    GOVERNMENT = "Government"