import requests
api = '9p70BQvR7pnuqYpWLOJ7RJuPfFJWHgVK'
ticker = 'AAPL'
limit = '10'
year = '2021'
month = '04'
day = '05'
api_url = f'https://api.polygon.io/v2/reference/news?ticker={ticker}&order=desc&limit={limit}&published_utc.gte={year}-{month}-{day}&sort=published_utc&apiKey={api}'
data = requests.get(api_url).json()
data['results'][0]['description']
list1 = []
for i in range(int(limit)):
    try:
        news = data['results'][i]['description']
        list1.append(news)
    except:
        pass

    # pawex86926@shaflyn.com