import requests
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/crawl', methods=['POST'])
def crawl():
    url = request.json['url']
    depth = request.json['depth']

    result = {}
    visited = set()
    url_queue = [(url, 1)]

    while url_queue:
        current_url, current_depth = url_queue.pop(0)

        if current_depth > depth:
            break

        if current_url not in visited:
            try:
                response = requests.get(current_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                links = set()

                for link in soup.find_all('a'):
                    href = link.get('href')

                    if href is not None and href.startswith('http'):
                        links.add(href)

                result[current_url] = list(links)
                visited.add(current_url)

                for link in links:
                    if link not in visited:
                        url_queue.append((link, current_depth + 1))

            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL {current_url}: {e}")

    return jsonify({
        "data": result,
        "status": "success"
    })


if __name__ == '__main__':
    app.run(debug=True)
