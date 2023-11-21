import cx_Oracle

class drop_tables:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'yspatel', password='05182555', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """drop table billing cascade constraints purge;
drop table director cascade constraints purge;
drop table genre cascade constraints purge;
drop table thelanguage cascade constraints purge;
drop table movie cascade constraints purge;
drop table productioncompany cascade constraints purge;
drop table theUser cascade constraints purge;
drop table billing_movies cascade constraints purge;
drop table movie_actor cascade constraints purge;"""
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
        return "All Tables Were Sucessfully Dropped"