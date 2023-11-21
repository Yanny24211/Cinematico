import cx_Oracle

class create_tables:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'yspatel', password='05182555', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """CREATE TABLE billing (
    transaction_id       INTEGER NOT NULL PRIMARY KEY,
    bill_date            DATE(10),
    username             VARCHAR(500),
    email                VARCHAR(500),
    order_total          FLOAT,
    payment_method       VARCHAR(500),
    user_id              INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES theUser(user_id)
);

CREATE TABLE director (
    director_id          INTEGER NOT NULL PRIMARY KEY,
    first_name           VARCHAR(500),
    last_name            VARCHAR(500),
    nationality          VARCHAR(500),
    director_description CLOB,
    date_of_birth        DATE(10)
);

CREATE TABLE genre (
    genre_id       INTEGER NOT NULL PRIMARY KEY,
    genre          VARCHAR2(300 CHAR)
);

CREATE TABLE thelanguage (
    language_id    INTEGER NOT NULL PRIMARY KEY,
    thelanguage       VARCHAR(500)
);

CREATE TABLE movie (
    movie_id                        INTEGER NOT NULL PRIMARY KEY,
    title                           VARCHAR(500),
    country_origin                  VARCHAR(500),
    runtime                         DATE(10),
    thecost                         FLOAT(5),
    video_format                    VARCHAR(500),
    relese_date                     DATE(10),
    rating                          FLOAT(1),
    movie_description               CLOB,
    genre_id                        INTEGER NOT NULL,
    director_id                     INTEGER NOT NULL,
    language_id                     INTEGER NOT NULL,
    company_id                      INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (director_id) REFERENCES director ( director_id ),
    FOREIGN KEY (language_id) REFERENCES theLanguage(language_id),
    FOREIGN KEY (company_id) REFERENCES productioncompany(company_id)
);

CREATE TABLE productioncompany (
    company_id          INTEGER NOT NULL PRIMARY KEY,
    company_name        VARCHAR(500),
    filmstyle_info      CLOB,
    movies              VARCHAR(500)
);

CREATE TABLE theUser (
    user_id                 INTEGER NOT NULL PRIMARY KEY,
    username                VARCHAR(500),
    fname                   VARCHAR(500),
    lname                   VARCHAR(500),
    current_points          FLOAT,
    email                   VARCHAR(500),
    date_of_birth           DATE(10),
    passkey                 VARCHAR(500)

);

CREATE TABLE billing_movies (
    transaction_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    PRIMARY KEY (transaction_id, user_id, movie_id),
    FOREIGN KEY (transaction_id) REFERENCES billing (TRANSACTION_ID),
    FOREIGN KEY (user_id) REFERENCES theUser (USER_ID),
    FOREIGN KEY (movie_id) REFERENCES movie (MOVIE_ID)
);

CREATE TABLE movie_actor (
    movie_id INTEGER NOT NULL,
    actor_name VARCHAR(500) NOT NULL,
    PRIMARY KEY (movie_id, actor_name),
    FOREIGN KEY (movie_id) REFERENCES movie (movie_id)
);"""
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
        return "All Tables Were Sucessfully Produced"