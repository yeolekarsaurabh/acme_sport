import json
from acme_sport.main import mapper
from acme_sport.Scorecard import ScoreCard

def test_mapper_creates_instances():
    """
    This is test function which checks if the data is mapped as expected.
    """
    with open('tests/data/expected_leaderboard.json') as file:
        expected_leaderboard = json.load(file)

    with open('tests/data/expected_scoreboard.json') as file:
        expected_scoreboard = json.load(file)
    result = mapper(expected_scoreboard,expected_leaderboard)
    assert all([type(record) == ScoreCard for record in result])
