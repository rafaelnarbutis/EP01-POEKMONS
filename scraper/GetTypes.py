SELECT = '//table[@class="dextable"][position()=2]//tr[2]//td[4]//a//@href'


def execute(response):
    types = []
    for type in response.xpath(SELECT).getall():
        types.append(type.split('/')[2].split('.')[0])
    return types
