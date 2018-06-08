from flask import Flask, Blueprint, render_template
app = Flask(__name__, static_url_path='/static', static_folder='./static')
app.config['SERVER_NAME'] = 'sojerntest.com:5000'
# app.url_map.default_subdomain = 'www'

www_blueprint = Blueprint('www', 'www', subdomain='www', static_url_path='/static', static_folder='./static')


@app.route('/')
def main():
    return render_template('privacy.html')


@www_blueprint.route('/')
def www():
    return render_template('privacy.html')
app.register_blueprint(www_blueprint)


privacy_blueprint = Blueprint('privacy', __name__, subdomain='privacy', static_url_path='/static', static_folder='./static')


@privacy_blueprint.route('/')
def privacy():
    return render_template('cookie_iframe.html')
app.register_blueprint(privacy_blueprint)

if __name__ == '__main__':
    app.run(host='sojerntest.com', port=5000, debug=True)
