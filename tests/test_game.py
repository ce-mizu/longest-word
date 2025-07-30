"""Testes para a classe Game."""

from src.longest_word.game import Game
import string


class TestGame:
    """Classe de testes unitários para a classe Game."""

    def test_game_initialization(self):
        """Teste se a grade é inicializada corretamente."""
        # setup
        new_game = Game()

        # exercise
        grid = new_game.grid

        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        """Teste para garantir que uma palavra vazia seja inválida."""
        new_game = Game()
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        """Teste com palavra válida que pode ser formada a partir da grade."""
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert new_game.is_valid(test_word) is True
        assert new_game.grid == list(test_grid)  # Garante que a grade não foi alterada

    def test_is_invalid(self):
        """Teste com palavra inválida que não pode ser formada a partir da grade."""
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word) is False
        assert new_game.grid == list(test_grid)
