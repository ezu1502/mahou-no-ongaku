

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
)   