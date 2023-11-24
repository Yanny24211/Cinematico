CREATE VIEW movie_info AS
SELECT
  m.title AS movie_title,
  m.movie_description,
  m.thecost AS Purchase_Cost,
  g.genre
FROM
  movie m
JOIN
  genre g ON m.genre_id = g.genre_id;


CREATE VIEW user_membership_status AS
SELECT
  u.username,
  u.current_points,
  CASE
    WHEN u.current_points >= 500 THEN 'Gold'
    WHEN u.current_points >= 300 THEN 'Silver'
    ELSE 'Bronze'
  END AS membership_status
FROM
  theUser u;


CREATE VIEW top_rated_movies AS
SELECT
  m.title AS movie_title,
  m.rating
FROM
  movie m
WHERE
  m.rating >= 8.0;

SELECT*FROM movie_info;
SELECT*FROM user_membership_status; 
SELECT*FROM top_rated_movies; 

drop view movie_info;
drop view user_membership_status;
drop view top_rated_movies;