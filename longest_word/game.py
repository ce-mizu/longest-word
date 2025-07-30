"""Módulo que define a classe Game, responsável por gerar uma grade de letras
e verificar se palavras são válidas com base nessa grade.
"""
import string
import random

class Game:
    """Classe que representa um jogo de formação de palavras a partir de uma grade aleatória."""
    def __init__(self) -> list:
        """Inicializa o jogo com uma grade aleatória de 9 letras maiúsculas."""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Verifica se a palavra pode ser formada com as letras da grade atual.
        Args:
            word (str): A palavra a ser verificada.
        Returns:
            bool: True se a palavra é válida, False caso contrário.
        """
        if not word:
            return False
        letters = self.grid.copy()
        for w in word:
            if w in letters:
                letters.remove(w)
            else:
                return False
        return True

    def __str__(self):
        return f"Grade atual: {' '.join(self.grid)}"
