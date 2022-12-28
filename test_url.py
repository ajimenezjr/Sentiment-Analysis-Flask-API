full_url = ''

text_details = open('text_to_summarize.txt', 'r').read()
stem = 'http://127.0.0.1:5000/summary/'
words = '50'
full_url = stem + "?words=" + words + "&q=" + text_details
# print(full_url)

import requests

api_url = stem


# API key (replace with your own API key)
# api_key = "sk_973e70a26e074017b34cdb07751a456e"


def request_response(data=None):
    # Make the API request
    response = requests.get(api_url, params={'words': words, 'q': text_details})
    data = response.json()
    return data


if __name__ == "__main__":
    request_data = request_response()
print(__name__)
print(request_data)
