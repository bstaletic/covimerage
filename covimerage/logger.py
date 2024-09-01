import logging
import sys

logger = logging.getLogger('covimerage')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stderr))
