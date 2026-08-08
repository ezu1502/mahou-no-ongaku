
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE NOT NULL, 
    title TEXT NOT NULL,
    play_count INTEGER DEFAULT 0,
    listen_time REAL DEFAULT 0.0
    );


