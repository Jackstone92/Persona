import os

from flask import Blueprint, render_template

frontend = Blueprint('frontent', __name__)


@frontend.route('/', methods=['GET'])
@frontend.route('/all-personas', methods=['GET'])
def get_index():
    return render_template('index.html')
