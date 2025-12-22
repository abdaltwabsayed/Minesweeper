

import heapq
import copy

class AStarSolver:
    def __init__(self, board):
        self.board = board

    # ---------- MAIN LOOP ----------
    def move(self):
        plan = self.a_star()
        if not plan:
            return

        action, neighbors = plan[0]
        if action == "open":
            self.openUnflagged(neighbors)
        elif action == "flag":
            self.flagAll(neighbors)

    # ---------- A* SEARCH ----------
    def a_star(self):
        start = copy.deepcopy(self.board)

        pq = []
        counter = 0

        h0 = self.heuristic(start)
        heapq.heappush(pq, (h0, 0, counter, start, []))
        counter += 1

        visited = set()

        while pq:
            f, g, _, board, path = heapq.heappop(pq)

            key = self.board_key(board)
            if key in visited:
                continue
            visited.add(key)

            # ---------- deterministic moves (cost 0) ----------
            actions = self.deterministic_actions(board)
            if actions:
                action = actions[0]
                return path + [action]

            # ---------- guessing (cost 1) ----------
            guesses = self.guess_actions(board)
            if guesses:
                action = guesses[0]
                return path + [action]

        return []

    def deterministic_actions(self, board):
        actions = []
        for row in board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    continue

                around = piece.getNumberAround()
                neighbors = piece.getNeighbors()
                unknown = sum(not p.getClicked() for p in neighbors)
                flagged = sum(p.getFlagged() for p in neighbors)

                if around == flagged and unknown > 0:
                    actions.append(("open", neighbors))
                elif around == unknown and unknown > 0:
                    actions.append(("flag", neighbors))
        return actions

    def guess_actions(self, board):
        actions = []
        for row in board.getBoard():
            for piece in row:
                if not piece.getClicked() and not piece.getFlagged():
                    actions.append(("open", [piece]))
        return actions[:1]  # single guess is enough

    def heuristic(self, board):
        unopened = 0
        for row in board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    unopened += 1
        return unopened

    def board_key(self, board):
        key = []
        for row in board.getBoard():
            for p in row:
                key.append((p.getClicked(), p.getFlagged(), p.getNumberAround()))
        return tuple(key)

    def openUnflagged(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, False)

    def flagAll(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, True)

