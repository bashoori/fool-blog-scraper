import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL of Motley Fool
BASE_URL = "https://www.fool.com"

# Starting point for crawling blog articles (investing category)
START_URL = "https://www.fool.com/investing/"

# Headers to mimic a real browser (important to avoid getting blocked)
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Function to extract unique article links from a category or paginated page
def get_article_links(page_url):
    res = requests.get(page_url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Select all anchor tags that likely point to blog articles under "/investing/"
    articles = soup.select('a[href*="/investing/"]')
    
    # Remove query params and keep unique URLs
    links = {BASE_URL + a['href'].split('?')[0] for a in articles if '/investing/' in a['href']}
    
    return list(links)

# Function to extract title and article text from a given URL
def scrape_article(url):
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, 'html.parser')

        # Get article title (usually inside <h1>)
        title = soup.find('h1').text.strip()

        # Get all paragraphs inside <article> tag
        paragraphs = soup.select('article p')
        text = "\n".join([p.get_text(strip=True) for p in paragraphs])

        return {"url": url, "title": title, "text": text}
    
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None

# Main scraping loop
all_articles = []   # Stores scraped articles
seen_urls = set()   # Track visited URLs
page_num = 1        # Start from page 1

# Loop through paginated category pages until 20 articles or max 10 pages
while len(all_articles) < 20 and page_num < 10:
    print(f"🔄 Scraping page {page_num}...")

    # Construct paginated URL (Motley Fool uses ?page=2, etc.)
    page_url = f"{START_URL}?page={page_num}"

    # Extract article links from the page
    urls = get_article_links(page_url)
    
    for url in urls:
        # Skip already visited URLs and stop after 1000 articles
        if url not in seen_urls and len(all_articles) < 1000:
            seen_urls.add(url)

            # Scrape the article content
            article = scrape_article(url)

            if article:
                all_articles.append(article)
                print(f"✅ Collected: {article['title']}")
                time.sleep(1)  # Be polite with 1-second delay

    page_num += 1
    time.sleep(2)  # Add delay between pages to avoid overloading server

# Save scraped articles to CSV file in /data folder
df = pd.DataFrame(all_articles)
df.to_csv("data/fool_blog_posts.csv", index=False)
print("🎉 Scraping complete! Saved to data/fool_blog_posts.csv")