from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.bot_token()
        self.getclicktoken()
        self.db_bot()

    def bot_token(self):
        self.token = os.getenv('TOKEN')

    def getclicktoken(self):
        self.click_token = os.getenv("CLICK_TOKEN", "")

    def db_bot(self):
        self.host = os.getenv("HOST", "localhost")
        self.user = os.getenv("USER", "postgres")
        self.database = os.getenv("DATABASE", "online_market")
        self.password = os.getenv("PASSWORD", '123456')