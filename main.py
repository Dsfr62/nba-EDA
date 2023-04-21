import pandas as pd
from utils import display_df

df = pd.read_csv("./public/2021-2022 NBA Player Stats - Regular.csv", sep=";", encoding="latin-1")

mean_all_players_3P = df["3P"].mean()
mean_all_players_3PA = df["3PA"].mean()
mean_all_players_3P_pct = df["3P%"].mean()

# Best shooters
# IF 3P% > mean_all_players_3P%
df_3P_pct = df[df["3P%"] > mean_all_players_3P_pct]
# IF 3PA > mean_all_players_3PA or 5
df_3PA_mean = df_3P_pct[df_3P_pct["3PA"] > mean_all_players_3PA]
df_3P = df_3PA_mean[df_3PA_mean["3PA"] > 5]
# IF 3P > mean_all_players_3P or 2.5
df_3P_mean = df_3P[df_3P["3P"] > mean_all_players_3P]
df_3P = df_3P_mean[df_3P_mean["3P"] > 2.5]

# G * (3 * 2.5) = 3p_per_game
data = []
for value in df_3P.values:
    # Columns indexes: 1 is Player, 5 is G (game), 11 is 3P
    games_played = value[5]
    all_3P_by_game = games_played * (3 * value[11])
    to_append = [value[1], value[2], value[5], value[11], value[12], value[13], all_3P_by_game]
    data.append(to_append)

new_df = pd.DataFrame(data=data, columns=["Player", "Pos", "Games", "3P", "3PA", "3P%", "3PG"])

print(f"""
Shooters analysis of NBA players stats during regular season
mean of 3 point goals per game: {mean_all_players_3P.__round__(2)}
mean of 3 point goal attempted per game: {mean_all_players_3PA.__round__(2)}
mean of 3 point goal percentage per game: {mean_all_players_3P_pct.__round__(2)}

Top 5 best PG shooters of regular season 2021 - 2022
{display_df(new_df[new_df["Pos"] == "PG"][["Player", "3PG"]].sort_values("3PG", ascending=False).head())}

Top 5 best SG shooters of regular season 2021 - 2022
{display_df(new_df[new_df["Pos"] == "SG"][["Player", "3PG"]].sort_values("3PG", ascending=False).head())}

Top 5 best SF shooters of regular season 2021 - 2022
{display_df(new_df[new_df["Pos"] == "SF"][["Player", "3PG"]].sort_values("3PG", ascending=False).head())}
""")