#coding: utf-8

from . import {{ h5blueprint }}
from flask import render_template, request

@{{ h5blueprint }}.route('/')
def index():
    platform = request.user_agent.platform
    if platform in ["android", "iphone", "ipad"]:
        return render_template('{{ h5blueprint }}_index_m.html')
    else:
        return render_template('{{ h5blueprint }}_index_d.html')
