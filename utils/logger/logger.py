import logging


class CustomLogger(logging.Logger):

    def __init__(self, name: str):
        super().__init__(name)
        self.setLevel(logging.DEBUG)
        self.create_info_handler()

    def create_info_handler(self):
        # Create a handler to send the log output to the console
        info_handler = logging.StreamHandler()
        info_handler.setLevel(logging.DEBUG)

        # Create a formatter and set it on the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        info_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.addHandler(info_handler)


# Create a logger
logger = CustomLogger('Algorithm logger')
