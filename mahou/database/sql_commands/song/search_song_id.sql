
SELECT *
FROM songs
LEFT JOIN metadata
    ON songs.id = metadata.song_id
WHERE id = ?;