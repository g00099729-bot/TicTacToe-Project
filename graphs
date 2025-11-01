import matplotlib.pyplot as plt
import numpy as np

# Matchup names
matchups = [
    "Minimax (X) vs AlphaBeta (O)",
    "Minimax (X) vs Expectimax (O)",
    "AlphaBeta (X) vs Minimax (O)",
    "AlphaBeta (X) vs Expectimax (O)",
    "Expectimax (X) vs Minimax (O)",
    "Expectimax (X) vs AlphaBeta (O)"
]

# Number of wins/draws from your results
x_wins = [0, 5, 0, 5, 0, 0]
o_wins = [0, 0, 0, 0, 0, 0]
draws  = [5, 0, 5, 0, 5, 5]

# Average decision times
avg_time_x = [1.8098, 1.73201, 0.00226, 0.00222, 1.77377, 2.89978]
avg_time_o = [0.00219, 0.18811, 0.18256, 0.18266, 0.18653, 0.003]

# ------------------ WINS BAR CHART ------------------
bar_width = 0.2
index = np.arange(len(matchups))

plt.figure(figsize=(12,6))
plt.bar(index, x_wins, bar_width, label="X Wins", color='skyblue')
plt.bar(index + bar_width, o_wins, bar_width, label="O Wins", color='salmon')
plt.bar(index + 2*bar_width, draws, bar_width, label="Draws", color='lightgreen')

plt.xlabel("Matchups")
plt.ylabel("Number of Games")
plt.title("Tic-Tac-Toe Agent Comparison - Wins and Draws")
plt.xticks(index + bar_width, matchups, rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

# ------------------ DECISION TIME BAR CHART ------------------
plt.figure(figsize=(12,6))
plt.bar(index, avg_time_x, bar_width, label="Avg Time X (s)", color='skyblue')
plt.bar(index + bar_width, avg_time_o, bar_width, label="Avg Time O (s)", color='salmon')

plt.xlabel("Matchups")
plt.ylabel("Average Decision Time (s)")
plt.title("Tic-Tac-Toe Agent Comparison - Average Decision Time")
plt.xticks(index + bar_width/2, matchups, rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
