"""
karapace - constants

Copyright (c) 2020 Aiven Ltd
See LICENSE for details
"""

# This is a log level that has higher value than any default level.
# Used for logging status messages that need to be visible always
LOGGING_STATUS_LEVEL = 100
LOGGING_STATUS_LEVEL_NAME = "STATUS"

SCHEMA_TOPIC_NUM_PARTITIONS = 1
API_VERSION_AUTO_TIMEOUT_MS = 30000
TOPIC_CREATION_TIMEOUT_MS = 20000
DEFAULT_SCHEMA_TOPIC = "_schemas"

SECOND = 1000
MINUTE = 60 * SECOND
