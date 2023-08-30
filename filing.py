import os


def to_camel_case(input_string):
    words = input_string.split()
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    return "".join(camel_case_words)


def to_snake_case(input_string):
    words = input_string.split()
    snake_case_string = "_".join([word.lower() for word in words])
    return snake_case_string


def main(data):
    url = data[0]
    domain = data[4]
    subdomain = data[5]
    problem = data[6]
    score = data[2]
    dificulty = data[1]
    language = "js"

    file_path = f"hackerrank_solutions/{to_snake_case(domain)}/{to_snake_case(subdomain)}/{to_snake_case(problem)}"

    template = """/*
Problem: {}
Dificulty: {}
Time Complexity:
Space Complexity:
Score: x/{}
*/
""".format(
        url, dificulty, score
    )

    os.makedirs(file_path)

    with open(f"{file_path}/{to_camel_case(problem)}.{language}", "w") as file:
        file.write(template)


if __name__ == "__main__":
    data = []
    main(data)
