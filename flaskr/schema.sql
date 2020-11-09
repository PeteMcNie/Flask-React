-- 3: Define how database table will look
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS stats;

CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    playername TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stat_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    attack INTEGER NOT NULL,
    staminer INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    passing INTEGER NOT NULL,
    tackling INTEGER NOT NULL,
    special TEXT NOT NULL,
    FOREIGN KEY (stat_id) REFERENCES player (id)
);