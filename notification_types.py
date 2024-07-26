from bot_functions import BotFunctions
from db_helper import DbHelper

class NotificationTypes(BotFunctions):

    def __init__(self) -> None:
        super().__init__()
        self.db = DbHelper("FootballMatches")


    def daily(self):
        match_datas = self.db.get_all_data("MatchCards")
        counter = 0

        for document in match_datas:
            if counter < 1:
                counter = counter + 1
                telegram_header_message = "GÜNÜN MAÇLARI"
                self.daily_bot(telegram_header_message)
            
            #ucl bot message sender
            if document["league"] == "UEFA Champions League":
                message = f"🔴 | {document["team1"]} - {document["team2"]}  /  {document["time"]}"
                self.ucl_bot(message)

            #uel bot message sender
            if document["league"] == "UEFA Europa League":
                message = f"🔴 | {document["team1"]} - {document["team2"]}  /  {document["time"]}"
                self.uel_bot(message)

            #ucol bot message sender
            if document["league"] == "UEFA Europa Conference League":
                message = f"🔴 | {document["team1"]} - {document["team2"]}  /  {document["time"]}"
                self.ucol_bot(message)

            #pl bot message sender
            if document["league"] == "Premier League":
                message = f"🔴 | {document["team1"]} - {document["team2"]}  /  {document["time"]}"
                self.pl_bot(message)

            #sl bot message sender
            if document["league"] == "Süper Lig":
                message = f"🔴 | {document["team1"]} - {document["team2"]}  /  {document["time"]}"
                self.sl_bot(message)


NotificationTypes().daily()