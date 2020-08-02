##  PROBLEM STATEMENT: ACME Sport ![js-standard-style](https://img.shields.io/badge/Python-brightgreen.svg?style=flat)
ACME Sports, wants to develop a dynamic process to return a list of NFL events in JSON format. It’s dynamic because the process will pull the NFL event data from a remote API that is frequently updated.

## Demo
API is deployed on Heroku (https://acme-sport.herokuapp.com).

### Routes:
- `/getScoreData/{fromDate}/{toDate}/NFL`
    - `fromDate` and `toDate` are required in `YYYY-MM-DD` format.
    - Sample API Call:
    https://acme-sport.herokuapp.com/getScoreData/2020-01-12/2020-01-19/NFL

## Input and Output
### Input
The API endpoint URLs with the NFL data are below. Please assume that the API provides no other functionality other than to return the data in JSON format

Scoreboard: /scoreboard/{league}/{start_date}/{end_date}

https://delivery.chalk247.com/scoreboard/NFL/2020-01-12/2020-01-20.json?api_key=xxyzz

Team Rankings: /team_rankings/{league}

https://delivery.chalk247.com/team_rankings/NFL.json?api_key=xxyzz

### Output
```json
[
    {
        "event_id": "1233827",
        "event_date": "12-01-2020",
        "event_time": "15:05",
        "away_team_id": "42",
        "away_nick_name": "Texans",
        "away_city": "Houston",
        "away_rank": "21",
        "away_rank_points": "-6.00",
        "home_team_id": "63",
        "home_nick_name": "Chiefs",
        "home_city": "Kansas City",
        "home_rank": "2",
        "home_rank_points": "21.20"
    },
    {
        "event_id": "1233912",
        "event_date": "12-01-2020",
        "event_time": "18:40",
        "away_team_id": "52",
        "away_nick_name": "Seahawks",
        "away_city": "Seattle",
        "away_rank": "19",
        "away_rank_points": "-3.42",
        "home_team_id": "39",
        "home_nick_name": "Packers",
        "home_city": "Green Bay",
        "home_rank": "12",
        "home_rank_points": "5.05"
    }
]
```

### Prerequisites
```
Python 3.x
Pytest 6.0.0
```

### Installing
```
pip install -r requirements.txt
```

## Running the tests
Tests are written and can be verified by the following command:<br/>
**For Linux and Mac**
```
$ python3 -m pytest
```
### Main Program Execution
```
python3 app.py
```

### Coding style:
![js-standard-style](https://img.shields.io/badge/code%20style-PEP%208-brightgreen.svg?style=flat)

