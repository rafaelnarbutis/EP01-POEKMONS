SELECT = '//table[@class="dextable"][position()=2]//tr[4]//td[2]//text()'

def execute(response): return response.xpath(SELECT).getall()[2].strip()
