# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:59:27 2022

@author: jeanc
"""

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import redirect
from datetime import date
import dtos
import services

app = Flask(__name__, static_url_path='')

@app.context_processor
def inject_today_date():
    return {'today_date': date.today()}

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/scss/<path:path>')
def send_scss(path):
    return send_from_directory('scss', path)

@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

from flask import url_for



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchEtab')
def search_etab():
    return render_template('searchEtab.html')

@app.route('/searchEtabGet')
def search_etab_get():
    keyword = request.args.get('keyword', '')

    inspections = services.getInspectionsFromKeyword(keyword)

    return render_template('searchEtabResult.html', inspections = inspections, nbInspections = len(inspections))
    

@app.route('/simulerEtab')
def simuler_etab():
    idinspection = 33610

    resultAissa, resultArthur, resultJean, inspectionInfo = services.getModelsResults(idinspection)

    return render_template('simulerNvleVisiteEtab.html', resultAissa = resultAissa, resultArthur = resultArthur, resultJean = resultJean, ins = inspectionInfo)


@app.route('/simulerNvleVisite')
def simuler_nouvelle_visite_etab():
    idinspection = int(request.args.get('idins', ''))

    resultAissa, resultArthur, resultJean, inspectionInfo = services.getModelsResults(idinspection)

    return render_template('simulerNvleVisiteEtab.html', resultAissa = resultAissa, resultArthur = resultArthur, resultJean = resultJean, ins = inspectionInfo)

@app.route('/configIA')
def config_ia():
    return render_template('notImplemented.html')

@app.route('/searchEtabFromPos')
def search_etab_from_pos():

    return redirect("/searchEtabGet?keyword=nancy")

    #inspections = services.getInspectionsFromKeyword('nancy')

    #return render_template('searchEtabResult.html', keyword = 'nancy', inspections = inspections, nbInspections = len(inspections))

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')




# with app.test_request_context():
    # print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))
    # url_for('static', filename='bootstrap.min.css')
    # url_for('static', filename='bootstrap.min.js')
