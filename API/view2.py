import cx_Oracle

class view2:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'ahrahman', password='07076151', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            command = "SELECT * FROM TOP_RATED_MOVIES"
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
    