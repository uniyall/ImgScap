from bs4 import *
import requests as rq
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # For rendering Home Page
def form():
    return render_template('index.html')

@app.route('/images', methods = ['POST'])
def display_images():
    option = str(request.form['Links'])
    if(option == 'POTY'):
        r2 = rq.get('https://nypost.com/2022/12/01/2022-national-geographic-pictures-of-the-year/')
    if(option== 'FIFA'):
        r2 = rq.get('https://nypost.com/2022/11/22/moments-from-fifa-world-cup-qatar-2022/')
    if(option == 'NASA'):
        r2 = rq.get('https://nypost.com/2022/11/24/nasa-releases-amazing-new-images-of-the-surface-of-the-moon/')
    soup2 = BeautifulSoup(r2.text, "html.parser")
    links = []
    imgs = soup2.select('img[src^="https://nypost.com/wp-content/uploads"]')
    for img in imgs:
        links.append(img['src'])
    links = links[::2]
    del links[-2]
    return render_template('images.html', image_urls = links )

if __name__ == '__main__':
    app.run()

