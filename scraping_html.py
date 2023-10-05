import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URLを指定
url = ""

# HTMLをダウンロード
response = requests.get(url)
response.encoding = response.apparent_encoding # エンコーディングを自動検出
html = response.text

# HTMLからCSSファイルのリンクを取得
soup = BeautifulSoup(html, 'html.parser')
css_links = []
for link in soup.find_all('link'):
    if link.get('rel') == ['stylesheet']:
        css_links.append(link.get('href'))

# CSSファイルをダウンロードして保存するディレクトリを指定
css_dir = "C:\\"
if not os.path.exists(css_dir):
    os.makedirs(css_dir)

# CSSファイルをダウンロードして保存する
for link in css_links:
    css_url = urljoin(url, link) # 相対URLを絶対URLに変換
    css_response = requests.get(css_url)
    css_content = css_response.text
    css_filename = css_url.split('/')[-1] # ファイル名を取得
    css_path = os.path.join(css_dir, css_filename) # パスを作成
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# HTMLを保存するディレクトリを指定
html_dir = "C:\\"
if not os.path.exists(html_dir):
    os.makedirs(html_dir)

# HTMLを保存する
html_path = os.path.join(html_dir, "index.html")
with open(html_path, 'w', encoding=response.encoding) as f: # エンコーディングを指定
    f.write(html)
