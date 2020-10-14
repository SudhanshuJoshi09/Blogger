from app import app
from flask import render_template, url_for, request, redirect
from models import db, create_article, Article, search_articles
import json


# Create New Articles.
@app.route('/new_article', methods=['GET', 'POST'])
def new_page():
    message = 'Add a new article'
    if request.method == 'POST':
        topic = request.form['topic']
        # topic = request.form.get('topic')  --Alternative
        tags = request.form['tags']
        # tags = request.form.get('tags')  --Alternative
        details = request.form['details']
        # details = request.form.get('details')  --Alternative

        art_id = create_article(topic, tags, details)
        return redirect(url_for('display_page', message=art_id))

    return render_template('new_article.html', message = '')


# Display Created article.
@app.route('/display_article/<message>')
def display_page(message):
    article = Article.query.filter_by(id = int(message)).all()
    article = article[0]
    topic = article.topic
    tags = json.loads(article.tags)
    details = article.details
    return render_template('display_article.html', topic = topic,
                            tags = tags, details = details)


# Alternative search results.
@app.route('/search_article/<token>')
def alternate_search_results(token):
    results, found = search_articles(token)
    print(results)
    return render_template('display_results.html', results=results)


# Search Article by tags.
@app.route('/search_article', methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        token = request.form['token']
        results, found = search_articles(token)
        if found == True:
            return render_template('display_results.html', results=results)
        else:
            return render_template('alternate_results.html', results=results)

    return render_template('search_results.html')
