#!/usr/bin/env python
# encoding: utf-8

import os
from jinja2 import Environment, PackageLoader, TemplateNotFound
from sanic import Blueprint
from sanic.response import html


current_directory = os.path.dirname(os.path.realpath(__file__))
static_directory = os.path.join(current_directory, 'static')
env = Environment(loader=PackageLoader('tbone_admin', 'templates'))
bp = Blueprint('admin', url_prefix='/admin')
bp.static('/static', static_directory, name='static')


@bp.route('/', methods=['GET'])
async def index(request):
    try:
        template = env.get_template('index.html')
    except TemplateNotFound:
        raise TemplateNotFound('index.html')

    content = template.render()
    return html(content)
