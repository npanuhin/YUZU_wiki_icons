from os.path import join as os_join, normpath as os_normpath, split as os_split, dirname as os_dirname, isdir as os_isdir
from urllib.parse import urlparse, parse_qsl
from os import makedirs

from requests import head as req_head, get as req_get


def mkpath(*paths):
    return os_normpath(os_join(*paths))


def urlToGameRef(url):
    return os_split(urlparse(url).path.strip('/').strip('\\'))[-1]


def releaseIdToNsuid(release_id):
    return dict(parse_qsl(
        urlparse(
            req_head("https://ec.nintendo.com/apps/{}/GB".format(release_id), allow_redirects=True).url
        ).query
    ))["nsuid"]


def downloadFile(url, path):
    if not os_isdir(os_dirname(path)):
        makedirs(os_dirname(path))

    with open(path, 'wb') as file:
        file.write(req_get(url).content)


# --- TESTING ---

def main():
    print(urlToGameRef("https://yuzu-emu.org/game/3-little-pigs-and-bad-wolf/"))
    print(releaseIdToNsuid("0100749009844000"))


if __name__ == "__main__":
    main()
