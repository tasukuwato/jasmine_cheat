import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = ''
output_dir = 'C:\\'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for script in soup.find_all('script'):
    if script.has_attr('src'):
        file_url = urljoin(url, script['src'])
        file_name = os.path.basename(file_url)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'wb') as f:
            f.write(requests.get(file_url).content)

for link in soup.find_all('a'):
    file_url = urljoin(url, link.get('href'))
    if file_url.endswith('.html'):
        file_name = os.path.basename(file_url)
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'wb') as f:
            f.write(requests.get(file_url).content)
        response = requests.get(file_url)
        linked_resources_soup = BeautifulSoup(response.content, 'html.parser')
        for resource in linked_resources_soup.find_all(['script', 'link']):
            if resource.has_attr('src'):
                file_url = urljoin(file_url, resource['src'])
                file_name = os.path.basename(file_url)
                file_path = os.path.join(output_dir, file_name)
                with open(file_path, 'wb') as f:
                    f.write(requests.get(file_url).content)
