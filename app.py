import os
import zipfile

project_structure = {
    "motorum-flask/": [
        "run.py", "requirements.txt", "README.md", ".gitignore"
    ],
    "motorum-flask/app/": [
        "__init__.py", "routes.py"
    ],
    "motorum-flask/app/static/css/": ["style.css"],
    "motorum-flask/app/static/images/": [],
    "motorum-flask/app/templates/": [
        "index.html", "compare.html", "brand_detail.html"
    ],
    "motorum-flask/app/data/": ["motorcycles.json"]
}

file_contents = {
    "run.py": '''from app import app

if __name__ == "__main__":
    app.run(debug=True)
''',
    "requirements.txt": "Flask==2.3.2\n",
    "README.md": "# Motorum - Flask Web Uygulaması\n\nBu proje, motosiklet markalarını ve modellerini karşılaştırabileceğiniz bir Flask web uygulamasıdır.",
    ".gitignore": "__pycache__/\n*.pyc\ninstance/\n.env\n",
    "__init__.py": '''from flask import Flask

app = Flask(__name__)

from app import routes
''',
    "routes.py": '''from flask import render_template, request
from app import app
import json

@app.route("/")
def index():
    with open("app/data/motorcycles.json") as f:
        data = json.load(f)
    return render_template("index.html", brands=data["brands"])

@app.route("/compare")
def compare():
    model1 = request.args.get("model1")
    model2 = request.args.get("model2")
    with open("app/data/motorcycles.json") as f:
        data = json.load(f)
    models = data["models"]
    m1 = next((m for m in models if m["name"] == model1), None)
    m2 = next((m for m in models if m["name"] == model2), None)
    return render_template("compare.html", model1=m1, model2=m2)
''',
    "style.css": "body { font-family: Arial, sans-serif; background-color: #f2f2f2; }",
    "index.html": '''<!doctype html>
<html>
<head><title>Motorum</title></head>
<body>
<h1>Markalar</h1>
<ul>
{% for brand in brands %}
  <li>{{ brand }}</li>
{% endfor %}
</ul>
</body>
</html>''',
    "compare.html": '''<!doctype html>
<html>
<head><title>Karşılaştırma</title></head>
<body>
<h1>Karşılaştırma</h1>
<p>{{ model1.name }} vs {{ model2.name }}</p>
</body>
</html>''',
    "brand_detail.html": '''<!doctype html>
<html>
<head><title>Marka Detayı</title></head>
<body>
<h1>Marka Detayı</h1>
</body>
</html>''',
    "motorcycles.json": '''{
  "brands": ["Küba", "Honda", "Yamaha", "Suzuki"],
  "models": [
    {"name": "Küba X", "brand": "Küba", "engine": "125cc", "price": "15000TL"},
    {"name": "Honda CBR", "brand": "Honda", "engine": "250cc", "price": "50000TL"}
  ]
}'''
}

zip_filename = "motorum-flask.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for folder, files in project_structure.items():
        for file in files:
            path = os.path.join(folder, file)
            content = file_contents.get(file, "")
            zipf.writestr(path, content)

print(f"{zip_filename} başarıyla oluşturuldu.")
