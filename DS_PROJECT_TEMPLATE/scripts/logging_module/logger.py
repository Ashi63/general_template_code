import logging
from pathlib import Path
from dataclasses import dataclass

# get the parent directory of the logging folder
@dataclass
class LoggingConfig:
    parent_folder = Path().resolve().parent.parent
    log_folder_path = parent_folder/'logs'
    log_file_path = log_folder_path/'project_log.log'

class ProjectLogger:
    def __init__(self):
        self.logging_paths_config = LoggingConfig() 
        self.log_file_path = self.logging_paths_config.log_file_path
        self.logger = self._create_logger()
        
    def _create_logger(self):
        logger = logging.getLogger("ProjectLogger")
        logger.setLevel(logging.DEBUG)
        
        # Create a file handler that logs all levels of messages to a file.
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.DEBUG)
        
        # Create a stream handler that logs only INFO level  and above messages to console.
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        
        # Create a formatter to specify the format of log messages.
        formatter =  logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s ', datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        
        
        return logger
    
    def debug(self,message):
        self.logger.debug(message)
        
    def info(self, message):
        self.logger.info(message)
        
    def warning(self,message):
        self.logger.warning(message)
        
    def error(self,message):
        self.logger.error(message)
        
    def critical(self,message):
        self.logger.critical(message)


@dataclass
class LoggingConfig:
    parent_folder = Path().resolve().parent.parent
    log_folder_path = parent_folder/'logs'
    log_file_path = log_folder_path/'exceptions.log'

class ExceptionHandler:
    def __init__(self, log_file_path="exceptions.log"):
        self.logging_paths_config = LoggingConfig() 
        self.log_file_path = self.logging_paths_config.log_file_path
        self.logger = self._create_logger()

    def _create_logger(self):
        logger = logging.getLogger("ExceptionHandler")
        logger.setLevel(logging.ERROR)

        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def handle_exception(self, message=None, exc_info=False):
        if message:
            self.logger.error(message, exc_info=exc_info)
        else:
            self.logger.exception("An exception occurred:")


if __name__=='__main__':
    logger = ProjectLogger()
    logger.debug("This is a debug message") 
    logger.info("This is a info message") 
    logger.warning("This is a warning message")
    logger.error("This is a error message")
    logger.critical("This is a critical message")

 
    # Usage example:

    # Initialize the ExceptionHandler class
    exception_handler = ExceptionHandler()

    try:
        # Some code that may raise an exception
        result = 10 / 0
    except Exception as e:
        # Handle the exception and log it
        exception_handler.handle_exception("Error occurred while performing the division.", exc_info=True)
