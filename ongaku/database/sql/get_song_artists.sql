
SELECT name FROM artists
WHERE id in (
    SELECT artist_id FROM song_artists
    WHERE song_id IN (
        SELECT id FROM songs
        WHERE path = ?
    )
);