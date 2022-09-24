def execute(response, currentEvolution):
    nextEvolution = False
    for evo in response.css('.evochain').css('a').xpath('@href').getall():
        if nextEvolution:
            return response.xpath('//table//td[@align="right"]').css('a[href*=pokedex] ::text').getall()[1].strip()
        elif evo == currentEvolution:
            nextEvolution = True