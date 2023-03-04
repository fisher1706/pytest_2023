from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not expected"
    WRONG_ELEMENT_COUNT = "Number of items is not equal of expected"

