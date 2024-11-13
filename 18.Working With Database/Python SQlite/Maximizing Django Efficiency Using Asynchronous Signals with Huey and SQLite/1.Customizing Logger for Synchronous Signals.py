#settings.py
import logging

#class CustomFormatter(logging.Formatter):
def format(self, record):
    if not hasattr(record, 'elapsed'):
        record.elapsed = 0.0  # Provide a default value for 'elapsed'
    return super().format(record)

# Update the logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            '()': CustomFormatter,
            'format': '{asctime} {levelname} {name}:{lineno} [{elapsed:.3f}s] - {message}',
            'style': '{',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {  # Suppress django.server logs
            'handlers': ['console'],
            'level': 'ERROR',  # Only show errors and above
            'propagate': False,
        },
        'user': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'PIL': {  # Reduce verbosity for PIL library
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',  # Default root level to WARNING
    },
}
