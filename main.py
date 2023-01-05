import logging
from flask import Flask, render_template


from pytrends.request import TrendReq
pytrends = TrendReq(hl='fr', tz=360)

import requests
import pandas as pd
import numpy as np

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


@app.route('/trends',methods = ['GET', 'POST'])
def trend():
    kw=['Lionel Messi']
    df=pytrends.get_historical_interest(kw, year_start=2022, 
        month_start=10, day_start=1,  
        year_end=2022, month_end=12, day_end=31, 
        cat=0, geo='FR', gprop='', sleep=0).reset_index()
    df['date']=pd.to_datetime(df['date'])
    df=df.resample('D', on='date').mean()
    df['Lionel Messi'] = df['Lionel Messi'].fillna(0)
    line_labels = df.index.strftime("%m/%d/%Y").tolist()
    line_values = df['Lionel Messi'].tolist()
    return render_template('chart.html', labels=line_labels, values=line_values)

if __name__ == "__main__":
    app.run(debug=True)