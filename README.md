# Stock-Alert-System
"Stock News Alert System": A Python project that sends SMS alerts with stock price changes and related news articles using Alpha Vantage, NewsAPI, and Twilio APIs.

# Stock News Alert System

## Introduction

This Python project fetches stock data and news articles related to a specific company and sends an alert via SMS using Twilio when the stock price increases or decreases by 2% or more compared to the previous day's closing price.

## Requirements

To run this project, you need the following:

- Python (3.7 or later)
- Twilio Account SID and Auth Token
- Alpha Vantage API key
- NewsAPI key

## Setup

1. Clone this repository to your local machine.

2. Install the required Python libraries using pip:

3. Obtain the following credentials:

- Twilio Account SID and Auth Token: Create a Twilio account (https://www.twilio.com/) and get your SID and Auth Token from the Twilio Console.

- Alpha Vantage API key: Sign up for a free account on Alpha Vantage (https://www.alphavantage.co/) to get your API key.

- NewsAPI key: Register for a free API key on NewsAPI (https://newsapi.org/) to access news articles.

4. Set up environment variables for the API keys:

- For Alpha Vantage API key, add it as an environment variable named `API_KEY`.

- For the Twilio credentials, set the following environment variables:

- Replace `YOUR_TWILIO_ACCOUNT_SID`, `YOUR_TWILIO_AUTH_TOKEN`, `YOUR_VIRTUAL_TWILIO_NUMBER`, and `YOUR_VERIFIED_PHONE_NUMBER` with your Twilio account details.

5. Run the Python script:
## How it Works

1. The script fetches the closing stock prices for the current day and the previous day using the Alpha Vantage API.

2. It calculates the percentage difference in price between the two days.

3. If the percentage difference is greater than or equal to 0.8 (5% increase/decrease), it fetches news articles related to the specified company from NewsAPI.

4. It formats the article headlines and descriptions.

5. The script uses Twilio to send each article as a separate SMS to the specified phone number.

## Note

- The Alpha Vantage and NewsAPI keys are sensitive information. Make sure to keep them secure and avoid sharing them publicly.

- This project assumes that you have already set up a Twilio account and verified your phone number to receive SMS.

- Remember to respect the usage limits of the APIs to avoid any issues with rate limiting.

- This project is for educational purposes and does not provide financial advice. Use it responsibly and at your own







