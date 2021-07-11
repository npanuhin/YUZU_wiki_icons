from os.path import isfile as os_isfile

from utils import mkpath, urlToGameRef
from yuzu_wiki import getGamesList, getGame

from time import sleep


def main():
    print("Getting games list...")

    games = getGamesList()

    games = [
        {
            "name": game[0],
            "ref": urlToGameRef(game[1]),
            "wiki_url": game[1],
        }
        for game in games
    ]
    missing = []

    print("Collecting game data...")

    for index, game in enumerate(games):
        if os_isfile(mkpath("../icons1000", game["ref"] + ".jpg")):
            continue

        try:
            release_id, wiki_img_url = getGame(game["ref"])

            if wiki_img_url is None:
                print("Icon \"{}\" is not present".format(game["ref"]))

                missing.append(game)

            print("{}/{} ({}) completed".format(index + 1, len(games), game["ref"]))

        except Exception:
            print("Exception in game {} ({})".format(game["name"], game["ref"]))
            # print_exc()

    if not missing:
        return

    # missing.md

    with open("missing.md", 'w', encoding="utf-8") as file:
        file.write("<h2 align=\"center\">Missing icons</h2>\n\n")
        file.write("There are {} games that currently have no icons. If you found them, please submit a PR or contact me\n\n".format(len(missing)))
        file.write("{}".format(
            "".join("- [{}]({}) ({})\n".format(game["name"], game["wiki_url"], game["ref"]) for game in missing)
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
