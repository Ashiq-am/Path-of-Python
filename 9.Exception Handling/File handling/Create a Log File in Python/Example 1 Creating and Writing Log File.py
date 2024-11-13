import logging

logging.basicConfig(filename="gfg-log.log", filemode="w",
					format="%(name)s → %(levelname)s: %(message)s")

logging.warning("warning")

logger = logging.getLogger(__name__)
FileOutputHandler = logging.FileHandler('logs.log')

logger.addHandler(FileOutputHandler)


logger.warning("test.")
