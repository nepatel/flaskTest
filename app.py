from flask import Flask, request, url_for, render_template, jsonify
from oauth2client.service_account import ServiceAccountCredentials
import os, gspread, json

app = Flask(__name__)
@app.route('/')
def testApp():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    
    # read env data
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    credentials_raw = json.loads(credentials_raw);
 
    #credentials = ServiceAccountCredentials.from_json_keyfile_dict(all_creds, scope)
    
    #gc = gspread.authorize(credentials)

    crime_Dict = {
                    "crimes": [
                        {
                            "crime": "unauthorized entry",
                            "count": 0
                        },
                        {
                            "crime": "marijuana",
                            "count": 0
                        },
                        {
                            "crime": "controlled substance",
                            "count": 0
                        },
                        {
                            "crime": "drug paraphernalia",
                            "count": 0
                        },
                        {
                            "crime": "underage consumption",
                            "count": 0
                        },
                        {
                            "crime": "poss. of alcohol",
                            "count": 0
                        },
                        {
                            "crime": "golf cart",
                            "count": 0
                        },
                        {
                            "crime": "assault",
                            "count": 0
                        },
                        {
                            "crime": "rape",
                            "count": 0
                        },
                        {
                            "crime": "breaking and entering",
                            "count": 0
                        },
                        {
                            "crime": "larceny",
                            "count": 0
                        },
                        {
                            "crime": "injury",
                            "count": 0
                        },
                        {
                            "crime": "vehicle",
                            "count": 0
                        },
                        {
                            "crime": "traffic stop",
                            "count": 0
                        },
                        {
                            "crime": "fondling",
                            "count": 0
                        },
                        {
                            "crime": "scam",
                            "count": 0
                        },
                        {
                            "crime": "trespass",
                            "count": 0
                        },
                        {
                            "crime": "suspicious",
                            "count": 0
                        },
                        {
                            "crime": "fraud",
                            "count": 0
                        },
                        {
                            "crime": "forgery",
                            "count": 0
                        },
                        {
                            "crime": "vandalism",
                            "count": 0
                        },
                        {
                            "crime": "hit and run",
                            "count": 0
                        },
                        {
                            "crime": "traffic crash",
                            "count": 0
                        }
                        ]}

    #return jsonify(crime_Dict)
    return jsonify(credentials_raw)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run('localhost', port)
