-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT tv_show_genres.show_id
	FROM tv_show_genres, tv_genres
	WHERE tv_show_genres.genre_id = tv_genres.id && tv_genres.name = "Comedy"
	GROUP BY tv_show_genres.show_id)
ORDER BY tv_shows.title;
