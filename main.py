"""Stock News Alert System """
#----------------------------------------------------------------------------#
__author__ = "Alister D'souza"
__copyright__ = " Copyright (C) 2007 Free Software Foundation, Inc."
__credits__ = " Stack Overflow "
__license__ = "GNU"
__version__ = "1.0.1"
__maintainer__ = "Alister D'souza"
__email__ = "alisterdsouzaa@outlook.com"
__status__ = "Release"
#-----------------------------------------------------------------------------#

# Import necessary libraries
from datetime import date, timedelta
from twilio.rest import Client
import os
import requests

# Constants for the project
STOCK_NAME = "TSLA"  # Stock symbol for Tesla Inc.
COMPANY_NAME = "Tesla Inc"  # Company name for news filtering

STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # API endpoint for stock data
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # API endpoint for news data

# Replace the following with your Twilio account details
TWILIO_SID = ""  # Your Twilio account SID
TWILIO_AUTH_TOKEN = ""  # Your Twilio account authentication token
VIRTUAL_TWILIO_NUMBER = ""  # Your Twilio virtual number
VERIFIED_NUMBER = ""  # Your verified phone number to receive messages

# Get today and yesterday's dates
today = date.today()
yesterday = today - timedelta(days=1)
print(today)
print(yesterday)

# Fetch Alpha Vantage API key from environment variable, if not found use default value
# I have set my API Key in environment variables
STOCK_DATA_API_KEY = os.getenv("API_KEY", default="No Environment Key found")

# Alpha Vantage API requires API key to access the data
STOCK_NEWS_DATA_API_KEY = "" # Your API KEY for News Data

# Create parameters for getting yesterday's stock data using Alpha Vantage API
paramaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_DATA_API_KEY,
}

# Send a GET request to Alpha Vantage API to get yesterday's stock data
response = requests.get(url=STOCK_ENDPOINT, params=paramaters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# Extract the list of stock data from the response dictionary
stock_data_list = [value for (key, value) in stock_data.items()]

# Get yesterday's closing stock price
yesterday_data = stock_data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterdays_data = stock_data_list[1]
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]
print(day_before_yesterdays_closing_price)

# Calculate the difference between yesterday's and the day before yesterday's closing stock prices
difference = abs(float(yesterdays_closing_price) - float(day_before_yesterdays_closing_price))
print(difference)

# Calculate the percentage difference in price between yesterday and the day before yesterday
percentage_difference = (difference / float(yesterdays_closing_price)) * 100
print(percentage_difference)

# Check if the percentage difference is greater than or equal to 2
# 2% can be increased or decreased.
if percentage_difference >= 2:
    # Create parameters for getting news related to the company name from NewsAPI
    news_api_parameters = {
        "apiKey": STOCK_NEWS_DATA_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    # Send a GET request to NewsAPI to get news articles related to the company
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_api_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # Get the first 3 articles using Python slice operator
    first_3_articles = articles[:3]
    print(first_3_articles)

    # Format the articles' headlines and descriptions
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}"
                          for article in first_3_articles]

    # Initialize Twilio client to send SMS
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
