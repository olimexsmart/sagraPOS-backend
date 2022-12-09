
from flask import Flask
from flask import send_from_directory
from flask import render_template
# from flask import request
import json
from dataPersistence import *

# Init Flask server specifying static files directory
WEB_APP_DIR = 'templates'
app = Flask(__name__, template_folder=WEB_APP_DIR)

# Test that server is running fine


@app.route('/echo/<stuff>', methods=['GET'])
def test(stuff):
    return stuff

# Static file serving index 1


@app.route('/')
def staticServingIndex1():
    return render_template('index.html')

# Static file serving index 2


@app.route('/web/')
def staticServingIndex2():
    return render_template('index.html')

# Static file serving specific route


@app.route('/web/<path:name>')
def staticServingFromPath(name):
    print(name)
    datalist = str(name).split('/')
    filePath = WEB_APP_DIR
    # Join possible sub-folder names
    for i in range(0, len(datalist) - 1):
        filePath += '/' + datalist[i]
    # Return file
    return send_from_directory(filePath, datalist[-1])


@app.route('/db/getMenuEntries/<int:menuID>')
def getMenuEntries(menuID):
    return selectMenuEntries(menuID)


# Image serving from DB
@app.route('/db/getFoodImage/<int:menuEntryID>')
def getFoodImage(menuEntryID):
    return f'{menuEntryID}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4999)
