# coding:utf8
"""
Created by zhaoguoqing on 18/10/30
"""
from flask import Flask, jsonify
import click

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/json')
def json():
    return jsonify({'name': 'bob', 'age': 13})

@app.cli.command()
def cmd_test():
    click.echo('cmd test.')



