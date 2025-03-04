from flask import Flask, render_template, request, redirect, url_for, flash, after_this_request
from datetime import datetime
import os
import secrets


app = Flask(__name__)

# generate 32 char random key
app.secret_key = secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Plain text password
correct_password = "virenisthebest"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].upper()
        date_from = request.form['date_from']
        date_to = request.form['date_to']
        password = request.form['password']
        
        # Password validation
        if password != correct_password:
            flash("Incorrect password, please try again.")
            return render_template("index.html")

        # Format the date
        formatted_date_from = datetime.strptime(date_from, "%Y-%m-%d").strftime("%d %B %Y")
        formatted_date_to = datetime.strptime(date_to, "%Y-%m-%d").strftime("%d %B %Y")
        
        # Handle file upload
        photo = request.files['photo']
        if photo:
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
            photo.save(photo_path)
            
            return redirect(url_for('generated', name=name, date_from=formatted_date_from, date_to=formatted_date_to, photo=photo.filename))

    return render_template('index.html')

@app.route('/template')
def generated():
    name = request.args.get('name')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    photo = request.args.get('photo')
    
    # Schedule file deletion after the response is sent
    if photo:
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo)

        # @after_this_request
        # def remove_file(response):
        #     try:
        #         os.remove(photo_path)
        #     except Exception as e:
        #         print(f"Error deleting file: {e}")
        #     return response
    
    return render_template('template.html', name=name, date_from=date_from, date_to=date_to, photo=photo)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
