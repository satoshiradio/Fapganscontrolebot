class BotConfig:
    TOKEN = "1234567890:ABCDEFGH123_IJKLMNOPQRSTUVWXYZ456789"
    FAPGANS_STICKER_ID = "AgADXgADUomRIw"


class DbConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class PriceServiceConfig:
    SERVICE_URI = "https://api.coindesk.com/v1/bpi/currentprice.json"
    POLL_INTERVAL_IN_SECONDS = 60
