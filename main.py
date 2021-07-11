from json import dump as json_dump, load as json_load
from os.path import isfile as os_isfile
# from traceback import print_exc
from copy import deepcopy

import sys
sys.path.append("src")

from utils import mkpath, urlToGameRef, downloadFile
from yuzu_wiki import getYuzuGames, getGame
from nintendo_eshop import eshopNsuid, eshopSquareIcon


# --- SETTINGS --- #

# YUZU_WIKI_REPO = "yuzu-games-wiki/"
force_game_update = False

# --- SETTINGS --- #


def main():
    if os_isfile("games.json"):
        with open("games.json", 'r', encoding="utf-8") as file:
            games = json_load(file)
    else:
        games = {}

    print("Database contains {} games".format(len(games)))

    print("Getting YUZU game list...")
    count = 0
    for game in getYuzuGames():
        count += 1
        game_ref = urlToGameRef(game[1])

        if game_ref not in games:
            games[game_ref] = {
                "name": game[0],
                "wiki_url": game[1],
                "compatebility": game[2]
            }

    print("Found {} games".format(count))

    print("Collecting YUZU game data...")

    game_index = 0
    for game_ref, game in games.items():

        release_id_updated, nsuid_updated, icon_url_updated = False, False, False
        old_game = deepcopy(game)

        try:
            if force_game_update or "release_id" not in game or "wiki_img_url" not in game:
                release_id, wiki_img_url = getGame(game_ref)
                game["release_id"] = release_id
                game["wiki_img_url"] = wiki_img_url

                release_id_updated = True

            if force_game_update or release_id_updated or "nsuid" not in game:
                nsuid = eshopNsuid(game["release_id"])
                game["nsuid"] = nsuid

                nsuid_updated = True

            if force_game_update or nsuid_updated or "icon_url" not in game:
                icon_url = eshopSquareIcon(game["nsuid"])
                game["icon_url"] = icon_url

                icon_url_updated = True

            if force_game_update or icon_url_updated or "icon1000" not in game:
                game["icon1000"] = None  # Will be updated later

                if not os_isfile(mkpath("icons1000", game_ref + ".jpg")):
                    downloadFile(game["icon_url"], mkpath("icons1000", game_ref + ".jpg"))

            # print("{} | {} | {} | {}".format(game["name"], release_id, nsuid, icon_url))

        except Exception:
            print("Exception in game \"{}\" ({})".format(game["name"], game_ref))
            # print_exc()

        if os_isfile(mkpath("icons1000", game_ref + ".jpg")):
            game["icon1000"] = game_ref + ".jpg"

        if old_game != game:
            with open("games.json", 'w', encoding="utf-8") as file:
                json_dump(games, file, ensure_ascii=False, indent=4)
                file.write('\n')

        game_index += 1
        print("{}/{} ({}) completed".format(game_index, len(games), game_ref))
        # if game_index == 3:
        #     break

    print("Finished")


if __name__ == "__main__":
    main()
