-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title, tv_genres.name;
