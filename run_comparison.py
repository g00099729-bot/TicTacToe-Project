# run_comparison.py
from game import GameState
from agent_base import MinimaxAgent, AlphaBetaAgent, ExpectimaxAgent
import time
import pandas as pd

def compare_agents():
    state = GameState()
    agents = {
        "Minimax": MinimaxAgent(depth=4),
        "AlphaBeta": AlphaBetaAgent(depth=4),
        "Expectimax": ExpectimaxAgent(depth=4)
    }

    results = []
    for name, agent in agents.items():
        move, score, elapsed = agent.get_action(state)
        results.append({
            "Agent": name,
            "Best Move": move,
            "Score": round(score, 2),
            "Execution Time (s)": round(elapsed, 5)
        })

    df = pd.DataFrame(results)
    print(df)
    df.to_csv("comparison_results.csv", index=False)

if __name__ == "__main__":
    compare_agents()
