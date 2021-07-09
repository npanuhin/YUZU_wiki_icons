from bs4 import BeautifulSoup
from requests import get as req_get

from utils import urlToGameRef


def getGamesList():
    soup = BeautifulSoup(req_get("https://yuzu-emu.org/game/").text, "lxml").find("body")

    soup = soup.find_all("div", class_="container")[2].find("table").find("tbody")

    games = []

    for line in soup.find_all("tr"):
        link = line.find("td").find("a")

        games.append([
            link.text.strip(),                                     # Name of the game
            link.get("href").strip(),                              # Link to YUZU game's wiki page
            int(line.find_all("td")[1].get("data-compatibility"))  # Compatebility [0 (Perfect) - 5 (Won't Boot) or 99 (Not Tested)]
        ])

    return games


def getGame(game_ref):
    soup = BeautifulSoup(req_get("https://yuzu-emu.org/game/{}/".format(game_ref)).text, "lxml").find("body")

    img_path = soup.find_all("div", class_="container")[1].find_all("div", class_="column")[1].find("img").get("src").strip()

    if img_path == "https://yuzu-emu.org/images/boxart.png":
        img_path = None

    release_id = soup.find_all("div", class_="container")[1].find_all("div", class_="column")[1].find_all("div", class_="columns")[1]
    release_id = release_id.find_all("div", class_="column")[1].text.strip()

    return (release_id, img_path)


# --- TESTING ---

def main():
    print(len(getGamesList()))
    print(getGame(urlToGameRef("https://yuzu-emu.org/game/20xx/")))


if __name__ == "__main__":
    main()
