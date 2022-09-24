import pandas as pd

POKEMONS_PATH = '../scraper/pokemons.json'
CSV_PATH = 'pokemons.csv'


def read(): pd.read_json(POKEMONS_PATH).to_csv(path_or_buf = CSV_PATH)


if __name__ == '__main__': read()
