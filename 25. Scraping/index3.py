import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/maseeh.niazai'

try:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text of the first h1 element on the page
    h1_element = soup.find('h1')
    h1_text = h1_element.text.strip() if h1_element else "No h1 element found"

    # Print the extracted text
    print(f'First h1 element text: {h1_text}')

    # Extract the src attribute of the first img element on the page
    img_element = soup.find('img')
    img_src = img_element['src'] if img_element and 'src' in img_element.attrs else "No img element found"

    # Print the extracted src attribute
    print(f'First img element src attribute: {img_src}')

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
