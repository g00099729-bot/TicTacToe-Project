# minimax_agent.py
from agent_base import Agent
from game import GameState

class MinimaxAgent(Agent):
    def get_action(self, state: GameState, depth=None):
        _, action = self.minimax(state, depth)
        return action

    def minimax(self, state: GameState, depth_limit=None):
    # Terminal state: return utility and no action
    if state.is_terminal() or (depth_limit is not None and depth_limit == 0):
        return state.utility(), None

    # MAX player ('X')
    if state.to_move == 'X':
        max_value = float('-inf')
        best_action = None
        for action in state.get_legal_actions():
            successor = state.generate_successor(action)
            value, _ = self.minimax(successor, None if depth_limit is None else depth_limit - 1)
            if value > max_value:
                max_value = value
                best_action = action
        return max_value, best_action

    # MIN player ('O')
    else:  # state.to_move == 'O'
        min_value = float('inf')
        best_action = None
        for action in state.get_legal_actions():
            successor = state.generate_successor(action)
            value, _ = self.minimax(successor, None if depth_limit is None else depth_limit - 1)
            if value < min_value:
                min_value = value
                best_action = action
        return min_value, best_action
