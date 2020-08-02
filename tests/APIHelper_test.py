import json
from acme_sport.APIHelper import APIHelper

def test___transformScoreBoard():
    """
    This is a unit test function that checks for the transform data is same as expected.
    """
    with open('tests/data/data_scoreboard.json') as file:
        raw_data = json.load(file)
    actual_data = APIHelper._APIHelper__transformScoreBoard(raw_data)
    with open('tests/data/expected_scoreboard.json') as file2:
        expected_data = json.load(file2)
    assert all([actual_r == expected_r for actual_r, expected_r in zip(actual_data, expected_data)])

def test___transformRank():
    """
    This is a unit test function that checks for the transform data is same as expected.
    """
    with open('tests/data/data_leaderboard.json') as file:
        raw_data = json.load(file)
    actual_data = APIHelper._APIHelper__transformRank(raw_data)
    with open('tests/data/expected_leaderboard.json') as file2:
        expected_data = json.load(file2)
    assert all([actual_r == expected_r for actual_r, expected_r in zip(actual_data, expected_data)])
