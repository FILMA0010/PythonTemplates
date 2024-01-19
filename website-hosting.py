# Simple Website-Hosting Example
# Required packages: flask and flask_sslify
# pip install flask flask_sslify
from flask import Flask, render_template
from flask_sslify import SSLify

port=3000 # Change the Port of your web application

app = Flask(__name__, static_folder='static', static_url_path='/static') # Folder for Static Content like CSS.
sslify = SSLify(app)

@app.route('/') # Path on Website
def index(): # Dont forget to change this when you copy
    return render_template('index.html') # Name of the file

@app.route('/test') # Path on Website
def test(): # Dont forget to change this when you copy
    return render_template('test.html') # Name of the file

if __name__ == '__main__':
#    app.run(host='0.0.0.0', ssl_context=('path/to/ssl_cert.pem', 'path/to/ssl_key.pem')) # Use if SSL (HTTPS)
     app.run(host='0.0.0.0', port=port) # Host is for public hosting, so others can connect. Otherwise only you can via the local connection