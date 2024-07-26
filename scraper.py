from base_scraper import BaseScraper
from config.config import Config

class Scraper:

    def __init__(self):
        pass

    def ucl_scraper(self):
        scrape_link = Config("./config/config.ini").get_section("SCRAPER")["ucl"]
        BaseScraper(scrape_link)
    
    def uel_scraper(self):
        scrape_link = Config("./config/config.ini").get_section("SCRAPER")["uel"]
        BaseScraper(scrape_link)

    def ucol_scraper(self):
        scrape_link = Config("./config/config.ini").get_section("SCRAPER")["ucol"]
        BaseScraper(scrape_link)

    def pl_scraper(self):
        scrape_link = Config("./config/config.ini").get_section("SCRAPER")["pl"]
        BaseScraper(scrape_link)

    def sl_scraper(self):
        scrape_link = Config("./config/config.ini").get_section("SCRAPER")["sl"]
        BaseScraper(scrape_link)


Scraper().ucol_scraper()
Scraper().uel_scraper()
Scraper().ucl_scraper
