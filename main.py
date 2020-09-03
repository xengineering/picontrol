#!/usr/bin/python3


"""
    picontrol - A small Web Application to shutdown or reboot your Raspberry Pi.

    Copyright (C) 2020  xengineering

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from waitress import serve
from flask import Flask, render_template, current_app


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/css/<css_file>')
def css(css_file):
    return current_app.send_static_file("css/{}".format(css_file))


@app.route('/favicon.ico')
def favicon():
    return current_app.send_static_file("img/favicon.ico")


if __name__ == '__main__':
    serve(app, listen='*:8080')  # production server / bind to port
    #serve(app, unix_socket='/run/web-template/unix.sock')  # production server / unix domain socket
    #app.run()  # debug server - NOT FOR PRODUCTION!
