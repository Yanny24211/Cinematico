import cx_Oracle

class query_1:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'ahrahman', password='07076151', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """SELECT
  SUBSTR(first_name, 1, 20) AS FIRST_NAME,
  SUBSTR(last_name, 1, 20) AS LAST_NAME,
  SUBSTR(nationality, 1, 20) AS NATIONALITY,
  SUBSTR(director_description, 1, 100) AS FILM_STYLE
FROM
  director d
WHERE nationality = 'American'
ORDER BY first_name;"""
            for command in commands.replace('\n',' ').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            columns = [col[0] for col in c.description]
            rows = [[cell for cell in row] for row in c]
            #print("Columns: ", columns, "Rows: ", rows)
            self.conn.close()
            return (columns,rows)
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
        