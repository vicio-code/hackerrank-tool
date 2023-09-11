data = {
    "url": "https://www.hackerrank.com/challenges/solve-me-first",
    "language": "JS",
    "domain": "Domain 4",
    "subdomain": "Vapo vapo",
    "problem": "Solve Me First",
    "score": "0",
    "dificulty": "Easy",
}


def create_domain_header(domain):
    return ["\n", f"## {domain}\n", "\n"]


def create_subdomain_list(subdomain):
    return [f"- [{subdomain}](github/link_to_subdomain)\n", "\n"]


def create_subdomain_table(subdomain):
    return [
        f"### {subdomain}\n",
        "\n",
        "| Problem | Solution | Time | Space | Difficulty | Points |\n",
        "| --- | --- | --- | --- | --- | --- |\n",
    ]


def main():
    file_path = "table.md"
    with open(file_path, "r", encoding="utf-8") as file:
        md_lines = file.readlines()

    domains_position = []
    subdomains_position = []
    domain_exists = False
    subdomain_exists = False

    for index in range(len(md_lines)):
        line = md_lines[index]
        if line.startswith("## "):
            domains_position.append([line, index])
        if line.startswith("- "):
            subdomains_position.append([line, index])
        if line.startswith(f"## {data['domain']}"):
            domain_exists = True
            current_domain_position = index
        if line.startswith(f"- [{data['subdomain']}"):
            subdomain_exists = True

    if not domain_exists:
        domain_h2 = create_domain_header(data["domain"])
        subdomain_list = create_subdomain_list(data["subdomain"])
        insert_position = subdomains_position[-1][1] + 1
        md_lines = (
            md_lines[:insert_position]
            + domain_h2
            + subdomain_list
            + md_lines[insert_position:]
        )

    if domain_exists and not subdomain_exists:
        subdomain_list = create_subdomain_list(data["subdomain"])
        insert_position = current_domain_position + 2
        for line in md_lines[current_domain_position + 2 :]:
            if line.startswith("\n"):
                break
            insert_position += 1
        md_lines = (
            md_lines[:insert_position] + subdomain_list + md_lines[insert_position:]
        )

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(md_lines)


if __name__ == "__main__":
    main()
