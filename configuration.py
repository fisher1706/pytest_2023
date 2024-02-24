from dotenv import load_dotenv
import os

SERVICE_URL = 'https://gorest.co.in/public/v1/users'


"""
data to connect to postgresql -> start postgresql before
for connect to DB -> use .env file + class "SettingsLoadDotEnv"
"CONNECTION_ROW" -> only as example
"""
CONNECTION_ROW = "postgresql://postgres:admin@localhost:5432/twoe_hd_kino"


class SettingsLoadDotEnv:
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_NAME = os.getenv("DB_NAME")

    DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


if __name__ == '__main__':
    sl = SettingsLoadDotEnv()
    print(sl.DB_URL)
