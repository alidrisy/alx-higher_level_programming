-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_shows.title, tv_genres.name
from tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
