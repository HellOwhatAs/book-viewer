import json, os
books = []
links = []
for book_path in [
    "./example/math.json",
    "./example/Skeleton_Crew.json",
    "./example/Cycle_of_the_Werewolf.json"
]:
    with open(book_path, "r", encoding='utf-8') as f:
        chapters = [
            [
                f"<mark>{os.path.basename(book_path)}</mark>",
                [
                    f"The start of {os.path.basename(book_path)}"
                ]
            ]
        ]
        commands = []
        book = json.load(f)
        for elem in book:
            if isinstance(elem, list):
                chapters.append(elem)
            elif isinstance(elem, dict) and elem not in links:
                links.append(elem)
            elif isinstance(elem, str):
                commands.append(elem)
            else:
                ...
        for cpt in chapters:
            cpt.extend(commands)
        books.extend(chapters)

BOOK = links + books