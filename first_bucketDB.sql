CREATE TABLE teams (
		team_id int PRIMARY KEY,
    name VARCHAR(40),
    abbrev CHAR(3)
);

CREATE TABLE games (
		game_id VARCHAR(15),
    first_scorer VARCHAR(40),
		overall boolean,
    team_id int,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
);

ALTER TABLE games
  ADD CONSTRAINT uq_games UNIQUE(game_id, team_id);

INSERT INTO teams (team_id, name, abbrev) values ('0', 'Atlanta Hawks', 'ATL');
INSERT INTO teams (team_id, name, abbrev) values ('1', 'Brooklyn Nets', 'BKN');
INSERT INTO teams (team_id, name, abbrev) values ('2', 'Boston Celtics', 'BOS');
INSERT INTO teams (team_id, name, abbrev) values ('3', 'Charlotte Hornets', 'CHA');
INSERT INTO teams (team_id, name, abbrev) values ('4', 'Chicago Bulls', 'CHI');
INSERT INTO teams (team_id, name, abbrev) values ('5', 'Cleveland Cavaliers', 'CLE');
INSERT INTO teams (team_id, name, abbrev) values ('6', 'Dallas Mavericks', 'DAL');
INSERT INTO teams (team_id, name, abbrev) values ('7', 'Denver Nuggets', 'DEN');
INSERT INTO teams (team_id, name, abbrev) values ('8', 'Detroit Pistons', 'DET');
INSERT INTO teams (team_id, name, abbrev) values ('9', 'Golden State Warriors', 'GSW');
INSERT INTO teams (team_id, name, abbrev) values ('10', 'Houston Rockets', 'HOU');
INSERT INTO teams (team_id, name, abbrev) values ('11', 'Indiana Pacers', 'IND');
INSERT INTO teams (team_id, name, abbrev) values ('12', 'Los Angeles Clippers', 'LAC');
INSERT INTO teams (team_id, name, abbrev) values ('13', 'Los Angeles Lakers', 'LAL');
INSERT INTO teams (team_id, name, abbrev) values ('14', 'Memphis Grizzlies', 'MEM');
INSERT INTO teams (team_id, name, abbrev) values ('15', 'Miami Heat', 'MIA');
INSERT INTO teams (team_id, name, abbrev) values ('16', 'Milwaukee Bucks', 'MIL');
INSERT INTO teams (team_id, name, abbrev) values ('17', 'Minnesota Timberwolves', 'MIN');
INSERT INTO teams (team_id, name, abbrev) values ('18', 'New Orleans Pelicans', 'NOP');
INSERT INTO teams (team_id, name, abbrev) values ('19', 'New York Knicks', 'NYK');
INSERT INTO teams (team_id, name, abbrev) values ('20', 'Oklahoma City Thunder', 'OKC');
INSERT INTO teams (team_id, name, abbrev) values ('21', 'Orlando Magic', 'ORL');
INSERT INTO teams (team_id, name, abbrev) values ('22', 'Philadelphia 76ers', 'PHI');
INSERT INTO teams (team_id, name, abbrev) values ('23', 'Phoenix Suns', 'PHX');
INSERT INTO teams (team_id, name, abbrev) values ('24', 'Portland Trail Blazers', 'POR');
INSERT INTO teams (team_id, name, abbrev) values ('25', 'Sacramento Kings', 'SAC');
INSERT INTO teams (team_id, name, abbrev) values ('26', 'San Antonio Spurs', 'SAS');
INSERT INTO teams (team_id, name, abbrev) values ('27', 'Toronto Raptors', 'TOR');
INSERT INTO teams (team_id, name, abbrev) values ('28', 'Utah Jazz', 'UTA');
INSERT INTO teams (team_id, name, abbrev) values ('29', 'Washington Wizards', 'WAS');