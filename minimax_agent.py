# minimax_agent.py
from agent_base import Agent
from game import GameState

class MinimaxAgent:
    def get_action(self, state, depth_limit=None):
        _, action = self.minimax(state)
        return action

    def minimax(self, state):
        # Base case: check for terminal state
        if state.is_terminal():
            return state.utility(), None

        if state.current_player == 'X':  # Maximizing player
            best_val = float('-inf')
            best_action = None
            for action in state.get_legal_actions():
                val, _ = self.minimax(state.result(action))
                if val > best_val:
                    best_val = val
                    best_action = action
            return best_val, best_action
        else:  # Minimizing player
            best_val = float('inf')
            best_action = None
            for action in state.get_legal_actions():
                val, _ = self.minimax(state.result(action))
                if val < best_val:
                    best_val = val
                    best_action = action
            return best_val, best_action
