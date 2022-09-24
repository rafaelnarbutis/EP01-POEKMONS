SELECT = '//table[@class="dextable"][position()=4]//tr[3]//td//text()'


def execute(response):
    damages = []
    for idx, damage in enumerate(response.xpath(SELECT).getall()):
        if idx == 0:        damages.append("NORMAL: " + str(damage).replace("*", "").strip())
        elif idx == 1:      damages.append("FIRE: " + str(damage).replace("*", "").strip())
        elif idx == 2:      damages.append("WATER: " + str(damage).replace("*", "").strip())
        elif idx == 3:      damages.append("ELECTRIC: " + str(damage).replace("*", "").strip())
        elif idx == 4:      damages.append("GRASS: " + str(damage).replace("*", "").strip())
        elif idx == 5:      damages.append("ICE: " + str(damage).replace("*", "").strip())
        elif idx == 6:      damages.append("FIGHT: " + str(damage).replace("*", "").strip())
        elif idx == 7:      damages.append("POISON: " + str(damage).replace("*", "").strip())
        elif idx == 8:      damages.append("GROUND: " + str(damage).replace("*", "").strip())
        elif idx == 9:      damages.append("FLYING: " + str(damage).replace("*", "").strip())
        elif idx == 10:     damages.append("PSYCHIC: " + str(damage).replace("*", "").strip())
        elif idx == 11:     damages.append("BUG: " + str(damage).replace("*", "").strip())
        elif idx == 12:     damages.append("ROCK: " + str(damage).replace("*", "").strip())
        elif idx == 13:     damages.append("GHOST: " + str(damage).replace("*", "").strip())
        elif idx == 14:     damages.append("DRAGON: " + str(damage).replace("*", "").strip())
    return damages
