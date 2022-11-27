
from flask import Flask
from flask import send_from_directory
from flask import render_template

WEB_APP_DIR = 'templates'

app = Flask(__name__, template_folder=WEB_APP_DIR)


@app.route('/')
def render_page():
    return render_template('index.html')


@app.route('/web/')
def render_page_web():
    return render_template('index.html')


@app.route('/web/<path:name>')
def return_flutter_doc(name):

    datalist = str(name).split('/')
    DIR_NAME = WEB_APP_DIR

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])

@app.route('/test', methods=['GET', 'POST'])
def test():
    return 'ciao'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4999)

