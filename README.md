<h1 align="center">YUZU icons<h1>

This project is intended to fill the [YUZU wiki](https://yuzu-emu.org/game/) page with game icons.


## Requirements

- Python 3 (PIP): [requests](https://pypi.org/project/requests/), [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [scikit-image](https://pypi.org/project/scikit-image)

Install all at once:
```bash
py -3 -m pip install -U requests beautifulsoup4 scikit-image
```


#### Optional (development)

- JS ([NPM](https://nodejs.org/en/download/ "Download Node.js")): [nintendo-switch-eshop](https://www.npmjs.com/package/nintendo-eshop-api)

Install all at once:
```bash
npm install nintendo-switch-eshop
```



## Run

1. Run `main.py` to generate 1000x1000 icons
2. Run `src/verify.py` to check each icon (optional, recommended) 

	**Make sure to run it first with `delete_damaged = False`**
3. For those icons that were not generated or damaged – create them manually or skip
