from base_bot_functions import BaseBotFunctions
from config.config import Config

class BotFunctions(BaseBotFunctions):

    def __init__(self) -> None:
        super().__init__()


    def ucl_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["ucl_token"]
        self.send_message(token, message)

    def uel_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["uel_token"]
        self.send_message(token, message)
    
    def ucol_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["ucol_token"]
        self.send_message(token, message)

    def pl_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["pl_token"]
        self.send_message(token, message)

    def sl_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["sl_token"]
        self.send_message(token, message)

    def daily_bot(self, message):
        token = Config("./config/config.ini").get_section("TELEGRAM")["daily_programmer_token"]
        self.send_message(token, message)