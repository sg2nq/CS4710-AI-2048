from math import log


#class ReflexAgent(object):
    # def __init__(self):
    #     pass
    #
    # def evaluation(self, game, action):
    #     current_state = game.get_current_state()
    #     next_state = game.get_next_state(current_state, action)
    #
    #     adjacent_cells = 0
    #     next_empty_slots = 0
    #     for coord in next_state:
    #         if not next_state[coord]:
    #             next_empty_slots += 1
    #         else:
    #             x, y = coord
    #             if x > 0 and next_state[coord] == next_state[x-1, y]:
    #                 adjacent_cells += 1
    #             if x < 3 and next_state[coord] == next_state[x+1, y]:
    #                 adjacent_cells += 1
    #             if y > 0 and next_state[coord] == next_state[x, y-1]:
    #                 adjacent_cells += 1
    #             if y < 3 and next_state[coord] == next_state[x, y+1]:
    #                 adjacent_cells += 1
    #
    #     max_tile = next_state[max(next_state, key=next_state.get)]
    #
    #     return next_empty_slots + max_tile + adjacent_cells
    #
    # def get_action(self, game):
    #     evals = []
    #     for action in game.get_actions():
    #         evals.append((action, self.evaluation(game, action)))
    #     return max(evals, key=lambda item: item[1])[0]


class ExpectimaxAgent(object):
    def __init__(self, depth=2):
        self.depth = depth
        #possible_moves = state.get_possible_states()

    def evaluation(self, state, direc):
        # Get the biggest block on the board
        # biggest_block = log(state[max(state, key=state.get)], 2)
        # biggest_block = log(state[max(state, key=state.get)], 2)
        # biggest_block = log(state[max(state, key=state.get)], 2)
        # print(state.values())
        biggest_block = 0
        sec_biggest_block = 0
        third_biggest_block = 0
        if sorted(state.values(), reverse=True)[0]:
            biggest_block = log(sorted(state.values(), reverse=True)[0], 2)
        if sorted(state.values(), reverse=True)[1]:
            sec_biggest_block = log(sorted(state.values(), reverse=True)[1], 2)
        if sorted(state.values(), reverse=True)[2]:
            third_biggest_block = log(sorted(state.values(), reverse=True)[2], 2)

        # Count the number of blank spots
        blank_spots = 0

        # The bigger the corner block the better
        corner_block = 0
        for coord in state:
            if not state[coord]:
                blank_spots += 1
        if state[(0, 0)]:  # randomly picked top left corner because that's how I play
            corner_block += log(state[(0, 0)], 2) * 3
        if state[(0, 1)]:  # randomly picked top left corner because that's how I play
            corner_block += log(state[(0, 1)], 2) * 2
        if state[(0, 2)]:  # randomly picked top left corner because that's how I play
            corner_block += log(state[(0, 2)], 2) * 2

        # Since we're aiming for the block to be the top left, arbitrary point for up or left move
        dir_points = 0
        if direc == "left" or direc == "up":
            dir_points += 20
        return biggest_block * 3 + sec_biggest_block * 2 + third_biggest_block + blank_spots + corner_block + dir_points

    def get_action(self, game):
        v = [float("-inf"), ""]
        v = max(v, self.value(game, game.get_current_state(), 0, 2, ""))
        return v[1]

    def value(self, game, state, agent, depth, direc = ""):
        if agent == 1:
            depth -= 1
        if len(game.get_actions(state)) == 0 or depth == 0:
            return self.evaluation(state, direc), ""


        if agent == 0:
            return self.max_value(game, state, depth, direc)
        else:
            return self.exp_value(game, state, depth, direc)

    def max_value(self, game, state, depth, direc = ""):

        v = [float("-inf"), ""]
        for direc in game.get_actions():
            v = max([self.value(game, game.get_next_state(state, direc), 1, depth, direc)[0], direc], v)

        return v


    def exp_value(self, game, state, depth, direc = ""):
        v = 0
        possible_moves = game.get_possible_states(state)
        for new_state in possible_moves:
            p = self.value(game, new_state, 0, depth, direc)[0]
            try:
                v += 1.0 / len(possible_moves) * p
            except:
                v += 1.0 * p
        return v, ""


###### BETTER VERSION
    # def get_action(self, game):
    #     v = [float("-inf"), ""]
    #     v = max(v, self.value(game, game.get_current_state(), 0, self.depth, ""))
    #     return v[1]
    #
    # def value(self, game, state, agent, depth, direc = ""):
    #     if agent == 1:
    #         depth -= 1
    #     if len(game.get_actions(state)) == 0 or self.depth == 0 or depth == 0:
    #         return self.evaluation(state, direc), ""
    #     if agent == 0:
    #         return self.max_value(game, state, direc)
    #     else:
    #         return self.exp_value(game, state, direc)
    #
    # def max_value(self, game, state, direc = ""):
    #     if len(game.get_actions(state)) == 0 or self.depth == 0:
    #         return self.evaluation(state, direc), ""
    #
    #     v = [float("-inf"), ""]
    #     for direc in game.get_actions():
    #         v = max([self.value(game, game.get_next_state(state, direc), 1, self.depth, direc)[0], direc], v)
    #
    #     return v
    #
    #
    # def exp_value(self, game, state, direc = ""):
    #     if len(game.get_actions(state)) == 0 or self.depth == 0:
    #         return  self.evaluation(state, direc), ""
    #     v = 0
    #     possible_moves = game.get_possible_states(state)
    #     for new_state in possible_moves:
    #         p = (ExpectimaxAgent(depth=self.depth - 1).value(game, new_state, 0, self.depth, direc))[0]
    #         #p = (ExpectimaxAgent(depth=self.depth - 1).value(game, new_state, 0, self.depth, direc))[0]
    #         try:
    #             v += 1.0 / len(possible_moves) * p
    #         except:
    #             v += 1.0 * p
    #     return v, ""

####################################
    # def get_action(self, game):
    #     v = [float("-inf"), ""]
    #     v = max(v, self.value(game, game.get_current_state(), ""))
    #     return v[1]
    #
    # def value(self, game, state, direc = ""):
    #     if len(game.get_actions(state)) == 0 or self.depth == 0:
    #         return self.evaluation(state, direc), ""
    #
    #     return self.max_value(game, state, direc)
    #
    # def max_value(self, game, state, direc = ""):
    #     if len(game.get_actions(state)) == 0 or self.depth == 0:
    #         return self.evaluation(state, direc), ""
    #
    #     v = [float("-inf"), ""]
    #     for direc in game.get_actions():
    #         v = max([self.exp_val(game, game.get_next_state(state, direc), direc)[0], direc], v)
    #
    #     return v
    #
    #
    # def exp_val(self, game, state, direc = ""):
    #     if len(game.get_actions(state)) == 0 or self.depth == 0:
    #         return  self.evaluation(state, direc), ""
    #     v = 0
    #     possible_moves = game.get_possible_states(state)
    #     for new_state in possible_moves:
    #         p = (ExpectimaxAgent(depth=self.depth - 1).value(game, new_state, direc))[0]
    #         try:
    #             v += 1.0 / len(possible_moves) * p
    #         except:
    #             v += 1.0 * p
    #     return v, ""
