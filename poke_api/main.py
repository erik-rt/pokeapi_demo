from typing import Generator, Tuple, Dict
import requests


def fetch_pages(url: str) -> Generator[Dict, None, None]:
    """
    Generator function that fetches pages from the given URL one at a time.

    Parameters:
    url (str): The URL to fetch pages from.

    Yields:
    dict: The JSON data of the next page.

    Raises:
    Exception: If the request fails.
    """
    while url:
        res = requests.get(url)
        if res.status_code != 200:
            raise Exception(f"Request failed with status {res.status_code}")
        data = res.json()
        url = data.get("next")
        yield data


def count_a_moves() -> Generator[Tuple[str, int], None, None]:
    """
    Generator function that counts the number of 'a' moves in each generation.

    Yields:
    tuple: A tuple containing the name of the generation and the count of 'a' moves.

    Raises:
    Exception: If the request fails.
    """
    for page in fetch_pages("https://pokeapi.co/api/v2/generation"):
        for generation in page["results"]:
            gen_res = requests.get(generation["url"])
            if gen_res.status_code != 200:
                raise Exception(f"Request failed with status {gen_res.status_code}")
            gen_data = gen_res.json()
            a_moves = sum(
                1 for move in gen_data["moves"] if move["name"].lower().startswith("a")
            )
            yield generation["name"], a_moves


def main():
    """
    Main function that finds the generation with the most 'a' moves and prints it.
    """
    max_moves = 0
    max_gen = None
    for gen, a_moves in count_a_moves():
        if a_moves > max_moves:
            max_moves = a_moves
            max_gen = gen

    print(
        f"The generation with the most 'a' moves is {max_gen} with {max_moves} moves."
    )


if __name__ == "__main__":
    main()
