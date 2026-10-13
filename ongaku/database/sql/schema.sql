CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE NOT NULL,

    play_count INTEGER NOT NULL DEFAULT 0,
    listen_time REAL NOT NULL DEFAULT 0,

    date TEXT,
    track_number TEXT,

    title TEXT
);

CREATE TABLE IF NOT EXISTS artists (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS song_artists (
    song_id INTEGER NOT NULL
        REFERENCES songs(id) ON DELETE CASCADE,

    artist_id INTEGER NOT NULL
        REFERENCES artists(id) ON DELETE CASCADE,

    PRIMARY KEY (song_id, artist_id)

);

CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY,

    name TEXT NOT NULL,
    date TEXT
);

CREATE TABLE IF NOT EXISTS song_albums (
    song_id INTEGER NOT NULL
        REFERENCES songs(id) ON DELETE CASCADE,

    album_id INTEGER NOT NULL
        REFERENCES albums(id) ON DELETE CASCADE,

    PRIMARY KEY (song_id, album_id)

);

CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS song_playlists (
    song_id INTEGER NOT NULL
        REFERENCES songs(id) ON DELETE CASCADE,

    playlist_id INTEGER NOT NULL
        REFERENCES playlists(id) ON DELETE CASCADE,

    position INTEGER,

    PRIMARY KEY (song_id, playlist_id)
);
