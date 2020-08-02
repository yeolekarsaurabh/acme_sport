import json
import requests
import collections

from pprint import pprint
from .settings import SECRET_KEY,SCOREBOARD_URL,TEAMRANKING_URL
from .Scorecard import ScoreCard
from .APIHelper import APIHelper


def mapper(scoreboard, team_rankings:list):
    """ 
    This function creates a mapper which searchs ranks from teamranking
    and takes scoreboard record and created ScoreCard instance
    """
    acc = []
    for score in scoreboard:
        home_ranking = list(filter(lambda x: x['team_id'] == score['home_team_id'], team_rankings))
        away_ranking = list(filter(lambda x: x['team_id'] == score['away_team_id'], team_rankings))
        if len(home_ranking) > 0 and len(away_ranking) > 0:
            instance = ScoreCard(score, home_ranking[0], away_ranking[0])
            acc.append(instance)
    return acc


def main(dateFrom, dateTo, league):
    error, scoreboard, tr_raw = APIHelper.getScoreAndRank(dateFrom=dateFrom, dateTo=dateTo, league=league)
    if error:
        return error
    all_the_instances = mapper(scoreboard, tr_raw)
    result = []
    for instance in all_the_instances:
        pprint(json.dumps(instance.__dict__))
        result.append(instance.__dict__)
    return result

if __name__ == "__main__":
    main('2020-01-12', '2020-01-19', 'NFL')



