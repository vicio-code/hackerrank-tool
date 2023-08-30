import requests

url = (
    "https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/"
)

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie": "hackerrank_mixpanel_token=c6802eea-e672-4540-a19b-05b7d0d7fb7d; _hrank_session=789c1b8548900389505fcbd84ced11e7; hrc_l_i=F",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
