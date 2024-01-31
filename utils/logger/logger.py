import logging

# Create a logger
logger = logging.getLogger('algorithm_logger')
logger.setLevel(logging.INFO)

# Create a handler to send the log output to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it on the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)
