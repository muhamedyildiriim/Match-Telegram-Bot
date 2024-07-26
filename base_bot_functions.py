from config.config import Config
import requests
import os

class BaseBotFunctions:
    def __init__(self):
        # Get the current working directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create the full path for the config.ini file
        config_path = os.path.join(current_dir, 'config', 'config.ini')

        # Retrieve the required bot information using the Config class
        self.base_url = Config(config_path).get_section("TELEGRAM")["base_url"]
        self.group_id = Config(config_path).get_section("TELEGRAM")["group_id"]

    def send_message(self, token, message: str) -> None:
        url = f"{self.base_url}/bot{token}/sendMessage?chat_id={self.group_id}&text={message}"
        requests.get(url).json()
