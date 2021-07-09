const fs = require('fs');
const {
    getGamesAmerica,
    getGamesEurope,
    getGamesJapan,
    getQueriedGamesAmerica,
    parseGameCode
} = require('nintendo-switch-eshop');


var game_nsuid = {},
    game_america = [], game_europe = [], game_japan = [];

// console.log('Getting games (America)...');
// getGamesAmerica({
//     locale: 'en',
// }).then(game_america => {
    
    console.log('Getting games (Europe)...');
    getGamesEurope({
        locale: 'en',
        // limit: 1
    }).then(game_europe => {

        // console.log('Getting games (Japan)...');
        // getGamesJapan({
        //     locale: 'en',
        //     // limit: 1
        // }).then(game_japan => {
            
            let games = game_america.concat(game_europe).concat(game_japan);

            console.log(games);

            // games = games.slice(0, 3);

            console.log('Found', games.length, 'games');

            // for (let game of games) {
            //     game_nsuid[game["nsuid"]] = game;
            // }

            // var count = 0;
            // for (var i in game_nsuid)  if (game_nsuid.hasOwnProperty(i)) ++count;

            // console.log('Extracted', count, 'NSUIDs');

            game_nsuid = games;

            fs.writeFile('eshop_games.json', JSON.stringify(game_nsuid, null, '\t'), (err) => {
                if (err) throw err;
                console.log('Finished');
            });
        
        // })
    // })
});