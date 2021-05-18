import requests
import json

from requests.api import head

url = "https://datahack.analyticsvidhya.com/problem/Z8DPWYU12032TI0/add-programming-answer/"

params = {
    'files':{
        'solution_file': open('submission.csv','rb'),
    },
    'data':{
        'csrfmiddlewaretoken': 'BYrKVPxeSRp5JgZirQRSxifDO8K4HiZjDDEc0BZQj9g2nOIdQYrTJqDHy0RGtjRD',
        'message': 'Test',
        'code_link_display': 'False',
    }
}
headers = {
        'accept': '*/*',
        'cookie': '_gcl_au=1.1.764887773.1621273390; _ga=GA1.2.14842170.1621273390; _gid=GA1.2.1967597321.1621273390; _ga=GA1.3.14842170.1621273390; _gid=GA1.3.1967597321.1621273390; _fbp=fb.1.1621273390396.1739191204; identityid=j9pyba13u9wqvum10czt75yn13g94l7y; csrftoken=8rNAETaohm4BSWzs7nAm677lCO50nhoXa602JFC0IEVywuinwvanifvpmGcC9igh; sessionid=5f83t1u37riak14pfp4m28jfji1oevsl',
        'origin': 'https://datahack.analyticsvidhya.com',
        'referer': 'https://datahack.analyticsvidhya.com/contest/janatahack-customer-segmentation/True/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'x-csrftoken': 'null',
        'x-newrelic-id': 'VwcFVFVQABAEU1dWBAEDV1I=',
        'x-requested-with': 'XMLHttpRequest',
}

def get_score(filename):
    params["files"]["solution_file"] = open(filename,'rb')
    r = requests.post(url, files=params["files"], data=params["data"], headers = headers)
    content = r.text[5507:5525]
    return content