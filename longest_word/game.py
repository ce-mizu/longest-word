import string
import random

class Game:
    """Criação da classe Game"""
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy()
        for w in word:
            if w in letters:
                letters.remove(w)
            else:
                return False
        return True
