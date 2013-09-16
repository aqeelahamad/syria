import sys
import re
import os
import requests
import jinja2
from requests_oauthlib import OAuth1
from flask import render_template
from flask import Flask

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')



app = Flask('myapp', template_folder=tmpl_dir)
app = Flask(__name__)

BASE_URL = u'https://api.twitter.com/1.1/'

client_key = u'h1T9MORP5zGidpXlibAtA'
client_secret = u'3duWKMwMmnHfPbZPjfSqyEMNnFi1mWEUXUP24QgpE'
resource_owner_key = u'1746056306-LW4UXRxp0qjtij57gXrYkDX5Uy4ANFQyMxoHD2B'
resource_owner_secret = u'rFxMKOaonqWnVpdw3K0p2CoLiWwLfdVFOpA5RlzDcw'

oauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret)

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')


queryoauth = OAuth1(client_key, client_secret,
                    resource_owner_key, resource_owner_secret,
                    signature_type='query')


bodyoauth = OAuth1(client_key, client_secret,
                   resource_owner_key, resource_owner_secret,
                   signature_type='body')
                   
@app.route('/')			   
def sy():
	payload = {'q': 'syria','count':5}
	url = 'https://api.twitter.com/1.1/search/tweets.json'
	r = requests.get(url, auth=oauth,params=payload)
	a=r.json()
	#b=[]
	#for i in range(payload['count']):
	#	time=a['statuses'][i]['created_at']
	#	st=a['statuses'][i]['text']
	#	t=time.encode('utf8')
	#	s=st.encode('utf8')
	#	tup=(s,t)
	#	b.append(tup)
	#return render_template('syr.html',updates=b)
	return a

if __name__ == "__main__":
    app.run()

    