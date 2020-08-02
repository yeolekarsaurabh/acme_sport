import requests
import traceback
from .settings import SECRET_KEY,SCOREBOARD_URL,TEAMRANKING_URL

class APIHelper:
    @staticmethod
    def getScoreAndRank(dateFrom, dateTo, league):
        """
        This function takes three parameters dateFrom, dateTo and league as an input.
        fromDate and toDate are required in YYYY-MM-DD format.
        """
        scoreboard = requests.get(f"{SCOREBOARD_URL}/{league}/{dateFrom}/{dateTo}.json?api_key={SECRET_KEY}")
        team_ranking = requests.get(f"{TEAMRANKING_URL}/{league}.json?api_key={SECRET_KEY}")
        data_scoreboard = scoreboard.json()
        if data_scoreboard.get('results').get('error'):
            return data_scoreboard.get('results').get('error'), None, None
        data_team_ranking = team_ranking.json()
        data_scoreboard = APIHelper.__transformScoreBoard(data_scoreboard)
        data_team_ranking = APIHelper.__transformRank(data_team_ranking)
        return None, data_scoreboard, data_team_ranking

    @staticmethod
    def __transformScoreBoard(jsonResp):
        """
        This functions takes data in json format and gives the values without the headers.
        """
        acc = []
        data = list(jsonResp['results'].values())
        values = list(filter(lambda value: type(value) != list, data))
        for value in values:
            events = value.get('data').values()
            acc.extend(events)
        return acc

    @staticmethod
    def __transformRank(raw):
        """
        This functions takes data in json format and gives the values without the headers.
        """
        return raw.get('results').get('data')
