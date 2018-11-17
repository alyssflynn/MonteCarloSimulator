'''
NOTES
-----
- bootstrapped code from flask docs (http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)
'''

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# from werkzeug.utils import secure_filename
# import keras
# from keras.preprocessing import image
# from keras import backend as K

import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb  
import matplotlib.pyplot as plt  
from scipy.stats import norm
# %matplotlib inline
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from monte_carlo import plotstock, pyplotstock

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    defaultData = plotstock(ticker='PG', time_intervals=1000, iterations=10, start='2007-1-1')
    # defaultData = pyplotstock(ticker='PG', time_intervals=1000, iterations=10, start='2007-1-1')
    return render_template("index.html", plot_data=defaultData, title='Default')

@app.route('/<ticker>/<start>/<end>')
def render_plot(ticker, start, end):
    # embedData = plotstock(ticker=ticker, time_intervals=1000, iterations=10, start=start)
    embedData = pyplotstock(ticker=ticker, time_intervals=1000, iterations=10, start=start)
    return render_template('index.html', plot_data=embedData, title='title')

if __name__ == "__main__":
    app.run(debug=True)
