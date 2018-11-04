# coding:utf8
"""
Created by zhaoguoqing on 18/10/30
"""
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import pymongo
import click

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/zgq'
# mongo = PyMongo(app)

mongo = pymongo.MongoClient('mongodb://localhost:27017/zgq')


@app.route('/')
def index():
    return 'Hello'

@app.route('/json')
def json():
    return jsonify({'name': 'bob', 'age': 13})

@app.route('/book')
def book():
    books = [i for i in mongo['zgq']['douban_book'].find({}, {'_id': 0}).limit(10)]
    return jsonify(books)




