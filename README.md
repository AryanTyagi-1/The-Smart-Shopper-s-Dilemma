# The-Smart-Shopper-s-Dilemma
We are building a system for a smart shopping assistant. A user types in a product name — say, “365 WholeFoods Peanut Butter”. They expect our system to instantly fetch all relevant product cards from Google Shopping: product name, brand, price, and total weight.
# Smart Shopper’s Django API
Get real-time product data (name, brand, price, weight) from Google Shopping by querying a single API endpoint. High performance with async scraping and caching.
# Features of Django API 
* Asynchronous web scraping for low-latency results.
* Caching of frequent queries for instant responses.
* REST API interface: any client can fetch product data.
* Easily extensible for new e-commerce targets
# Prerequisites :
* Python 3.13 : We can use Python 3.10 +
* pip
* Redis : We are using it  for production caching
* Chrome : if using Playwright or selenium for scraping That's why chrome 

# Setup instructions 
1.  Clone the Repository
git clone https://github.com/<your-username>/smart_shopper_django.git
cd smart_shopper_django.
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate. 
3. Install Dependencies
pip install -r requirements.txt
Sample requirements.txt:
Django>=4.2
httpx[http2]
lxml
uvicorn
* Optionally, for browser scraping:
playwright
* For caching:
django-redis
(Optional, for Playwright)
playwright install
4. Run Migrations
python manage.py migrate
5. Configuration
Redis Caching 
Configure Django cache settings in settings.py:
  
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
We can start with our Reddis Server if it  is available.

# Run the Server Instructions 
1. With async support, run the server using Uvicorn:
uvicorn smart_shopper.asgi:application

Standard Django run (slower, debugging only):
python manage.py runserver.

# Example Output :
 json
{
  "results": [
    {
      "name": "365 WholeFoods Peanut Butter",
    "brand": "365 by Whole Foods Market",
      "price": "$4.99",
      "weight": "16 oz"
    },
    ...
  ]
}





