import logging
import logging.config
from app.core.config import Settings

def setup_logging():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(ascitime)s [%(levelname)s] %(name)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": Settings.LOG_LEVEL
            },
        },
        "root": {
            "handlers": ["console"],
            "level": Settings.LOG_LEVEL
        },
        "loggers": {
            "app": {
                "level": Settings.LOG_LEVEL,
                "handlers": ["console"],
                "propagate": False
            },
            "uvicorn": {
                "level": Settings.LOG_LEVEL,
                "handlers": ["console"],
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(config)

logger = logging.getLogger("app")

