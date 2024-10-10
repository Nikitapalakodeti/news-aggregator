import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape news articles from BBC
def scrape_bbc(url: str):
    #url = "https://www.bbc.com/news/articles/c869y6qx6e4o"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = ''
    text = ''
    for article in soup.find_all('article'):
        if title == '':
            title = article.find('h1').text	
        text = text + '\n' + article.find('p').text if article.find('p') else text
        publication_date = 'N/A'  # Modify based on actual scraping logic  

    return {'link': url, 'summary': text, 'title': title, 'publication_date': publication_date}

# Function to save articles to CSV
def save_to_csv(articles):
    df = pd.DataFrame(articles)
    df.to_csv('news_articles.csv', index=False)

# Main execution
if __name__ == "__main__":
    urls = ["https://www.bbc.com/news/articles/crkd8g307kro","https://www.bbc.com/news/articles/c869y6qx6e4o","https://www.bbc.com/news/articles/c981q381p58o","https://www.bbc.com/news/articles/c33vjjg8k3yo","https://www.bbc.com/news/articles/cx2y4ew10wxo"]
    articles = []
    for url in urls:
        articles.append(scrape_bbc(url))
    save_to_csv(articles)

    print(f"Scraped {len(articles)}articles.")
