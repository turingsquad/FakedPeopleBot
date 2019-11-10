from configparser import ConfigParser
import os


class Config:

    def __init__(self, config_file="config/config.ini"):
        if not os.path.exists(config_file):
            raise FileExistsError("Could not locate path for config " + config_file)
        config = ConfigParser()
        config.read(config_file)
        bot = config["Bot"]
        self.token = bot["token"]
