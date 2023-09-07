-- That script list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT tv_show_genres.genre_id
	FROM tv_show_genres, tv_shows
	WHERE tv_show_genres.show_id = tv_shows.id && tv_shows.title = "Dexter"
	GROUP BY tv_show_genres.genre_id)
ORDER BY tv_genres.name; 
