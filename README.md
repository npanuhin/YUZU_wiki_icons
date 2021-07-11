<h1 align="center">YUZU icons</h1>

This project is intended to fill the [YUZU wiki](https://yuzu-emu.org/game/) page with game icons.


## Requirements

- Python 3 (PIP): [requests](https://pypi.org/project/requests/), [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), [Pillow](https://pypi.org/project/Pillow/)

Install all at once:
```bash
py -3 -m pip install -U requests beautifulsoup4 Pillow
```


#### Optional (development)

- JS ([NPM](https://nodejs.org/en/download/ "Download Node.js")): [nintendo-switch-eshop](https://www.npmjs.com/package/nintendo-eshop-api)

Install all at once:
```bash
npm install nintendo-switch-eshop
```


## Usage

Run `main.py` to update the entire database. You can set `force_game_update = True` to force all games to be updated.

Run `src/verify.py` to make sure the 1000x1000 icons are not damaged and the correct size. You can set `delete_damaged = True` to remove damaged files (**WARNING**).

Run `src/print_missing.py` to update README with missing icons.


<!-- MISSING ICONS START -->
<h2 align="center">Missing icons</h2>

There are 117 games that currently have no icons. If you found them, please submit a PR or contact me

- [3D MiniGolf](https://yuzu-emu.org/game/3d-minigolf/) (3d-minigolf)
- [60 Seconds!](https://yuzu-emu.org/game/60-seconds/) (60-seconds)
- [ACA NEOGEO THE ULTIMATE 11: SNK FOOTBALL CHAMPIONSHIP](https://yuzu-emu.org/game/aca-neogeo-the-ultimate-11-snk-football-championship/) (aca-neogeo-the-ultimate-11-snk-football-championship)
- [Adventure Time: Pirates of the Enchiridion](https://yuzu-emu.org/game/adventure-time-pirates-of-the-enchiridion/) (adventure-time-pirates-of-the-enchiridion)
- [AeternoBlade II](https://yuzu-emu.org/game/aeternoblade-ii/) (aeternoblade-ii)
- [ALPHA](https://yuzu-emu.org/game/alpha/) (alpha)
- [American Ninja Warrior: Challenge](https://yuzu-emu.org/game/american-ninja-warrior-challenge/) (american-ninja-warrior-challenge)
- [Animal Crossing: New Horizons Island Transfer Tool](https://yuzu-emu.org/game/animal-crossing-new-horizons-island-transfer-tool/) (animal-crossing-new-horizons-island-transfer-tool)
- [Atelier Lydie & Suelle \~The Alchemists and the Mysterious Paintings\~](https://yuzu-emu.org/game/atelier-lydie-and-suelle-\~the-alchemists-and-the-mysterious-paintings\~/) (atelier-lydie-and-suelle-\~the-alchemists-and-the-mysterious-paintings\~)
- [Ben 10](https://yuzu-emu.org/game/ben-10/) (ben-10)
- [Big Buck Hunter Arcade](https://yuzu-emu.org/game/big-buck-hunter-arcade/) (big-buck-hunter-arcade)
- [BLAZBLUE CROSS TAG BATTLE SPECIAL TRIAL](https://yuzu-emu.org/game/blazblue-cross-tag-battle-special-trial/) (blazblue-cross-tag-battle-special-trial)
- [Caged Garden Cock Robin](https://yuzu-emu.org/game/caged-garden-cock-robin/) (caged-garden-cock-robin)
- [Cars 3: Driven to Win](https://yuzu-emu.org/game/cars-3-driven-to-win/) (cars-3-driven-to-win)
- [CHRONO CLASH: Fantasy Tactics](https://yuzu-emu.org/game/chrono-clash-fantasy-tactics/) (chrono-clash-fantasy-tactics)
- [Clue: The Classic Mystery Game](https://yuzu-emu.org/game/clue-the-classic-mystery-game/) (clue-the-classic-mystery-game)
- [DAEMON X MACHINA: Prototype Missions](https://yuzu-emu.org/game/daemon-x-machina-prototype-missions/) (daemon-x-machina-prototype-missions)
- [Dawn of the Breakers](https://yuzu-emu.org/game/dawn-of-the-breakers/) (dawn-of-the-breakers)
- [de Blob 2](https://yuzu-emu.org/game/de-blob-2/) (de-blob-2)
- [Eternal Edge](https://yuzu-emu.org/game/eternal-edge/) (eternal-edge)
- [Fallen Legion: Rise to Glory](https://yuzu-emu.org/game/fallen-legion-rise-to-glory/) (fallen-legion-rise-to-glory)
- [FINAL FANTASY X/X-2 HD Remaster](https://yuzu-emu.org/game/final-fantasy-xx-2-hd-remaster/) (final-fantasy-xx-2-hd-remaster)
- [Football Manager 2020 Touch](https://yuzu-emu.org/game/football-manager-2020-touch/) (football-manager-2020-touch)
- [Ginger: Beyond the Crystal](https://yuzu-emu.org/game/ginger-beyond-the-crystal/) (ginger-beyond-the-crystal)
- [Goosebumps The Game](https://yuzu-emu.org/game/goosebumps-the-game/) (goosebumps-the-game)
- [GROOVE COASTER WAI WAI PARTY!!!!](https://yuzu-emu.org/game/groove-coaster-wai-wai-party/) (groove-coaster-wai-wai-party)
- [Harvest Moon: Light of Hope Special Edition](https://yuzu-emu.org/game/harvest-moon-light-of-hope-special-edition/) (harvest-moon-light-of-hope-special-edition)
- [Has-Been Heroes](https://yuzu-emu.org/game/has-been-heroes/) (has-been-heroes)
- [Hello Kitty Kruisers With Sanrio Friends](https://yuzu-emu.org/game/hello-kitty-kruisers-with-sanrio-friends/) (hello-kitty-kruisers-with-sanrio-friends)
- [Hill Climbing Mania](https://yuzu-emu.org/game/hill-climbing-mania/) (hill-climbing-mania)
- [Hotel Transylvania 3 Monsters Overboard](https://yuzu-emu.org/game/hotel-transylvania-3-monsters-overboard/) (hotel-transylvania-3-monsters-overboard)
- [Hulu](https://yuzu-emu.org/game/hulu/) (hulu)
- [Just Dance 2018](https://yuzu-emu.org/game/just-dance-2018/) (just-dance-2018)
- [L.A. Noire](https://yuzu-emu.org/game/la-noire/) (la-noire)
- [LAYTON’S MYSTERY JOURNEY: Katrielle and the Millionaires’ Conspiracy - Deluxe Edition](https://yuzu-emu.org/game/laytons-mystery-journey-katrielle-and-the-millionaires-conspiracy-deluxe-edition/) (laytons-mystery-journey-katrielle-and-the-millionaires-conspiracy-deluxe-edition)
- [LEGO DC Super-Villains](https://yuzu-emu.org/game/lego-dc-super-villains/) (lego-dc-super-villains)
- [Let's Sing 2018](https://yuzu-emu.org/game/lets-sing-2018/) (lets-sing-2018)
- [Lumo](https://yuzu-emu.org/game/lumo/) (lumo)
- [Minecraft: Story Mode - Season Two](https://yuzu-emu.org/game/minecraft-story-mode-season-two/) (minecraft-story-mode-season-two)
- [Minecraft: Story Mode - The Complete Adventure](https://yuzu-emu.org/game/minecraft-story-mode-the-complete-adventure/) (minecraft-story-mode-the-complete-adventure)
- [MotoGP18](https://yuzu-emu.org/game/motogp18/) (motogp18)
- [MXGP3 - The Official Motocross Videogame](https://yuzu-emu.org/game/mxgp3-the-official-motocross-videogame/) (mxgp3-the-official-motocross-videogame)
- [NBA 2K18](https://yuzu-emu.org/game/nba-2k18/) (nba-2k18)
- [NBA 2K21](https://yuzu-emu.org/game/nba-2k21/) (nba-2k21)
- [Ni no Kuni: Wrath of the White Witch](https://yuzu-emu.org/game/ni-no-kuni-wrath-of-the-white-witch/) (ni-no-kuni-wrath-of-the-white-witch)
- [ONE PIECE: Unlimited World Red Deluxe Edition](https://yuzu-emu.org/game/one-piece-unlimited-world-red-deluxe-edition/) (one-piece-unlimited-world-red-deluxe-edition)
- [Party Planet](https://yuzu-emu.org/game/party-planet/) (party-planet)
- [Penny-Punching Princess](https://yuzu-emu.org/game/penny-punching-princess/) (penny-punching-princess)
- [Please Teach Me Onedari Shogi](https://yuzu-emu.org/game/please-teach-me-onedari-shogi/) (please-teach-me-onedari-shogi)
- [RXN -Raijin-](https://yuzu-emu.org/game/rxn-raijin-/) (rxn-raijin-)
- [Saturday Morning RPG](https://yuzu-emu.org/game/saturday-morning-rpg/) (saturday-morning-rpg)
- [SEGA AGES Lightening Force: Quest for the Darkstar](https://yuzu-emu.org/game/sega-ages-lightening-force-quest-for-the-darkstar/) (sega-ages-lightening-force-quest-for-the-darkstar)
- [Shantae: Half- Genie Hero Ultimate Edition](https://yuzu-emu.org/game/shantae-half-genie-hero-ultimate-edition/) (shantae-half-genie-hero-ultimate-edition)
- [Smash Boats](https://yuzu-emu.org/game/smash-boats/) (smash-boats)
- [Sniper Elite 3 Ultimate Edition](https://yuzu-emu.org/game/sniper-elite-3-ultimate-edition/) (sniper-elite-3-ultimate-edition)
- [South Park: The Fractured but Whole - Standard Edition](https://yuzu-emu.org/game/south-park-the-fractured-but-whole-standard-edition/) (south-park-the-fractured-but-whole-standard-edition)
- [Space Invaders Forever](https://yuzu-emu.org/game/space-invaders-forever/) (space-invaders-forever)
- [SpongeBob SquarePants: Battle for Bikini Bottom - Rehydrated](https://yuzu-emu.org/game/spongebob-squarepants-battle-for-bikini-bottom-rehydrated/) (spongebob-squarepants-battle-for-bikini-bottom-rehydrated)
- [Sports Party](https://yuzu-emu.org/game/sports-party/) (sports-party)
- [SUPER DRAGON BALL HEROES WORLD MISSION - Launch Edition](https://yuzu-emu.org/game/super-dragon-ball-heroes-world-mission-launch-edition/) (super-dragon-ball-heroes-world-mission-launch-edition)
- [Taxi Chaos](https://yuzu-emu.org/game/taxi-chaos/) (taxi-chaos)
- [The Longest Five Minutes](https://yuzu-emu.org/game/the-longest-five-minutes/) (the-longest-five-minutes)
- [This Is the Police](https://yuzu-emu.org/game/this-is-the-police/) (this-is-the-police)
- [Touhou Kobuto V: Burst Battle](https://yuzu-emu.org/game/touhou-kobuto-v-burst-battle/) (touhou-kobuto-v-burst-battle)
- [Tri6: Infinite](https://yuzu-emu.org/game/tri6-infinite/) (tri6-infinite)
- [Ultra Street Fighter II: The Final Challengers](https://yuzu-emu.org/game/ultra-street-fighter-ii-the-final-challengers/) (ultra-street-fighter-ii-the-final-challengers)
- [Under Night In-Birth Exe:Late[cl-r]](https://yuzu-emu.org/game/under-night-in-birth-exelatecl-r/) (under-night-in-birth-exelatecl-r)
- [UNO for Nintendo Switch](https://yuzu-emu.org/game/uno-for-nintendo-switch/) (uno-for-nintendo-switch)
- [Unravel Two](https://yuzu-emu.org/game/unravel-two/) (unravel-two)
- [Urban Trial Playground](https://yuzu-emu.org/game/urban-trial-playground/) (urban-trial-playground)
- [Wolfenstein: Youngblood](https://yuzu-emu.org/game/wolfenstein-youngblood/) (wolfenstein-youngblood)
- [Worldend Syndrome](https://yuzu-emu.org/game/worldend-syndrome/) (worldend-syndrome)
- [Xenoblade Chronicles 2: Torna \~ The Golden Country](https://yuzu-emu.org/game/xenoblade-chronicles-2-torna-\~-the-golden-country/) (xenoblade-chronicles-2-torna-\~-the-golden-country)
- [Assassin’s Creed: The Rebel Collection](https://yuzu-emu.org/game/assassins-creed-the-rebel-collection/) (assassins-creed-the-rebel-collection)
- [Asterix & Obelix XXL: Romastered](https://yuzu-emu.org/game/asterix-obelix-xxl-romastered/) (asterix-obelix-xxl-romastered)
- [Atelier Ryza: Ever Darkness & the Secret Hideout](https://yuzu-emu.org/game/atelier-ryza-ever-darkness-and-the-secret-hideout/) (atelier-ryza-ever-darkness-and-the-secret-hideout)
- [Attack on Titan 2](https://yuzu-emu.org/game/attack-on-titan-2/) (attack-on-titan-2)
- [Azur Lane: Crosswave](https://yuzu-emu.org/game/azur-lane-crosswave/) (azur-lane-crosswave)
- [Ben 10: Power Trip!](https://yuzu-emu.org/game/ben-10-power-trip/) (ben-10-power-trip)
- [Broken Lines](https://yuzu-emu.org/game/broken-lines/) (broken-lines)
- [Cabela's: The Hunt - Championship Edition](https://yuzu-emu.org/game/cabelas-the-hunt-championship-edition/) (cabelas-the-hunt-championship-edition)
- [Cartoon Network: Battle Crashers](https://yuzu-emu.org/game/cartoon-network-battle-crashers/) (cartoon-network-battle-crashers)
- [Code: Realize \~Future Blessings\~](https://yuzu-emu.org/game/code-realize-future-blessings/) (code-realize-future-blessings)
- [Collar X Malice -Unlimited-](https://yuzu-emu.org/game/collar-x-malice-unlimited/) (collar-x-malice-unlimited)
- [de Blob](https://yuzu-emu.org/game/de-blob/) (de-blob)
- [Disney Classic Games: Aladdin and The Lion King](https://yuzu-emu.org/game/disney-classic-games-aladdin-and-the-lion-king/) (disney-classic-games-aladdin-and-the-lion-king)
- [Draw a Stickman: EPIC 2](https://yuzu-emu.org/game/draw-a-stickman-epic-2/) (draw-a-stickman-epic-2)
- [FIFA 21 Nintendo Switch™ Legacy Edition](https://yuzu-emu.org/game/fifa-21-nintendo-switch-legacy-edition/) (fifa-21-nintendo-switch-legacy-edition)
- [FINAL FANTASY® CRYSTAL CHRONICLES™ Remastered Edition](https://yuzu-emu.org/game/final-fantasy-r-crystal-chronicles-remastered-edition/) (final-fantasy-r-crystal-chronicles-remastered-edition)
- [Fire Emblem: Three Houses](https://yuzu-emu.org/game/fire-emblem-three-houses/) (fire-emblem-three-houses)
- [KILL la KILL -IF](https://yuzu-emu.org/game/kill-la-kill-if/) (kill-la-kill-if)
- [LEGO NINJAGO Movie Video Game](https://yuzu-emu.org/game/lego-ninjago-movie-video-game/) (lego-ninjago-movie-video-game)
- [LEGO The Incredibles](https://yuzu-emu.org/game/lego-the-incredibles/) (lego-the-incredibles)
- [LEGO Worlds](https://yuzu-emu.org/game/lego-worlds/) (lego-worlds)
- [Monster Energy Supercross - The Official Videogame](https://yuzu-emu.org/game/monster-energy-supercross-the-official-videogame/) (monster-energy-supercross-the-official-videogame)
- [Monster Jam Crush It!](https://yuzu-emu.org/game/monster-jam-crush-it/) (monster-jam-crush-it)
- [NAMCO MUSEUM (PAC-MAN VS. Free Multiplayer-only Ver.)](https://yuzu-emu.org/game/namco-museum-pac-man-vs-free-multiplayer-only-ver/) (namco-museum-pac-man-vs-free-multiplayer-only-ver)
- [Nights of Azure 2: Bride of the New Moon](https://yuzu-emu.org/game/nights-of-azure-2-bride-of-the-new-moon/) (nights-of-azure-2-bride-of-the-new-moon)
- [Octopath Traveler - Prologue Demo Version](https://yuzu-emu.org/game/octopath-traveler-prologue-demo-version/) (octopath-traveler-prologue-demo-version)
- [ONE PIECE: PIRATE WARRIORS 4](https://yuzu-emu.org/game/one-piece-pirate-warriors-4/) (one-piece-pirate-warriors-4)
- [Profane](https://yuzu-emu.org/game/profane/) (profane)
- [Redeemer: Enhanced Edition](https://yuzu-emu.org/game/redeemer-enhanced-edition/) (redeemer-enhanced-edition)
- [Retro Arcade Shooter - Attack from Pluto](https://yuzu-emu.org/game/retro-arcade-shooter-attack-from-pluto/) (retro-arcade-shooter-attack-from-pluto)
- [Rev Up! RC Grand Prix](https://yuzu-emu.org/game/rev-up-rc-grand-prix/) (rev-up-rc-grand-prix)
- [SEGA Genesis Classics](https://yuzu-emu.org/game/sega-genesis-classics/) (sega-genesis-classics)
- [Skellboy](https://yuzu-emu.org/game/skellboy/) (skellboy)
- [Slot](https://yuzu-emu.org/game/slot/) (slot)
- [Splatoon 2](https://yuzu-emu.org/game/splatoon-2/) (splatoon-2)
- [STEINS;GATE ELITE](https://yuzu-emu.org/game/steinsgate-elite/) (steinsgate-elite)
- [Street Fighter 30th Anniversary Collection](https://yuzu-emu.org/game/street-fighter-30th-anniversary-collection/) (street-fighter-30th-anniversary-collection)
- [Super Chariot](https://yuzu-emu.org/game/super-chariot/) (super-chariot)
- [Super Street: Racer](https://yuzu-emu.org/game/super-street-racer/) (super-street-racer)
- [SWORD ART ONLINE: Hollow Realization Deluxe Edition](https://yuzu-emu.org/game/sword-art-online-hollow-realization-deluxe-edition/) (sword-art-online-hollow-realization-deluxe-edition)
- [The Lost Child](https://yuzu-emu.org/game/the-lost-child/) (the-lost-child)
- [UNBOX: Newbie's Adventure](https://yuzu-emu.org/game/unbox-newbies-adventure/) (unbox-newbies-adventure)
- [Valkyria Chronicles 4](https://yuzu-emu.org/game/valkyria-chronicles-4/) (valkyria-chronicles-4)
- [Yesterday Origins](https://yuzu-emu.org/game/yesterday-origins/) (yesterday-origins)
<!-- MISSING ICONS END -->
