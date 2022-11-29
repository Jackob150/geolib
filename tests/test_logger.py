log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "": {
            "handlers" : ["console_handler", "file_handler"],
            "level": "DEBUG"
        }
    },
    "handlers": {
        "console_handler": {
            "formatter": "basic_formatter",
            "class": "logging.StreamHandler",
            "level": "INFO",
            "stream": "ext://sys.stdout"
        },
        "file_handler": {
            "formatter": "basic_formatter",
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "mode": "a",
            "filename": "tests/tests_logs/pytest.log",
            "maxBytes": 24 * 1024 * 1024,
            "backupCount": 5
        }
    },
    "formatters":{
        "basic_formatter": {
            "format": "[%(asctime)s][%(levelname)s][%(module)s] %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S"
        }
    }
}
