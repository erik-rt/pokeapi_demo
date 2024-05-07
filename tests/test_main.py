import unittest
import requests_mock
from poke_api.main import fetch_pages, count_a_moves


class TestMain(unittest.TestCase):
    @requests_mock.Mocker()
    def test_fetch_pages(self, m):
        m.get(
            "https://pokeapi.co/api/v2/generation", json={"next": None, "results": []}
        )
        pages = list(fetch_pages("https://pokeapi.co/api/v2/generation"))
        self.assertEqual(len(pages), 1)

    @requests_mock.Mocker()
    def test_count_a_moves(self, m):
        m.get(
            "https://pokeapi.co/api/v2/generation",
            json={
                "next": None,
                "results": [
                    {"name": "gen1", "url": "https://pokeapi.co/api/v2/generation/1/"}
                ],
            },
        )
        m.get(
            "https://pokeapi.co/api/v2/generation/1/",
            json={"moves": [{"name": "a-move"}, {"name": "b-move"}]},
        )
        moves = list(count_a_moves())
        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0], ("gen1", 1))


if __name__ == "__main__":
    unittest.main()
