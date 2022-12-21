import logging
from flask import Flask, render_template

import requests

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZFXZZQTC1P"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-ZFXZZQTC1P');
    </script>"""
    return prefix_google + "i love Carbonara"


@app.route('/logger', methods=["GET"])
def logger():
    app.logger.warning('testing ')
    script="""
     <script>console.log("Is that a log?")</script>
    <input type="text" id="name" name="name" required placeholder = "hello Luiz">
    """
    return script

@app.route('/cookie', methods=['GET', 'POST'])
def cookie():
    req=requests.get('https://www.google.com/')
    return req.cookies.get_dict()

@app.route('/cookie/analytics', methods=['GET', 'POST'])
def cookie_analytics():
    req=requests.get('https://analytics.google.com/analytics/web/#/p345039963/reports/intelligenthome')
    return req.text