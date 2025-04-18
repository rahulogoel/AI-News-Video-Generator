import requests

API_KEY = 'enter-newsapi-api-key'       # https://newsapi.org/register
NEWS_URL = 'https://newsapi.org/v2/top-headlines'

def get_top_headlines(country='us', category='general', limit=5):
    params = {
        'apiKey': API_KEY,
        'country': country,
        'category': category,
        'pageSize': limit,
    }
    response = requests.get(NEWS_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
    articles = response.json().get('articles', [])
    results = []

    for article in articles:
        results.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'source': article['source']['name']
        })
    
    return results

# Example usage
if __name__ == "__main__":
    headlines = get_top_headlines()
    for idx, article in enumerate(headlines, start=1):
        print(f"\n[{idx}] {article['title']}\n{article['description']}\n(Source: {article['source']})\n")
