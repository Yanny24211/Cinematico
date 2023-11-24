import cx_Oracle

class drop_views:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'ahrahman', password='07076151', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """drop view movie_info;
drop view user_membership_status;
drop view top_rated_movies;"""
            for command in commands.replace('\n','').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            self.conn.close()
            #columns = [col[0] for col in c.description]
            #rows = [[cell for cell in row] for row in c]
            return "All Views Were Sucessfully Dropped"
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
        