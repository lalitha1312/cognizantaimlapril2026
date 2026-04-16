import sys
import os

# add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from conf.logger_conf import setup_logger

logger = setup_logger()

"""
Entry point for the apllication this module initinalizes the application and starts the main loop
"""

def run():
    """
    test logger
    """
    logger.info("app running successfully")

"""
handle entry point of the application
"""

if __name__ == "__main__":
    run()