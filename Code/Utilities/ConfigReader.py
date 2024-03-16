import json

class ConfigReader:
    def __init__(self) -> None:
        with open("Config.json", "r") as config_file:
            config = json.load(config_file)
        
        self.config = config