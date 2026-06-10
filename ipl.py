# IPL Data Analysis Project
# Python 3.6.4 compatible
# Required libraries: pandas, matplotlib
# Install: pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("ipl_matches.csv")
players = pd.read_csv("ipl_players.csv")

print("\n===== IPL DATA ANALYSIS PROJECT =====")
print("\nFirst 5 Matches:")
print(matches.head())

print("\nDataset Shape:")
print(matches.shape)

print("\nColumns:")
print(matches.columns.tolist())

print("\n===== Team-wise Wins =====")
team_wins = matches["winner"].value_counts()
print(team_wins)

print("\n===== Toss Decision Count =====")
print(matches["toss_decision"].value_counts())

print("\n===== Player of Match Count =====")
print(matches["player_of_match"].value_counts())

print("\n===== Season-wise Matches =====")
print(matches["season"].value_counts().sort_index())

print("\n===== Top Run Scorers =====")
top_runs = players.sort_values(by="runs", ascending=False)
print(top_runs[["player", "team", "runs"]])

print("\n===== Top Wicket Takers =====")
top_wickets = players.sort_values(by="wickets", ascending=False)
print(top_wickets[["player", "team", "wickets"]])

print("\n===== Team Performance Summary =====")
summary = []

teams = sorted(set(matches["team1"]).union(set(matches["team2"])))

for team in teams:
    played = len(matches[(matches["team1"] == team) | (matches["team2"] == team)])
    won = len(matches[matches["winner"] == team])
    lost = played - won
    win_percent = round((won / played) * 100, 2) if played > 0 else 0
    summary.append([team, played, won, lost, win_percent])

summary_df = pd.DataFrame(summary, columns=["Team", "Played", "Won", "Lost", "Win %"])
summary_df = summary_df.sort_values(by=["Won", "Win %"], ascending=False)
print(summary_df)

summary_df.to_csv("team_performance_summary.csv", index=False)

# Graph 1: Team wins
plt.figure(figsize=(10, 5))
team_wins.plot(kind="bar")
plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.tight_layout()
plt.savefig("team_wins.png")
plt.show()

# Graph 2: Top run scorers
plt.figure(figsize=(10, 5))
top_runs.head(5).plot(x="player", y="runs", kind="bar", legend=False)
plt.title("Top 5 Run Scorers")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.tight_layout()
plt.savefig("top_run_scorers.png")
plt.show()

# Graph 3: Top wicket takers
plt.figure(figsize=(10, 5))
top_wickets.head(5).plot(x="player", y="wickets", kind="bar", legend=False)
plt.title("Top 5 Wicket Takers")
plt.xlabel("Players")
plt.ylabel("Wickets")
plt.tight_layout()
plt.savefig("top_wicket_takers.png")
plt.show()

print("\nAnalysis completed successfully.")
print("Files created:")
print("1. team_performance_summary.csv")
print("2. team_wins.png")
print("3. top_run_scorers.png")
print("4. top_wicket_takers.png")
