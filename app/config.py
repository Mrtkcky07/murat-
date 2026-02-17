import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_FOOTBALL_KEY")
BASE_URL=os.getenv("BASE_URL")
WEATHER_KEY=os.getenv("WEATHER_API_KEY")

HEADERS={"x-rapidapi-key":API_KEY}