import os


def to_camel_case(input_string):
    words = input_string.split()
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    return "".join(camel_case_words)


def to_snake_case(input_string):
    words = input_string.split()
    snake_case_string = "_".join([word.lower() for word in words])
    return snake_case_string


js_comment_template = """/*
Problem: {}
Dificulty: {}
Time Complexity:
Space Complexity:
Score: x/{}
*/
"""

py_comment_template = """#
# Problem: {}
# Dificulty: {}
# Time Complexity:
# Space Complexity:
# Score: x/{}
#
"""


def main(data):
    url = data["url"]
    language = data["language"]
    domain = data["domain"]
    subdomain = data["subdomain"]
    problem = data["problem"]
    dificulty = data["dificulty"]
    score = data["score"]

    file_path = f"hackerrank_solutions/{to_snake_case(domain)}/{to_snake_case(subdomain)}/{to_snake_case(problem)}"

    if language == "js":
        template = js_comment_template.format(url, dificulty, score)
    elif language == "py":
        template = py_comment_template.format(url, dificulty, score)

    if os.path.exists(file_path) == False:
        os.makedirs(file_path)

    with open(f"{file_path}/{to_camel_case(problem)}.{language}", "w") as file:
        file.write(template)


if __name__ == "__main__":
    data = []
    main(data)
