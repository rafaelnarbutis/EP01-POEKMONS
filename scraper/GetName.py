CSS = 'title::text'

def execute(response): return response.css(CSS).get().split('-')[2].strip()