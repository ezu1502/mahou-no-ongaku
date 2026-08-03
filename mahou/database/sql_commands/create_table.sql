
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE NOT NULL, 
    title TEXT NOT NULL,
    times_played INTEGER DEFAULT 0
    );


    