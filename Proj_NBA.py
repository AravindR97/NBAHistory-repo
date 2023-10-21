from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import matplotlib.pyplot as plt

#Getting the details of all teams from the api:
LoD = teams.get_teams()

#Converting the list into a dataframe:
df = pd.DataFrame(LoD)

#selecting the row containing info of Golden State Warriors:
df_warr = df.loc[df['nickname']=='Warriors']

#getting the unique id of Golden State Warriors:
id_warr = df_warr.iat[0,0]
                        #-Using this id, we can find the stats of Warriors-
                        #-For this LeagueGameFinder() fn (from 'leaguegamefinder' class) is used-

warr_stat = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warr)
                        #-warr_stat is an object of class leaguegamefinder-

#viewing the content of warr_stat as a dataframe:
warr_df = warr_stat.get_data_frames()[0]
                        #-get_data_frames() gives a list of dataframes-
warr_df = warr_df[['GAME_DATE', 'MATCHUP','PLUS_MINUS']]


#creating separate dataframes for home and away matches:
home_df = warr_df.loc[warr_df['MATCHUP']== 'GSW vs. TOR']
away_df = warr_df.loc[warr_df['MATCHUP']== 'GSW @ TOR']

#plotting home and away points graph:
ax = plt.gca() #to get current axis
away_df.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
home_df.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
plt.legend(["away", "home"])
plt.title('GSW vs TOR')
plt.show()

