
INSERT INTO song (path, title)
VALUES (?, ?)
ON CONFLICT(path) DO NOTHING;