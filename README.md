# news-aggregator

Project Overview
This project is a News Aggregator that scrapes articles from various news sources (such as BBC) and serves them through a REST API built with Flask. It allows users to retrieve all articles, filter them by category, view specific articles by ID, and search articles by keywords. The articles are also saved in a CSV file for persistence.

Features
Scrapes news articles from BBC News
REST API to retrieve and filter articles
Search functionality for articles by keywords
Data stored in CSV format
Flask-based backend serving JSON responses
Endpoints
The REST API includes the following endpoints:

1. Get All Articles (with optional category filter)
Endpoint: /articles

Method: GET

Description: Retrieve all articles. You can also filter articles by category using the category query parameter.
2. Get Article by ID
Endpoint: /articles/{id}

Method: GET

Description: Retrieve a specific article by its ID
3. Search Articles by Keyword
Endpoint: /search

Method: GET

Description: Search for articles that contain specific keywords in the title or summary.

Prerequisites
To run this project, you need to have the following installed:

Python 3.x
pip (Python package installer)

Setup Instructions
Clone the repository:

git clone https://github.com/Nikitapalakodeti/news-aggregator.git
cd news-aggregator

Create a virtual environment:
python -m venv .venv
source .venv/bin/activate   # On Windows, use .venv\Scripts\activate

Install the required packages:
pip install -r requirements.txt

Run the Flask app:
python app.py

Dependencies
The following Python libraries are required to run this project:

Flask
requests
beautifulsoup4
pandas
nltk
gensim
These are included in the requirements.txt file. Install them by running pip install -r requirements.txt.
