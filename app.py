# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Örnek markalar (gerçek bir uygulamada veritabanından çekilir)
MARKALAR = ["Yamaha", "Honda", "Suzuki", "Kuba"]

@app.route('/')
def index():
    """Ana sayfa"""
    return render_template('index.html', markalar=MARKALAR)

@app.route('/marka/<marka_adi>')
def marka_detay(marka_adi):
    """Marka detay sayfası"""
    if marka_adi in MARKALAR:
        # Burada o markaya ait ilanlar listelenecek
        return render_template('marka.html', marka=marka_adi)
    else:
        return "Marka bulunamadı", 404

@app.route('/karsilastirma')
def karsilastirma():
    """Karşılaştırma sayfası"""
    return render_template('karsilastirma.html')

@app.route('/arama', methods=['GET'])
def arama():
    """Arama işlevi (şimdilik sadece sorguyu gösterir)"""
    sorgu = request.args.get('q', '')
    # Gerçek bir uygulamada burada veritabanında arama yapılır
    return f"Arama sorgusu: '{sorgu}' - (Bu kısım geliştirilecek)"

if __name__ == '__main__':
    app.run(debug=True)
