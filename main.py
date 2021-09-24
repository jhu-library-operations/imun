import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.warning("Watch out!")
logging.info("Told ya so")
