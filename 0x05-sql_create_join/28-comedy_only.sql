-- lists all Comedy shows
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id AND tv_genres.name = 'Comedy'
ORDER BY title;
