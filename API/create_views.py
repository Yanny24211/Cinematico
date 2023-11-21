import cx_Oracle

class create_views:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'yspatel', password='05182555', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """CREATE VIEW movie_info AS
SELECT
  m.title AS movie_title,
  m.runtime,
  m.rating,
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
  m.rating >= 8.0;"""
            for command in commands.replace('\n','').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            self.conn.close()
            #columns = [col[0] for col in c.description]
            #rows = [[cell for cell in row] for row in c]
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
        return "All Views Were Sucessfully Produced"