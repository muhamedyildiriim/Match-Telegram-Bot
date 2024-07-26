from notification_types import NotificationTypes
from scraper import Scraper
from db_helper import DbHelper
import schedule
import time

class Scheduler:
    def __init__(self):

        self.nt = NotificationTypes()
        self.scraper = Scraper()
        self.db = DbHelper("FootballMatches")

        self.daily_checks()
        self.pooling()


    def pooling(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


    #self.job_func = functools.partial(job_func, *args, **kwargs)
    #                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #TypeError: the first argument must be callable

    ###due to error, we use clear collection method of db class in a function###
    def db_functions(self):
        self.db.clear_collection("MatchCards")
        

    def daily_checks(self):
        schedule.every().day.at("13:43", "Europe/Istanbul").do(self.nt.daily)

        schedule.every().day.at("13:41", "Europe/Istanbul").do(self.db_functions)

        schedule.every().day.at("13:42", "Europe/Istanbul").do(self.scraper.pl_scraper)
        schedule.every().day.at("13:42", "Europe/Istanbul").do(self.scraper.sl_scraper)
        schedule.every().day.at("13:42", "Europe/Istanbul").do(self.scraper.ucl_scraper)
        schedule.every().day.at("13:42", "Europe/Istanbul").do(self.scraper.uel_scraper)
        schedule.every().day.at("13:42", "Europe/Istanbul").do(self.scraper.ucol_scraper)