import logging
import logging.config
from app.core.config import settings

def setup_logging():
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": settings.LOG_LEVEL
            },
        },
        "root": {
            "handlers": ["console"],
            "level": settings.LOG_LEVEL
        },
        "loggers": {
            "app": {
                "level": settings.LOG_LEVEL,
                "handlers": ["console"],
                "propagate": False
            },
            "uvicorn": {
                "level": settings.LOG_LEVEL,
                "handlers": ["console"],
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(config)

logger = logging.getLogger("app")

