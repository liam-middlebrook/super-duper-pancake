import base64
import json
import os
import requests
from flask import Flask, jsonify, render_template, redirect, url_for, session
from flask_pyoidc.flask_pyoidc import OIDCAuthentication

app = Flask(__name__)

app.config.from_pyfile(os.path.join(os.getcwd(), "config.env.py"))

# Disable SSL certificate verification warning
requests.packages.urllib3.disable_warnings()

auth = OIDCAuthentication(app,
                          issuer=app.config['OIDC_ISSUER'],
                          client_registration_info=app.config['OIDC_CLIENT_CONFIG'])


@app.route("/")
@auth.oidc_auth
def index():
    attributes_raw = base64.b64decode(app.config['OIDC_ATTRIBUTES_LIST'])
    attributes_list = json.loads(attributes_raw.decode('ascii'))

    results_dict = {}
    for attrib in attributes_list:
        results_dict[attrib] = session['userinfo'].get(attrib, '')

    return jsonify(results_dict)

@app.route('/logout')
@auth.oidc_logout
def logout():
    return redirect(url_for('index'), 302)
