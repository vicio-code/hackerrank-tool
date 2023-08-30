from bs4 import BeautifulSoup
import sys
import filing
import requests


def main(url):
    url = "https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/"

    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Cookie": "hackerrank_mixpanel_token=c6802eea-e672-4540-a19b-05b7d0d7fb7d; _hrank_session=789c1b8548900389505fcbd84ced11e7; hrc_l_i=F",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)

    # # Data Parsing
    # soup = BeautifulSoup(html_content, "html.parser")

    # difficulty_score_elements = soup.find_all("p", class_="pull-right")
    # categories_elements = soup.find_all("span", class_="breadcrumb-item-text")

    # data = []
    # data.append(url)

    # for element in difficulty_score_elements:
    #     data.append(element.get_text())
    # for element in categories_elements:
    #     data.append(element.get_text())

    # filing.main(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python request_script.py <link>")
    else:
        link = sys.argv[1]
        main(link)
