from configparser import ConfigParser

class Config:

    def __init__(self, config_file="config.ini"):
        config = ConfigParser()
        config.read(config_file)
        bot = config["Bot"]
        self.token = bot["token"]