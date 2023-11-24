import cx_Oracle

class query_5:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'ahrahman', password='07076151', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """SELECT
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
  u.current_points DESC;"""
            for command in commands.replace('\n',' ').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            columns = [col[0] for col in c.description]
            rows = [[cell for cell in row] for row in c]
            self.conn.close()
            return (columns,rows)
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
    