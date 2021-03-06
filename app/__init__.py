#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Author: huxuan <i(at)huxuan.org>
Description: Initial file for app.
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object('config')

db = SQLAlchemy(app)

from app import models


@app.route('/')
@app.route('/hellworld')
def helloworld():
    """ Hello World for app. """
    return 'Hello world from {}!'.format(__name__)
