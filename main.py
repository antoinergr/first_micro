import logging
from flask import Flask

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
    script = """
    <script> console.log("logger") </script>"""
    return "I'm a logger" + script