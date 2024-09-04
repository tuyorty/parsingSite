from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)  # Разрешаем CORS для всех маршрутов

@app.route('/parse', methods=['POST'])
def parse():
    data = request.json
    URL = data.get('URL')
    html_element_block = data.get('htmlElementBlock')
    class_element_block = data.get('classElementBlock')
    html_element_title = data.get('htmlElementTitle')
    class_element_title = data.get('classElementTitle')
    html_element_price = data.get('htmlElementPrice')
    class_element_price = data.get('classElementPrice')
    html_element_link = data.get('htmlElementLink')
    class_element_link = data.get('classElementLink')

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data', 'status_code': response.status_code})

    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll(html_element_block, class_=class_element_block)
    comps = []

    for item in items:
        comps.append({
            'title': item.find(html_element_title, class_=class_element_title).get_text(strip=True),
            'price': item.find(html_element_price, class_=class_element_price).get_text(strip=True),
            'link': item.find(html_element_link, class_=class_element_link).get('href')
        })

    return jsonify(comps)


if __name__ == '__main__':
    app.run(debug=True)

