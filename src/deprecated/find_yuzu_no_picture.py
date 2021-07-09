from requests import Session
from bs4 import BeautifulSoup
from os.path import isfile


def getGames(session):
    soup = BeautifulSoup(session.get("https://yuzu-emu.org/game/").text, "lxml").find("body")

    soup = soup.find_all("div", class_="container")[2].find("table").find("tbody")

    games = {}

    for line in soup.find_all("tr"):
        link = line.find("td").find("a")
        game_compatebility = int(line.find_all("td")[1].get("data-compatibility"))

        games[link.text.strip()] = [link.get("href"), game_compatebility]

    return games


def updateGameList(path, item=None, sort_id=None):

    if not isfile(path):
        with open(path, 'w', encoding="utf-8"):
            pass

        items = set()

    else:
        with open(path, 'r', encoding="utf-8") as file:
            items = set(
                (
                    line.split()[0].strip(),
                    int(line.split('|')[1].strip())
                ) for line in file
            )

    if item is not None:
        items.add((item, sort_id))

    with open(path, 'w', encoding="utf-8") as file:
        file.write("\n".join(
            ' | '.join(map(str, line)) for line in sorted(list(items), key=lambda item: (item[1], item[0]))
        ))

    return set(item[0] for item in items)


def main():
    print("Starting...")
    session = Session()

    games = getGames(session)

    print("Games: {}".format(len(games)))

    skip_games = updateGameList("without_picture.txt")

    # print(skip_games)

    count = 0

    for game_title, (game_url, game_compatebility) in games.items():
        count += 1
        if game_url in skip_games:
            continue

        soup = BeautifulSoup(session.get(game_url).text, "lxml").find("body")

        try:
            img = soup.find_all("div", class_="container")[1].find_all("div", class_="column")[1].find("img")

            if img.get("src") == "https://yuzu-emu.org/images/boxart.png":
                print("{}/{}: \"{}\" [{}] has NO image".format(count, len(games), game_title, game_compatebility))

                skip_games = updateGameList("without_picture.txt", game_url, game_compatebility)

            else:
                print("{}/{}: \"{}\" [{}] has image".format(count, len(games), game_title, game_compatebility))

        except Exception as e:
            print(e)
            print(game_title, (game_url, game_compatebility))


# if __name__ == "__main__":
#     main()
