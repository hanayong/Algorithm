# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import re
import pprint

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.word_set
collection = db.word
num = 0


@app.route('/')
def main():
    return render_template('myPage.html')


@app.route('/searching', methods=['POST', 'GET'])
def searching(word=None):
    global num
    if request.method == 'POST':
        word = request.form['word']
        insert(word)
    # collection.delete_many({})
    return render_template('myPage.html', word=word)


def insert(word: str) -> object:
    word_dict = {}
    global num
    regex = re.compile('[a-zA-Z]+')
    if regex.search(word) is None:
        return
    word_dict[str(num)] = word
    collection.insert(word_dict)
    num += 1
    # express(word_dict)
    return redirect('/')


def express(word_dict):
    doc_list = collection.find()
    for i in doc_list:
        pprint.pprint(i)


if __name__ == '__main__':
    app.run(debug=True)
