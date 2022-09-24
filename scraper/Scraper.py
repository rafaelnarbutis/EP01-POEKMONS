import json

import scrapy

import GetDamageTaken
import GetEvolution
import GetHeight
import GetName
import GetNumber
import GetTypes
import GetWeight
from Pokemon import Pokemon

BASE_URL = 'https://www.serebii.net'


def writeResult(pokemons):
    filename = f'pokemons.json'
    with open(filename, 'a') as f:
        f.write(json.dumps(pokemons, default=lambda o: o.__dict__, indent=4))
        f.close()


class PokemonScraper(scrapy.Spider):
    name = "pokemon_spider"
    currentEvolution = '/pokedex/001.shtml'
    start_urls = [BASE_URL + currentEvolution]
    pokemons = []

    def parse(self, response):
        pokemon = Pokemon()

        pokemon.setName(GetName.execute(response))
        pokemon.setNumber(GetNumber.execute(response))
        pokemon.setHeight(GetHeight.execute(response))
        pokemon.setWeight(GetWeight.execute(response))
        pokemon.setTypes(GetTypes.execute(response))
        pokemon.setDamageTaken(GetDamageTaken.execute(response))
        pokemon.setEvolution(GetEvolution.execute(response, self.currentEvolution))

        self.pokemons.append(pokemon)

        nextPage = response.xpath('//table//td[@align="right"]').css('a[href*=pokedex]').xpath('@href').getall()

        if nextPage:
            nextPage = nextPage[0]
            self.currentEvolution = nextPage
            yield scrapy.Request(response.urljoin(BASE_URL + nextPage))
        else:
            writeResult(self.pokemons)
