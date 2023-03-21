import logging
import logging.config

log_cia = "./log.log"

logging.config.fileConfig(fname="logging.conf", disable_existing_loggers=False, defaults={ 'logfilename' : log_cia } )

# Get the logger specified in the file
logger = logging.getLogger("sLogger")


logger.debug("TEST LOG")