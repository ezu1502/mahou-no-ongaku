
INSERT INTO songs (path, title)
VALUES (?, ?)
ON CONFLICT(path) DO NOTHING;