"""
Logger module
# """
# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)
import logging
from rich.logging import RichHandler

# FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FORMAT = '%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

logger = logging.getLogger(__name__)
