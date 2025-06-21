
import psycopg2
from config import Config

cfg = Config()


class Computer_db:
    def __init__(self):
        self.connect = psycopg2.connect(
            host=cfg.host,
            user=cfg.user,
            password=cfg.password,
            database=cfg.database
        )
        self.cursor = self.connect.cursor()
        self.create_table()
        print("Date base yaraldi")

    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS computer_db(
                id SERIAL PRIMARY KEY,
                brand_name VARCHAR(255),
                product_url TEXT,
                product_image VARCHAR(255),
                product_price VARCHAR(40),
                configurations TEXT UNIQUE
            )""")
        self.connect.commit()

    def insert_data(self, *args):
        self.create_table()
        self.cursor.execute(f"""INSERT INTO computer_db (brand_name, product_url, product_image, product_price, configurations)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT(configurations) DO NOTHING""", args)
        self.connect.commit()

    def select_data(self):
        self.cursor.execute(f"""
            SELECT brand_name, product_url, product_image, product_price, configurations
            FROM computer_db
        """)
        return self.cursor.fetchall()

Computer_db()
