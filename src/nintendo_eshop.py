from urllib.parse import urlparse, parse_qsl
from json import loads as json_loads
from requests import get as req_get
from bs4 import BeautifulSoup


def eshopNsuidAndIcon(release_id):
    r = req_get("https://ec.nintendo.com/apps/{}/GB".format(release_id))

    nsuid = dict(parse_qsl(
        urlparse(r.url).query
    ))["nsuid"]

    soup = BeautifulSoup(r.text, "lxml")

    img_url = soup.find("div", id="game_info").find("vc-price-box-standard").get(":packshot-src")

    img_url = "http:" + img_url.strip().strip("'").strip().strip('"')

    return nsuid, img_url
    # return mkpath("https://www.nintendo.co.uk", img_url)


def eshopSquareIcon(nsuid):
    img_url = json_loads(req_get(
        "http://search.nintendo-europe.com/en/select", params={
            "fq": "type:GAME AND system_type:nintendoswitch* AND product_code_txt:* AND nsuid_txt:{}".format(nsuid),
            "q": "*",
            "start": "0",
            "rows": "1"
        }
    ).text)["response"]['docs'][0]["image_url_sq_s"].replace("_image500w", "")

    return img_url


# --- TESTING ---

def main():
    # print(eshopNsuidAndIcon("0100749009844000"))
    print(eshopSquareIcon(eshopNsuidAndIcon("0100749009844000")[0]))


if __name__ == "__main__":
    main()
