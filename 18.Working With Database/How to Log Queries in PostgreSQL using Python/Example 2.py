import logging

# The getLogger() returns a logger with the specified name.
# If name is None, it returns the root logger.
logger = logging.getLogger('dev')

# Level is set
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message via setLevel')
logger.error('This is an error message via setLevel')
logger.critical('This is a critical message via setLevel')
