import schedule
import time
from src.scraper import SocGenScraper
from utils.email_sender import EmailEngine
from utils.database import DatabaseHandler
from utils.processor import pandas_converter

def run_work():
    sg = SocGenScraper()
    sg_data = sg.get_processed_data()
    sg_df = pandas_converter(sg_data)
    database_handler = DatabaseHandler(sg_df)
    new_sg_df = database_handler.run()
    ee = EmailEngine('eloidieme@gmail.com', new_sg_df)
    ee.send_email()

#schedule.every().day.at("02:12").do(run_work)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
    
if __name__ == '__main__':
    run_work()