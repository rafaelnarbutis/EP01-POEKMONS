SELECT = '//table[@class="dextable"][position()=2]//tr[4]//td[3]//text()'

def execute(response): return response.xpath(SELECT).getall()[1].strip()