class ScoreCard:
    def __init__(self, scorecard, home_team, away_team):
        self.event_id = scorecard.get('event_id')
        self.event_date = scorecard.get('event_date').split(' ')[0] # TODO: DD-MM-YYYY
        self.event_time = scorecard.get('event_date').split(' ')[1] # TODO: HH:MM
        self.away_team_id = scorecard.get('away_team_id')
        self.away_nick_name = scorecard.get('away_nick_name')
        self.away_city = scorecard.get('away_city')
        self.home_team_id = scorecard.get('home_team_id')
        self.home_nick_name = scorecard.get('home_nick_name')
        self.home_city = scorecard.get('home_city')
        self.away_rank = away_team.get('rank')
        self.home_rank = home_team.get('rank')
        self.away_rank_points = "{:.2f}".format(round(float(away_team.get('adjusted_points')), 2))
        self.home_rank_points = "{:.2f}".format(round(float(home_team.get('adjusted_points')), 2))