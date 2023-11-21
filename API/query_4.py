import cx_Oracle

class query_4:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'yspatel', password='05182555', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """SELECT
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
  bill.bill_date DESC;"""
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