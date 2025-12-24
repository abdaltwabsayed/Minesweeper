

import heapq
import copy
import random


class AStarSolver:
    def __init__(self, board):
        self.board = board

    # ---------- MAIN LOOP ----------
    def solve(self):
        if self.board.clickNumber == 0:
            x = random.choice(range(self.board.getSize()[0]))
            y = random.choice(range(self.board.getSize()[1]))
            piece = self.board.getPiece((x, y))
            piece.setHasBomb(False)
            self.board.handleClick(piece, False)
            self.board.setNeighbors()

        plan = self.a_star()
        if not plan:
            return

        for task in plan:
            action, neighbors = task
            if action == "open":
                self.openUnflagged(neighbors)
            elif action == "flag":
                self.flagAll(neighbors)

    # ---------- A* SEARCH ----------
    def a_star(self):
        pq = []
        h, g = 0, 0

        heapq.heappush(pq, (self.board, [h, g]))

        visited = set()

        while pq:
            board, path = heapq.heappop(pq)
            piecesState = self.heuristic(board)

            if piecesState in visited:
                continue
            visited.add(piecesState)

            # ---------- deterministic moves (cost 0) ----------
            actions = self.deterministic_actions(board)
            if actions:
                path[1] += len(actions)
                return actions

            # ---------- guessing (cost 1) ----------
            guesses = self.guess_actions(board)
            if guesses:
                path[0] += len(guesses)
                return guesses

        return []

    def deterministic_actions(self, board):
        actions = []
        for row in board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    continue

                around = piece.getNumberAround()
                neighbors = piece.getNeighbors()
                unknown, flagged = 0, 0
                for p in neighbors:
                    if not p.getClicked(): unknown += 1
                    if p.getFlagged(): flagged += 1

                if around == flagged and unknown > 0:
                    actions.append(("open", neighbors))
                if around == unknown and unknown > 0:
                    actions.append(("flag", neighbors))
        return actions

    def guess_actions(self, board):
        actions = []
        for row in board.getBoard():
            for piece in row:
                around = piece.getNumberAround()
                neighbors = piece.getNeighbors()
                unknown, flagged = 0, 0
                for p in neighbors:
                    if not p.getClicked(): unknown += 1
                    if p.getFlagged(): flagged += 1
                if unknown > (around - flagged):
                    actions.append(("open", neighbors))
        return actions  # single guess is enough

    def heuristic(self, board):
        piecesState = []
        for row in board.getBoard():
            for piece in row:
                piecesState.append((piece.getClicked(), piece.getFlagged(), piece.getNumberAround()))
        return tuple(piecesState)

    def openUnflagged(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, False)

    def flagAll(self, neighbors):
        for piece in neighbors:
            if not piece.getFlagged():
                self.board.handleClick(piece, True)

