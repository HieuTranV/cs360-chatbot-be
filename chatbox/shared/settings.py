import logging
import logging.config
from chatbox.config import settings

logging.config.fileConfig('./chatbox/log.conf')


log = logging.getLogger("[CHATBOX]")