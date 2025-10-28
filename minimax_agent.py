# minimax_agent.py
from agent_base import Agent
from game import GameState

class MinimaxAgent(Agent):
    def get_action(self, state: GameState, depth=None):
        _, action = self.minimax(state)
        return action

    def minimax(self, state, depth_limit=None):
       
        if state.is_terminal():
            return state.utility(), None

        player = state.to_move
        legal_actions = state.get_legal_actions()

        if player == 'X':
            best_value = float('-inf')
            best_action = None

            for action in legal_actions:
                successor = state.generate_successor(action)
                value, _ = self.minimax(successor, depth_limit)
                if value > best_value:
                    best_value = value
                    best_action = action

            return best_value, best_action

        else:
            best_value = float('inf')
            best_action = None

            for action in legal_actions:
                successor = state.generate_successor(action)
                value, _ = self.minimax(successor, depth_limit)
                if value < best_value:
                    best_value = value
                    best_action = action

            return best_value, best_action
