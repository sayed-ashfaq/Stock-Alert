# Stock-Alert
## Stock Price Change Alert System with News and Messaging Integration

This project is a Python-based application that monitors the stock price of a specified company. If a significant change in stock price is detected, the system fetches the latest news articles about the company and sends an alert via WhatsApp.

## Features
- Tracks stock price changes using the Alpha Vantage API.
- Fetches the latest news articles using the NewsAPI.
- Sends formatted alerts via WhatsApp using Twilio.

## Skills Demonstrated
- API Integration: Implemented Alpha Vantage, NewsAPI, and Twilio API.
- Python Programming: Leveraged Python for handling HTTP requests, JSON data parsing, and automated workflows.
- Data Handling: Processed real-time stock and news data.
- Messaging Automation: Automated sending of alerts with dynamic data.

## Tech Stack
- **Programming Language**: Python
- **APIs Used**:
  - Alpha Vantage (Stock Market Data)
  - NewsAPI (News Articles)
  - Twilio (WhatsApp Messaging)

## Workflow
1. **Monitor Stock Prices**:
   - Fetch daily stock prices for the specified company.
   - Calculate the percentage change between the last two closing prices.
2. **Fetch News Articles**:
   - If the stock price change exceeds the defined threshold (5%), fetch the top three news articles related to the company.
3. **Send Alerts**:
   - Send an alert message via WhatsApp, including the stock price change and news article details.

## Code Highlights
- **Stock Price Calculation**:
   - Extracts daily stock price data and calculates the percentage change.
- **Dynamic News Retrieval**:
   - Fetches and formats the most relevant news articles for the company.
- **Automated Alerts**:
   - Sends a detailed WhatsApp message summarizing the stock price change and news articles.

## Usage
Clone the repository, install the required Python libraries, and run the script to receive stock price alerts.
