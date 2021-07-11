from json import dump as json_dump  # , load as json_load
from os.path import isfile as os_isfile
# from traceback import print_exc

import sys
sys.path.append("src")

from utils import mkpath, urlToGameRef, downloadFile
from yuzu_wiki import getGamesList, getGame
from nintendo_eshop import eshopNsuidAndIcon, eshopSquareIcon


# ESHOP_GAMES = "eshop_games.json"
YUZU_WIKI_DATA = "yuzu-games-wiki/"


def main():
    # if not os_isfile(ESHOP_GAMES):
    #     raise FileNotFoundError("Eshop games list not found")
    # with open(ESHOP_GAMES, 'r', encoding="utf-8") as file:
    #     eshop_games = json_load(file)

    print("Getting games list...")
    games = getGamesList()

    games = [
        {
            "name": game[0],
            "ref": urlToGameRef(game[1]),
            "wiki_url": game[1],
            "compatebility": game[2]
        }
        for game in games
    ]

    print("Collecting game data...")

    for index, game in enumerate(games):
        if os_isfile(mkpath("icons1000", game["ref"] + ".jpg")):
            continue

        try:
            release_id, wiki_img_url = getGame(game["ref"])

            nsuid, _ = eshopNsuidAndIcon(release_id)

            icon_url = eshopSquareIcon(nsuid)

            game["release_id"] = release_id
            game["nsuid"] = nsuid
            game["wiki_img_url"] = wiki_img_url

            downloadFile(icon_url, mkpath("icons1000", game["ref"] + ".jpg"))

            # print("{} | {} | {} | {}".format(game["name"], release_id, nsuid, icon_url))

            print("{}/{} ({}) completed".format(index + 1, len(games), game["ref"]))

        except Exception:
            print("Exception in game {} ({})".format(game["name"], game["ref"]))
            # print_exc()

        # if index == 3:
        #     break

    print("Writing database")
    with open("games.json", 'w', encoding="utf-8") as file:
        json_dump(games, file, ensure_ascii=False, indent=4)
        file.write('\n')

    print("Finished")


if __name__ == "__main__":
    main()
