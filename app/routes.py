from flask import render_template, request, redirect
from app import app, db
from app.models import Violation, User
from app.camera_manager import add_camera, remove_camera

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/violations')
def violations():
    all_violations = Violation.query.all()
    return render_template('violations.html', violations=all_violations)

@app.route('/add_camera', methods=['POST'])
def add_camera_route():
    url = request.form.get('url')
    add_camera(url)
    return redirect('/')

@app.route('/remove_camera', methods=['POST'])
def remove_camera_route():
    camera_id = request.form.get('camera_id')
    remove_camera(camera_id)
    return redirect('/')
