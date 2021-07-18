from os.path import isfile as os_isfile
from json import load as json_load

# from utils import mkpath, urlToGameRef
# from yuzu_wiki import getGamesList, getGame


# --- SETTINGS --- #

game_database = "../games.json"

# --- SETTINGS --- #


def main():
    if not os_isfile(game_database):
        raise FileNotFoundError("Game database not found")

    with open(game_database, 'r', encoding="utf-8") as file:
        games = json_load(file)

    missing = {
        game_ref: game for game_ref, game in games.items() if "icon1000" not in game or game["icon1000"] is None
    }

    if not missing:
        return

    # missing.md

    with open("missing.md", 'w', encoding="utf-8") as file:
        file.write("<h2 align=\"center\">Missing icons</h2>\n\n")
        file.write("There are {} games that currently have no icons. If you found them, please open a new GitHub issue, submit a PR or contact me\n\n".format(len(missing)))
        file.write("{}".format(
            "".join("- [{}]({}) ({})\n".format(game["name"], game["wiki_url"], game_ref) for game_ref, game in missing.items()).replace('~', "\\~")
        ))

    # README.md

    with open("../README.md", 'r', encoding="utf-8") as file:
        readme = file.read()

    readme_start_pos = readme.find("<!-- MISSING ICONS START -->") + 28
    readme_end_pos = readme.find("<!-- MISSING ICONS END -->")

    with open("missing.md", 'r', encoding="utf-8") as file:
        readme = readme[:readme_start_pos] + '\n' + file.read() + readme[readme_end_pos:]

    with open("../README.md", 'w', encoding="utf-8") as file:
        file.write(readme)


if __name__ == "__main__":
    main()
