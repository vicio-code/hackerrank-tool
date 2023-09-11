from bs4 import BeautifulSoup
import sys
import hackerrank_solution_generator
import requests


def main(url, language):
    payload = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Cookie": "hackerrank_mixpanel_token=c6802eea-e672-4540-a19b-05b7d0d7fb7d; _hrank_session=789c1b8548900389505fcbd84ced11e7; hrc_l_i=F",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    html_content = response.text

    # Data Parsing
    soup = BeautifulSoup(html_content, "html.parser")

    categories_elements = soup.find_all("span", class_="breadcrumb-item-text")
    score_element = soup.find("p", class_="sidebar-detail pull-right")
    dificulty_elements = soup.find_all("div", class_="difficulty-block")
    dificulty_div = dificulty_elements[1].find_all("p")[1]

    data = {
        "url": url,
        "language": language,
        "domain": categories_elements[1].get_text(),
        "subdomain": categories_elements[2].get_text(),
        "problem": categories_elements[3].get_text(),
        "score": score_element.get_text(),
        "dificulty": dificulty_div.get_text(),
    }

    # for element in difficulty_score_elements:
    #     print(element.get_text())
    hackerrank_solution_generator.main(data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python request_script.py <link>")
    else:
        link = sys.argv[1]
        language = sys.argv[2]
        main(link, language)
