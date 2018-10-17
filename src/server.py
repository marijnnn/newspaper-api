#!/usr/bin/env python

from flask import Flask, jsonify, request
from newspaper import Article
import os

app = Flask(__name__)
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return 'Analyze webservice is running!'

@app.route('/analyze',  methods=['POST'])
def analyse():
    article = Article('')
    article.set_html(html=request.data)
    article.parse()
    return jsonify(source_url=article.source_url,
        url=article.url,
        title=article.title,
        top_img=article.top_img,
        meta_img=article.meta_img,
        imgs=list(article.imgs),
        movies=article.movies,
        text=article.text,
        keywords=article.keywords,
        meta_keywords=article.meta_keywords,
        tags=list(article.tags),
        authors=article.authors,
        publish_date=article.publish_date,
        summary=article.summary,
        article_html=article.article_html,
        meta_description=article.meta_description,
        meta_lang=article.meta_lang,
        meta_favicon=article.meta_favicon,
        meta_data=article.meta_data,
        canonical_link=article.canonical_link,
        additional_data=article.additional_data)

if __name__ == '__main__':
    port = os.getenv('NEWSPAPER_PORT', '38765')
    app.run(port=int(port), host='0.0.0.0')
