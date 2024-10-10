from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file
csv_file = 'news_articles.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file)

# Convert DataFrame to a list of dictionaries (for easy JSON serving)
articles = df.to_dict(orient='records')

# Endpoint 1: Get all articles, with optional filtering by category
@app.route('/articles', methods=['GET'])
def get_articles():
    category = request.args.get('category')
    
    # Filter by category if the category query param is provided
    if category:
        filtered_articles = [article for article in articles if article['category'] == category]
        return jsonify(filtered_articles)
    
    # Return all articles if no filter is provided
    return jsonify(articles)

# Endpoint 2: Get a specific article by id (index in CSV)
@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    if id < len(articles):
        return jsonify(articles[id])
    else:
        return jsonify({"error": "Article not found"}), 404

# Endpoint 3: Search articles by keywords
@app.route('/search', methods=['GET'])
def search_articles():
    query = request.args.get('q', '').lower()
    if query:
        results = [article for article in articles if query in article['summary'].lower() or query in article['title'].lower()]
        return jsonify(results)
    return jsonify([])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
