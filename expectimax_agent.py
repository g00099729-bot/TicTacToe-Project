from agent_base import Agent
from game import GameState
from evaluation import betterEvaluationFunction


class ExpectimaxAgent(Agent):
    def get_action(self, state: GameState, depth=None):
        """
        Returns the best move index (0-8) using Expectimax search.
        Handles stochastic (non-optimal) opponent moves.
        """
        value, action = self.expectimax(state, depth_limit=depth, current_depth=0)
        # Safety fallback in case no action is found
        if action is None:
            legal = state.get_legal_actions()
            if legal:
                action = legal[0]
        return action

    def expectimax(self, state: GameState, depth_limit, current_depth):
        # Terminal check
        if state.is_terminal():
            return state.utility(), None

        # Cutoff check
        if depth_limit is not None and current_depth >= depth_limit:
            return betterEvaluationFunction(state), None

        if state.to_move == 'X':
            best_val = float('-inf')
            best_act = None

            for a in state.get_legal_actions():
                s2 = state.generate_successor(a)
                v, _ = self.expectimax(s2, depth_limit, current_depth + 1)

                if v > best_val:
                    best_val = v
                    best_act = a

            return best_val, best_act

        else:
            actions = state.get_legal_actions()
            if not actions:

                return betterEvaluationFunction(state), None

            total = 0.0
            for a in actions:
                s2 = state.generate_successor(a)
                v, _ = self.expectimax(s2, depth_limit, current_depth + 1)
                total += v

            expected_value = total / len(actions)
            # No single "best action" at chance nodes (environment/opponent chooses randomly)
            return expected_value, None
            _, action = self.minimax(state)
            return action
