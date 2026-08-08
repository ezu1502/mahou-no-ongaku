
SELECT *
FROM songs
LEFT JOIN metadata
    on songs.id = metadata.song_id
ORDER BY title COLLATE NOCASE;


