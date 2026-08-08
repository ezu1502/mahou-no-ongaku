
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE NOT NULL, 
    title TEXT NOT NULL,
    play_count INTEGER DEFAULT 0,
    listen_time REAL DEFAULT 0.0
    );




CREATE TABLE IF NOT EXISTS metadata (
    song_id INTEGER PRIMARY KEY, 

    artist TEXT,
    album TEXT,
    track_number INTEGER,
    genre TEXT,
    date TEXT, 
    
    FOREIGN KEY (song_id)
        REFERENCES songs(id)
        ON DELETE CASCADE
);