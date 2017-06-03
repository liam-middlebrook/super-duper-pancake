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
    username = session['userinfo'].get('preferred_username', '')
    display_name = session['userinfo'].get('name', '')

    return jsonify({
        "preferred_username": username,
        "name": display_name
    })


@app.route('/logout')
@auth.oidc_logout
def logout():
    return redirect(url_for('index'), 302)
