--Query 1--
SELECT
  SUBSTR(first_name, 1, 20) AS FIRST_NAME,
  SUBSTR(last_name, 1, 20) AS LAST_NAME,
  SUBSTR(nationality, 1, 20) AS NATIONALITY,
  SUBSTR(director_description, 1, 100) AS FILM_STYLE
FROM
  director d
WHERE nationality = 'American'
ORDER BY first_name;

--Query 2--
SELECT
  SUBSTR(m.title, 1, 30) AS movie_title,
  SUBSTR(d.first_name || ' ' || d.last_name, 1, 30) AS director,
  SUBSTR(g.genre, 1, 20) AS genre,
  SUBSTR(TO_CHAR (m.release_date, 'YYYY-MM-DD'),1,50) AS release
FROM
  movie m
JOIN
  director d ON m.director_id = d.director_id
JOIN
  genre g ON m.genre_id = g.genre_id
ORDER BY
  m.release_date;

--Query 3--
SELECT
  SUBSTR(g.genre, 1, 20) AS genre,
  COUNT(*) AS movie_count,
  AVG(m.rating) AS avg_rating
FROM
  movie m
JOIN
  genre g ON m.genre_id = g.genre_id
GROUP BY
  g.genre;

--Query 4--
SELECT
  SUBSTR(TO_CHAR(bill.bill_date, 'YYYY-MM-DD'), 1, 25) AS bill_date,
  SUBSTR(u.username, 1, 20) AS username,
  LISTAGG(SUBSTR(m.title, 1, 70), ', ') WITHIN GROUP (ORDER BY m.title) AS movies_purchased,
  SUBSTR(SUM(bill.order_total), 1, 20) AS total_order_amount
FROM
  billing bill
JOIN
  theUser u ON bill.user_id = u.user_id
JOIN
  billing_movies bm ON bill.transaction_id = bm.transaction_id
JOIN
  movie m ON bm.movie_id = m.movie_id
GROUP BY
  bill.bill_date, u.username
ORDER BY
  bill.bill_date DESC;

--Query 5--
SELECT
  RPAD(SUBSTR(u.username, 1, 20), 20) AS username,
  u.current_points,
  RPAD(SUBSTR(NVL(SUM(b.order_total), 0), 1, 20), 20) AS total_spent
FROM
  theUser u
LEFT JOIN
  billing b ON u.user_id = b.user_id
GROUP BY
  u.username, u.current_points
ORDER BY
  u.current_points DESC;