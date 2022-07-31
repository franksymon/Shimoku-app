import os

import shimoku_api_python as Shimoku
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv("SHIMOKU_TOKEN")
universe_id: str = os.getenv("UNIVERSE_ID")
business_id: str = os.getenv("BUSINESS_ID")


shimoku = Shimoku.Client(
    config={"access_token": access_token},
    universe_id=universe_id,
    environment="production",
)
shimoku.plt.set_business(business_id)
