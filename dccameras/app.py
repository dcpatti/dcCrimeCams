# import the Flask class from the flask module
import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify 
from functools import wraps
import sqlite3


app = Flask(__name__)

app.secret_key = "mykey"


camdata = [{'PSA': 101,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 5,
  'TotalClaims': 2,
  'TotalApproved': 1,
  'TotalDecline': 1,
  'TotalCameras': 5,
  'TotalSpend': 750.0},
 {'PSA': 102,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 2,
  'TotalClaims': 3,
  'TotalApproved': 2,
  'TotalDecline': 1,
  'TotalCameras': 2,
  'TotalSpend': 600.0},
 {'PSA': 103,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 7,
  'TotalClaims': 3,
  'TotalApproved': 2,
  'TotalDecline': 17,
  'TotalCameras': 7,
  'TotalSpend': 1157.49},
 {'PSA': 104,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 645,
  'TotalClaims': 319,
  'TotalApproved': 295,
  'TotalDecline': 2,
  'TotalCameras': 645,
  'TotalSpend': 101667.93},
 {'PSA': 105,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 77,
  'TotalClaims': 59,
  'TotalApproved': 51,
  'TotalDecline': 8,
  'TotalCameras': 77,
  'TotalSpend': 14819.14},
 {'PSA': 106,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 239,
  'TotalClaims': 129,
  'TotalApproved': 116,
  'TotalDecline': 10,
  'TotalCameras': 239,
  'TotalSpend': 41058.72},
 {'PSA': 107,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 495,
  'TotalClaims': 253,
  'TotalApproved': 227,
  'TotalDecline': 19,
  'TotalCameras': 495,
  'TotalSpend': 77765.07},
 {'PSA': 108,
  'District': 1,
  'VoucherCams': 0,
  'RebateCams': 756,
  'TotalClaims': 397,
  'TotalApproved': 366,
  'TotalDecline': 6,
  'TotalCameras': 756,
  'TotalSpend': 122896.26},
 {'PSA': 201,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 163,
  'TotalClaims': 97,
  'TotalApproved': 82,
  'TotalDecline': 9,
  'TotalCameras': 163,
  'TotalSpend': 27141.65},
 {'PSA': 202,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 365,
  'TotalClaims': 157,
  'TotalApproved': 139,
  'TotalDecline': 1,
  'TotalCameras': 365,
  'TotalSpend': 55728.37},
 {'PSA': 203,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 88,
  'TotalClaims': 42,
  'TotalApproved': 38,
  'TotalDecline': 7,
  'TotalCameras': 88,
  'TotalSpend': 14047.94},
 {'PSA': 204,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 85,
  'TotalClaims': 56,
  'TotalApproved': 45,
  'TotalDecline': 5,
  'TotalCameras': 85,
  'TotalSpend': 15005.38},
 {'PSA': 205,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 204,
  'TotalClaims': 110,
  'TotalApproved': 96,
  'TotalDecline': 6,
  'TotalCameras': 204,
  'TotalSpend': 32966.05},
 {'PSA': 206,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 167,
  'TotalClaims': 93,
  'TotalApproved': 79,
  'TotalDecline': 2,
  'TotalCameras': 167,
  'TotalSpend': 28351.55},
 {'PSA': 207,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 35,
  'TotalClaims': 19,
  'TotalApproved': 15,
  'TotalDecline': 8,
  'TotalCameras': 35,
  'TotalSpend': 5246.74},
 {'PSA': 208,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 107,
  'TotalClaims': 52,
  'TotalApproved': 44,
  'TotalDecline': 1,
  'TotalCameras': 107,
  'TotalSpend': 16853.42},
 {'PSA': 209,
  'District': 2,
  'VoucherCams': 0,
  'RebateCams': 0,
  'TotalClaims': 1,
  'TotalApproved': 0,
  'TotalDecline': 0,
  'TotalCameras': 0,
  'TotalSpend': 0.0},
 {'PSA': 301,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 113,
  'TotalClaims': 54,
  'TotalApproved': 47,
  'TotalDecline': 2,
  'TotalCameras': 113,
  'TotalSpend': 17908.38},
 {'PSA': 302,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 347,
  'TotalClaims': 175,
  'TotalApproved': 153,
  'TotalDecline': 14,
  'TotalCameras': 347,
  'TotalSpend': 53097.36},
 {'PSA': 303,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 103,
  'TotalClaims': 59,
  'TotalApproved': 50,
  'TotalDecline': 6,
  'TotalCameras': 103,
  'TotalSpend': 16975.01},
 {'PSA': 304,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 129,
  'TotalClaims': 62,
  'TotalApproved': 52,
  'TotalDecline': 10,
  'TotalCameras': 129,
  'TotalSpend': 18519.12},
 {'PSA': 305,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 141,
  'TotalClaims': 78,
  'TotalApproved': 69,
  'TotalDecline': 5,
  'TotalCameras': 141,
  'TotalSpend': 22674.2},
 {'PSA': 306,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 64,
  'TotalClaims': 48,
  'TotalApproved': 32,
  'TotalDecline': 9,
  'TotalCameras': 64,
  'TotalSpend': 9827.61},
 {'PSA': 307,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 74,
  'TotalClaims': 49,
  'TotalApproved': 36,
  'TotalDecline': 9,
  'TotalCameras': 74,
  'TotalSpend': 12539.2},
 {'PSA': 308,
  'District': 3,
  'VoucherCams': 0,
  'RebateCams': 121,
  'TotalClaims': 75,
  'TotalApproved': 64,
  'TotalDecline': 6,
  'TotalCameras': 121,
  'TotalSpend': 19334.6},
 {'PSA': 401,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 257,
  'TotalClaims': 109,
  'TotalApproved': 97,
  'TotalDecline': 5,
  'TotalCameras': 257,
  'TotalSpend': 35217.56},
 {'PSA': 402,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 302,
  'TotalClaims': 131,
  'TotalApproved': 124,
  'TotalDecline': 3,
  'TotalCameras': 302,
  'TotalSpend': 45470.22},
 {'PSA': 403,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 458,
  'TotalClaims': 203,
  'TotalApproved': 187,
  'TotalDecline': 7,
  'TotalCameras': 458,
  'TotalSpend': 69525.08},
 {'PSA': 404,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 499,
  'TotalClaims': 224,
  'TotalApproved': 205,
  'TotalDecline': 11,
  'TotalCameras': 499,
  'TotalSpend': 75610.28},
 {'PSA': 405,
  'District': 4,
  'VoucherCams': 2,
  'RebateCams': 411,
  'TotalClaims': 179,
  'TotalApproved': 158,
  'TotalDecline': 9,
  'TotalCameras': 413,
  'TotalSpend': 58086.73},
 {'PSA': 406,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 242,
  'TotalClaims': 104,
  'TotalApproved': 93,
  'TotalDecline': 9,
  'TotalCameras': 242,
  'TotalSpend': 34734.13},
 {'PSA': 407,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 635,
  'TotalClaims': 328,
  'TotalApproved': 291,
  'TotalDecline': 13,
  'TotalCameras': 635,
  'TotalSpend': 100984.05},
 {'PSA': 408,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 179,
  'TotalClaims': 92,
  'TotalApproved': 81,
  'TotalDecline': 8,
  'TotalCameras': 179,
  'TotalSpend': 29336.23},
 {'PSA': 409,
  'District': 4,
  'VoucherCams': 0,
  'RebateCams': 314,
  'TotalClaims': 153,
  'TotalApproved': 139,
  'TotalDecline': 7,
  'TotalCameras': 314,
  'TotalSpend': 47470.23},
 {'PSA': 501,
  'District': 5,
  'VoucherCams': 0,
  'RebateCams': 616,
  'TotalClaims': 300,
  'TotalApproved': 275,
  'TotalDecline': 23,
  'TotalCameras': 616,
  'TotalSpend': 97607.67},
 {'PSA': 502,
  'District': 5,
  'VoucherCams': 0,
  'RebateCams': 621,
  'TotalClaims': 286,
  'TotalApproved': 256,
  'TotalDecline': 18,
  'TotalCameras': 621,
  'TotalSpend': 94448.55},
 {'PSA': 503,
  'District': 5,
  'VoucherCams': 2,
  'RebateCams': 598,
  'TotalClaims': 260,
  'TotalApproved': 236,
  'TotalDecline': 15,
  'TotalCameras': 600,
  'TotalSpend': 85155.03},
 {'PSA': 504,
  'District': 5,
  'VoucherCams': 0,
  'RebateCams': 480,
  'TotalClaims': 204,
  'TotalApproved': 190,
  'TotalDecline': 9,
  'TotalCameras': 480,
  'TotalSpend': 69927.3},
 {'PSA': 505,
  'District': 5,
  'VoucherCams': 0,
  'RebateCams': 116,
  'TotalClaims': 55,
  'TotalApproved': 47,
  'TotalDecline': 4,
  'TotalCameras': 116,
  'TotalSpend': 17658.66},
 {'PSA': 506,
  'District': 5,
  'VoucherCams': 2,
  'RebateCams': 390,
  'TotalClaims': 174,
  'TotalApproved': 157,
  'TotalDecline': 14,
  'TotalCameras': 392,
  'TotalSpend': 58563.72},
 {'PSA': 507,
  'District': 5,
  'VoucherCams': 0,
  'RebateCams': 516,
  'TotalClaims': 248,
  'TotalApproved': 223,
  'TotalDecline': 18,
  'TotalCameras': 516,
  'TotalSpend': 84081.1},
 {'PSA': 601,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 96,
  'TotalClaims': 60,
  'TotalApproved': 47,
  'TotalDecline': 11,
  'TotalCameras': 96,
  'TotalSpend': 15525.42},
 {'PSA': 602,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 193,
  'TotalClaims': 76,
  'TotalApproved': 65,
  'TotalDecline': 7,
  'TotalCameras': 193,
  'TotalSpend': 24577.61},
 {'PSA': 603,
  'District': 6,
  'VoucherCams': 4,
  'RebateCams': 191,
  'TotalClaims': 83,
  'TotalApproved': 71,
  'TotalDecline': 8,
  'TotalCameras': 195,
  'TotalSpend': 27121.23},
 {'PSA': 604,
  'District': 6,
  'VoucherCams': 4,
  'RebateCams': 205,
  'TotalClaims': 122,
  'TotalApproved': 100,
  'TotalDecline': 13,
  'TotalCameras': 209,
  'TotalSpend': 31822.3},
 {'PSA': 605,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 206,
  'TotalClaims': 85,
  'TotalApproved': 70,
  'TotalDecline': 12,
  'TotalCameras': 206,
  'TotalSpend': 28366.32},
 {'PSA': 606,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 136,
  'TotalClaims': 51,
  'TotalApproved': 41,
  'TotalDecline': 9,
  'TotalCameras': 136,
  'TotalSpend': 15982.72},
 {'PSA': 607,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 115,
  'TotalClaims': 53,
  'TotalApproved': 41,
  'TotalDecline': 6,
  'TotalCameras': 115,
  'TotalSpend': 15688.21},
 {'PSA': 608,
  'District': 6,
  'VoucherCams': 0,
  'RebateCams': 184,
  'TotalClaims': 74,
  'TotalApproved': 60,
  'TotalDecline': 10,
  'TotalCameras': 184,
  'TotalSpend': 22366.76},
 {'PSA': 701,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 259,
  'TotalClaims': 101,
  'TotalApproved': 91,
  'TotalDecline': 6,
  'TotalCameras': 259,
  'TotalSpend': 33974.98},
 {'PSA': 702,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 71,
  'TotalClaims': 30,
  'TotalApproved': 26,
  'TotalDecline': 2,
  'TotalCameras': 71,
  'TotalSpend': 9390.19},
 {'PSA': 703,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 70,
  'TotalClaims': 41,
  'TotalApproved': 34,
  'TotalDecline': 7,
  'TotalCameras': 70,
  'TotalSpend': 11330.88},
 {'PSA': 704,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 151,
  'TotalClaims': 71,
  'TotalApproved': 65,
  'TotalDecline': 5,
  'TotalCameras': 151,
  'TotalSpend': 21086.39},
 {'PSA': 705,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 87,
  'TotalClaims': 43,
  'TotalApproved': 38,
  'TotalDecline': 2,
  'TotalCameras': 87,
  'TotalSpend': 13686.9},
 {'PSA': 706,
  'District': 7,
  'VoucherCams': 2,
  'RebateCams': 33,
  'TotalClaims': 20,
  'TotalApproved': 15,
  'TotalDecline': 4,
  'TotalCameras': 35,
  'TotalSpend': 5043.7},
 {'PSA': 707,
  'District': 7,
  'VoucherCams': 0,
  'RebateCams': 91,
  'TotalClaims': 34,
  'TotalApproved': 25,
  'TotalDecline': 7,
  'TotalCameras': 91,
  'TotalSpend': 9725.25},
 {'PSA': 708,
  'District': 7,
  'VoucherCams': 2,
  'RebateCams': 83,
  'TotalClaims': 41,
  'TotalApproved': 37,
  'TotalDecline': 4,
  'TotalCameras': 85,
  'TotalSpend': 12050.12}]


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(camexpense2.sqlite)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_data(conn):
    """
    Query all rows in the  table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM cam_psa")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

# login required decorator
def login_required(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/dataviz')
def dataviz():
    return render_template('dataviz.html')  

@app.route('/datatable')
def datatable():
   con = sqlite3.connect("camexpense2.sqlite")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from cam_psa")
   
   rows = cur.fetchall()
   return render_template("datatable.html",rows = rows)

# def datatable():
#     return render_template('datatable.html')

   

@app.route('/maps')
def maps():
    return render_template('maps.html') 

@app.route('/maplarge')
def maplarge():
    return render_template('maplarge.html') 

@app.route('/api')
def api():
    return (
        f"<h1>Welcome to the DCcamerAPI!</h1><br/>"
        f"<strong><u>Available Routes:</u></strong><br/>"
        f"/api/v1.0/dc-cameras<br/>"
        f"<br/>"
        f"<strong>PSAs:</strong><br/>"
        f"/api/v1.0/dc-cameras/psa/101<br/>"
        f"to<br/>"
        f"/api/v1.0/dc-cameras/psa/708<br/>"
        f"<br/>"
        f"<strong>Districts:</strong><br/>"
        f"/api/v1.0/dc-cameras/district/1<br/>"
        f"to<br/>"
        f"/api/v1.0/dc-cameras/district/7<br/>"
    )

@app.route("/api/v1.0/dc-cameras")
def dccameras():
    return jsonify(camdata)

@app.route("/api/v1.0/dc-cameras/psa/<psa>")
def dcpsa(psa):

    canonicalized = psa.replace(" ", "").lower()
    for PSA in camdata:
        search_term = str(PSA["PSA"])
        
        if search_term == canonicalized:
            return jsonify(PSA)

    return jsonify({"error": f"PSA #{psa} not found."}), 404

@app.route("/api/v1.0/dc-cameras/district/<district>")
def dcdistrict(district):

    canonicalized = district.replace(" ", "").lower()
    for district_no in camdata:
        search_term = str(district_no["District"])
        
        if search_term == canonicalized:
            return jsonify(district_no)

    return jsonify({"error": f"District #{district} not found."}), 404

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash("You were just logged in!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
   session.pop('logged_in', None)
   flash("You were just logged out.")
   return redirect(url_for('welcome'))


# start the server with the 'run()' method

if __name__ == "__main__":
    app.run(debug=True)