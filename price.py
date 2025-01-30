import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the price from the webpage using appropriate HTML tags and attributes
    price = soup.find('span', {'class': 'price'}).text.strip()
    
    return price

def compare_prices(product_name, urls):
    prices = {}
    
    for url in urls:
        price = get_product_price(url)
        prices[url] = price
    
    # Find the lowest price and corresponding URL
    min_price = min(prices.values())
    min_price_url = [url for url, price in prices.items() if price == min_price][0]
    
    print(f"The lowest price for {product_name} is {min_price} at {min_price_url}")

# Example usage
product_name = "iPhone 12"
urls = [
    "https://www.amazon.com/Apple-iPhone-12-128GB-Black/dp/B08L5TG3ZP",
    "https://www.bestbuy.com/site/apple-iphone-12-128gb-black-verizon/6009933.p",
    "https://www.walmart.com/ip/Apple-iPhone-12-128GB-Black-Verizon-Unlocked/880227184"
]

compare_prices(product_name, urls)
