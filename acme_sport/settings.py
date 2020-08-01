import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
SCOREBOARD_URL='https://delivery.chalk247.com/scoreboard'
TEAMRANKING_URL='https://delivery.chalk247.com/team_rankings'