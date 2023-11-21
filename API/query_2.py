import cx_Oracle

class query_2:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'yspatel', password='05182555', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """SELECT
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
  m.release_date;"""
            for command in commands.replace('\n',' ').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            columns = [col[0] for col in c.description]
            rows = [[cell for cell in row] for row in c]
            self.conn.close()
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
        return (columns,rows)