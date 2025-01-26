import requests
from twilio.rest import Client
import os

# Stock and company details
STOCK = "MIDD"  # Stock symbol to track
COMPANY_NAME = "Middleby"  # Company name for fetching relevant news

# Twilio credentials (replace with environment variables for security)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
auth_token = os.getenv("TWILIO_AUTH_TOKEN")  # Twilio Auth Token

# API endpoints and keys (replace with environment variables for security)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # Stock price API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # News API
STOCK_APIKEY = os.getenv("STOCK_API_KEY")  # API key for stock price
NEWS_APIKEY = os.getenv("NEWS_API_KEY")  # API key for news


# Function to calculate stock price change percentage between yesterday and the day before
def stock_price_change(stk=STOCK):
    """
    Fetches daily stock data and calculates the percentage change in closing price
    between yesterday and the day before.
    """
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stk,
        "apikey": STOCK_APIKEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    stock_data = response.json()["Time Series (Daily)"]
    stock_data = [value for (key, value) in stock_data.items()]

    # Get closing prices for yesterday and the day before
    y_stock_close = float(stock_data[0]['4. close'])
    dby_stock_close = float(stock_data[1]['4. close'])

    # Calculate and return the percentage change
    return round(((y_stock_close - dby_stock_close) / dby_stock_close) * 100, 2)


# Function to fetch top 3 news articles for the company
def stock_news(cmpy=COMPANY_NAME):
    """
    Fetches top 3 news articles related to the given company, sorted by popularity.
    """
    news_params = {
        "apiKey": NEWS_APIKEY,
        "qInTitle": cmpy,
        "sortBy": "popularity"
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()

    # Extract headlines and descriptions for top 3 articles
    top_headlines = []
    top_description = []
    for i in range(min(int(news_data['totalResults']), 3)):
        headlines = news_data['articles'][i]['title']
        description = news_data['articles'][i]['description']
        top_headlines.append(headlines)
        top_description.append(description)

    # Return news as a list of tuples
    return [(top_headlines[i], top_description[i]) for i in range(len(top_headlines))]


# Check stock price change and send a WhatsApp message if change exceeds 5%
percentage_change = stock_price_change(stk=STOCK)
if abs(percentage_change) >= 5:
    news = stock_news(cmpy=COMPANY_NAME)
    client = Client(account_sid, auth_token)

    # Format the message with stock percentage change and news articles
    formatted_msg = f""" {STOCK}: {"🔻" if percentage_change < 0 else "🔺"}{percentage_change}%\n\n"""
    for headline, brief in news:
        formatted_msg += f"Headline: {headline}\nBrief: {brief}\n\n"

    # Send WhatsApp message (replace 'to' phone number with the recipient's number)
    message = client.messages.create(
        body=formatted_msg,
        from_='whatsapp:+14155238886',  # Twilio sandbox WhatsApp number
        to='whatsapp:+1234567890'  # Replace with recipient's WhatsApp number
    )
    print(message.status)
