from flask_sqlalchemy import SQLAlchemy
from app import app
from spell_check import check2
import json


# Setting Up Config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)


# Creating Article Table
class Article(db.Model):
    id = db.Column('article_id', db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    tags = db.Column(db.String(200))
    details = db.Column(db.String(100))

    def __init__(self, topic, tags, details):
        self.topic = topic
        self.tags = json.dumps(tags)
        self.details = details


# Creating Model Table
class Model(db.Model):
    id = db.Column('model_id', db.Integer, primary_key=True)
    model_name = db.Column(db.String(20))
    # model_desc = db.Column(db.String(200))

    def __init__(self, model_name):
        self.model_name = model_name
        # self.model_desc = model_desc


# Login Model
class Users(db.Model):
    id = db.Column('model_id', db.Integer, primary_key=True)
    email_id = db.Column(db.String(20))
    password = db.Column(db.String(20))
    user_name = db.Column(db.String(20))

    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password
        self.user_name = ''

        for character in email_id:
            if character == '@':
                break
            self.user_name += character


# Initializing Database.
db.create_all()


# Formating Tags.
def formated_tags(tag_list):
    temp_list = tag_list.split(',')
    new_tags = []
    for tags in temp_list:
        mod_tags = ''
        if tags == '':
            continue
        count = 0
        for i in range(len(tags)):
            if tags[i] != ' ':
                break
            count += 1

        for i in range(count, len(tags)):
            if tags[i] == ' ':
                break
            mod_tags += tags[i]
        new_tags.append(mod_tags)

    return new_tags


# To lower
def to_lower(topic, tags, details):
    return topic.lower(), tags.lower(), details.lower()


# Function to create new article
def create_article(topic, tags, details):
    topic, tags, details = to_lower(topic, tags, details)
    tags = formated_tags(tags)
    topic_tokenizer(topic)

    model_tags = tags
    for temp_tag in model_tags:
        new_model = Model(temp_tag)
        db.session.add(new_model)

    temp_article = Article(topic, tags, details)
    db.session.add(temp_article)
    db.session.commit()

    article = Article.query.filter_by(topic=topic).all()
    return article[0].id


# Creating new
# def create_account(email_id,

# Optimized Article Search
def optimized_search(token):
    token = formated_tags(token)
    result = []
    for article in Model.query.all():
        tag = article.model_name
        if check2(tag, token):
            result.append(tag)
    return result


# Function for searching articles.
def search_articles(token):
    result = []
    found = False
    token = formated_tags(token)
    token = token[0]

    for article in Article.query.all():
        tags_list = article.tags
        tags_list = json.loads(tags_list)

        for tag in tags_list:
            if tag == token:
                article_pack = []
                article_pack.append(article.topic)
                article_pack.append(tags_list)
                article_pack.append(article.details)
                result.append(article_pack)
                found = True
                break

    if found:
        return result, True
    val = optimized_search(token)
    return val, False


# topic tokenizer
def topic_tokenizer(topic):
    mod_topic = topic.split(' ')
    print(mod_topic)


# special character truncation
def special_char_trunc(topic):
    return ''.join(e for e in topic if e.isalnum())
