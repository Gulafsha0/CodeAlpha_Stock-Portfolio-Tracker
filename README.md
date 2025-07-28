# CodeAlpha_Stock-Portfolio-Tracker

✅ TASK 2: Stock Portfolio Tracker

This project is a simple stock tracker that allows users to input stock holdings and calculates their total investment based on predefined stock prices.

📝 Introduction

The *Stock Portfolio Tracker* is a beginner-friendly Python project designed to simulate how investment tracking works. Instead of using real-time APIs or market data, this version uses a *hardcoded dictionary* of stock prices for simplicity. The program collects stock names and quantities from the user, calculates the total value of the portfolio, and optionally saves the results to a .txt or .csv file.

This project was created as part of the *[CodeAlpha Internship Program](https://codealpha.tech)*.

🎯 Objective

- To build a console-based application that tracks stock investments.
- To practice using dictionaries, user input/output, arithmetic operations, and basic file handling.
- To simulate stock tracking logic in a simplified environment without using external data sources.

📖 Explanation

- The program begins with a predefined dictionary of stock prices:

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "MSFT": 310
}
