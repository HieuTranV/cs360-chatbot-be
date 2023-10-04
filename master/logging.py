import logging
import logging.config
from ..chatbox.config import settings

logging.config.fileConfig(settings.log.config_path)
log = logging.getLogger('[COMMON]')
