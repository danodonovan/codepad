#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
@app.route('/<id>')
def appview(id=None):
    return render_template('appview.html', id=id)


@app.route('/recv/<id>', methods=["PUT"])
def applisten(id):
    print("read id {0}".format(id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
