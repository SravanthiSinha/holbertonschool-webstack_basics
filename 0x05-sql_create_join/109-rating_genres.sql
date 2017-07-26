--  lists all genres from hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating FROM tv_shows, tv_show_ratings, tv_genres, tv_show_genres
WHERE tv_shows.id = tv_show_ratings.show_id AND tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id 
GROUP BY name ORDER BY rating DESC;
