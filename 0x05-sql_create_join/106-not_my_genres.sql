-- list all genres not linked to the show Dexter
SELECT DISTINCT name from tv_genres where name not in(
SELECT tv_genres.name  FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id and title = 'Dexter')
ORDER BY name;
