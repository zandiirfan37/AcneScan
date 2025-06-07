from flask import Flask
from app.routes import main
import os

app = Flask(__name__)

# Konfigurasi folder upload
# app.config['UPLOAD_FOLDER'] = os.path.join('app', 'static', 'assets', 'img')

# simpan ke folder <project-root>/static/uploads
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Register blueprint
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
