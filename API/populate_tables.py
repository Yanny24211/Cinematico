import cx_Oracle

class populate_tables:

    def __init__(self):
        dsn = cx_Oracle.makedsn('oracle.scs.ryerson.ca', '1521', 'orcl')
        self.conn = cx_Oracle.connect(user=r'ahrahman', password='07076151', dsn=dsn)

    def run(self):
        c = self.conn.cursor()
        try:
            commands = """
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (1, 'English');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (2, 'Spanish');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (3, 'French');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (4, 'Mandarin Chinese');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (5, 'Hindi');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (6, 'Japanese');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (7, 'Korean');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (8, 'German');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (9, 'Italian');
INSERT INTO thelanguage (LANGUAGE_ID, THELANGUAGE) VALUES (10, 'Russian');

INSERT INTO genre(GENRE_ID, GENRE)  VALUES  (1, 'Comedy');
INSERT INTO genre (genre_id, genre) VALUES (2, 'Adventure');
INSERT INTO genre (genre_id, genre) VALUES (3, 'Animation');
INSERT INTO genre (genre_id, genre) VALUES (4, 'Action');
INSERT INTO genre (genre_id, genre) VALUES (5, 'Crime');
INSERT INTO genre (genre_id, genre) VALUES (6, 'Drama');
INSERT INTO genre (genre_id, genre) VALUES (7, 'Fantasy');
INSERT INTO genre (genre_id, genre) VALUES (8, 'Horror');
INSERT INTO genre (genre_id, genre) VALUES (9, 'Mystery');
INSERT INTO genre (genre_id, genre) VALUES (10, 'Romance');
INSERT INTO genre (genre_id, genre) VALUES (11, 'Science Fiction');
INSERT INTO genre (genre_id, genre) VALUES (12, 'Thriller');
INSERT INTO genre (genre_id, genre) VALUES (13, 'Documentary');
INSERT INTO genre (genre_id, genre) VALUES (14, 'Family');
INSERT INTO genre (genre_id, genre) VALUES (15, 'Historical');
INSERT INTO genre (genre_id, genre) VALUES (16, 'Musical');
INSERT INTO genre (genre_id, genre) VALUES (17, 'War');
INSERT INTO genre (genre_id, genre) VALUES (18, 'Western');

INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (0, 'John', 'Dars', 'USA', 'Visionary maestro of laughter, crafting comedic masterpieces that tickle the funny bone and warm the heart.', TO_DATE('1970-01-01', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (2, 'Christopher', 'Nolan', 'British', 'Acclaimed filmmaker known for mind-bending narratives and innovative visuals.', TO_DATE('1970-07-30', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (3, 'Francis Ford', 'Coppola', 'American', 'Legendary director behind The Godfather trilogy.', TO_DATE('1939-04-07', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (4, 'Quentin', 'Tarantino', 'American', 'Renowned for his unique storytelling and dialogue.', TO_DATE('1963-03-27', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (5, 'Steven', 'Spielberg', 'American', 'Iconic filmmaker with a diverse range of blockbuster hits.', TO_DATE('1946-12-18', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (6, 'Frank', 'Darabont', 'American', 'Known for his work on The Shawshank Redemption and The Green Mile.', TO_DATE('1959-01-28', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (7, 'Peter', 'Jackson', 'New Zealander', 'Acclaimed director of The Lord of the Rings trilogy.', TO_DATE('1961-10-31', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (8, 'David', 'Fincher', 'American', 'Known for his work on Se7en and Fight Club.', TO_DATE('1962-08-28', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (9, 'Ridley', 'Scott', 'British', 'Renowned director with classics like Blade Runner and Gladiator.', TO_DATE('1937-11-30', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (10, 'Stanley', 'Kubrick', 'American', 'Influential filmmaker with masterpieces like 2001: A Space Odyssey.', TO_DATE('1928-07-26', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (11, 'Alfred', 'Hitchcock', 'British', 'Master of suspense with classics like Rear Window and Psycho.', TO_DATE('1899-08-13', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (12, 'Josh', 'Cooley', 'American', 'Animation', TO_DATE('1979-05-23', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (13, 'Rob', 'Minkoff', 'American', 'Animation', TO_DATE('1962-08-11', 'YYYY-MM-DD'));
INSERT INTO director(DIRECTOR_ID, FIRST_NAME, LAST_NAME, NATIONALITY, DIRECTOR_DESCRIPTION, DATE_OF_BIRTH) VALUES (14, 'Barry', 'Jenkins', 'American', 'Drama',TO_DATE('1979-11-19', 'YYYY-MM-DD'));

INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (5, 'Cinematic Creations', 'Specializing in visually stunning and emotionally resonant films', 'Laugh Fest');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (1, 'Warner Bros. Pictures', 'Major film studio known for producing a wide range of blockbuster movies.','The Shawshank Redemption (1994), The Dark Knight (2008), Inception (2010), Interstellar (2014), The Matrix (1999), The Lord of the Rings: The Fellowship of the Ring (2001), The Departed (2006), The Prestige (2006), The Dark Knight (2008), Inception (2010), The Social Network (2010), The Shape of Water (2017), Mad Max: Fury Road (2015), Dunkirk (2017), Gravity (2013), Blade Runner 2049 (2017), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (2, 'Paramount Pictures', 'Major film studio with a rich history of producing iconic films.','The Godfather (1972), Forrest Gump (1994), Titanic (1997), Saving Private Ryan (1998), Gladiator (2000), Transformers (2007), Inglourious Basterds (2009), Interstellar (2014), Transformers: Dark of the Moon (2011), The Godfather Part III (1990), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (3, 'Universal Pictures', 'One of the oldest film studios with a diverse range of film productions.','Jurassic Park (1993), E.T. the Extra-Terrestrial (1982), Jaws (1975), Schindler\''s List (1993), The Princess Bride (1987), The Mummy (1999), Gladiator (2000), The Dark Knight (2008), Inception (2010), Jurassic World (2015), Despicable Me (2010), Fast and Furious series, and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (4, '20th Century Studios', 'Major film studio with a focus on producing successful and impactful films.','Deadpool (2016), Avatar (2009), The Sound of Music (1965), The Grand Budapest Hotel (2014), Star Wars: Episode IV - A New Hope (1977), The Martian (2015), Bohemian Rhapsody (2018), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (6, 'Columbia Pictures', 'One of the major film studios known for a variety of film genres.','Men in Black (1997), Spider-Man (2002), The Social Network (2010), Whiplash (2014), The Dark Knight (2008), Inception (2010), Ghostbusters (1984), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (7, 'Dreamworks Animation', 'Specializing in animated films with compelling storytelling and innovative animation techniques.', 'Shrek (2001), How to Train Your Dragon (2010), Madagascar (2005), Kung Fu Panda (2008), Trolls (2016), The Prince of Egypt (1998), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (8, 'Pixar Animation Studios', 'Renowned for its computer-animated feature films and short films with emotional storytelling and cutting-edge animation technology.', 'Toy Story (1995), Finding Nemo (2003), Up (2009), Inside Out (2015), Coco (2017), The Incredibles (2004), Monsters, Inc. (2001), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (9, 'Walt Disney Studios', 'A global leader in family entertainment, producing a wide range of animated and live-action films.', 'The Lion King (1994), Frozen (2013), Beauty and the Beast (1991), Aladdin (1992), The Little Mermaid (1989), Moana (2016), Mulan (1998), and many more');
INSERT INTO productioncompany(COMPANY_ID, COMPANY_NAME, FILMSTYLE_INFO, MOVIES) VALUES (10, 'A24', 'An independent entertainment company known for producing critically acclaimed films with a focus on artistic and innovative storytelling.', 'Moonlight (2016), Lady Bird (2017), Hereditary (2018), Ex Machina (2014), The Florida Project (2017), A Ghost Story (2017), and many more');

INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (2, 'Laugh Fest', 'USA', 144, 25.99, 'HD', TO_DATE('2023-11-15', 'YYYY-MM-DD'), 4.5, 'A hilarious comedy for all ages', 1, 0, 1, 5);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (1, 'The Shawshank Redemption', 'USA', 142, 10.99, 'HD', TO_DATE('1994-09-23', 'YYYY-MM-DD'), 9.3, 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 6, 6, 1, 1);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (4, 'The Godfather', 'USA', 175, 30.0, '70mm Film', TO_DATE('1972-03-24', 'YYYY-MM-DD'), 9.2, 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 5, 3, 1, 2);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (3, 'Pulp Fiction', 'USA', 154, 28.0, '4K UHD', TO_DATE('1994-10-14', 'YYYY-MM-DD'), 8.9, 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 6, 4, 1, 5);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (5, 'Inception', 'USA', 148, 29.99, '4K UHD', TO_DATE('2010-07-16', 'YYYY-MM-DD'), 8.8, 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 11, 2, 1, 1);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (6, 'Shrek', 'USA', 90, 19.99, 'HD', TO_DATE('2001-04-22', 'YYYY-MM-DD'), 7.8, 'An ogre and his new friend embark on a journey to rescue Princess Fiona from a dragon and reclaim the deeds to their land.', 3, 7, 1, 7);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (7, 'Toy Story', 'USA', 81, 22.99, 'HD', TO_DATE('1995-11-22', 'YYYY-MM-DD'), 8.3, 'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\''s room.', 3, 12, 1, 8);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (8, 'The Lion King', 'USA', 88, 24.99, '4K UHD', TO_DATE('1994-06-15', 'YYYY-MM-DD'), 8.5, 'A young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.', 3, 13, 1, 9);
INSERT INTO movie(movie_id, title, country_origin, runtime, thecost, video_format, release_date, rating, movie_description, genre_id, director_id, language_id, company_id) VALUES (9, 'Moonlight', 'USA', 111, 27.0, '4K UHD', TO_DATE('2016-10-21', 'YYYY-MM-DD'), 7.4, 'A young African-American man grapples with his identity and sexuality while experiencing the everyday struggles of childhood to adulthood.', 6, 14, 1, 10);

INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (1, 'john_doe', 'John', 'Doe', 150, 'john.doe@example.com', TO_DATE('1992-05-15', 'YYYY-MM-DD'), 'securepassword123');
INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (2, 'mary_smith', 'Mary', 'Smith', 300, 'mary.smith@example.com', TO_DATE('1985-09-28', 'YYYY-MM-DD'), 'marys_password456');
INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (3, 'sam_jones', 'Sam', 'Jones', 450, 'sam.jones@example.com', TO_DATE('1990-12-10', 'YYYY-MM-DD'), 'sam_secure789');
INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (4, 'emily_jackson', 'Emily', 'Jackson', 150, 'emily.jackson@example.com', TO_DATE('1995-07-18', 'YYYY-MM-DD'), 'emily_pass321');
INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (5, 'alex_wilson', 'Alex', 'Wilson', 0, 'alex.wilson@example.com', TO_DATE('1988-02-22', 'YYYY-MM-DD'), 'alex_password567');
INSERT INTO theUser (USER_ID, USERNAME, FNAME, LNAME, CURRENT_POINTS, EMAIL, DATE_OF_BIRTH, PASSKEY) VALUES (6, 'sara_miller', 'Sara', 'Miller', 150, 'sara.miller@example.com', TO_DATE('1993-10-05', 'YYYY-MM-DD'), 'sara_secure890');

INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (1, TO_DATE('2023-09-30', 'YYYY-MM-DD'), 'john_doe', 'john.doe@example.com', 25.99, 'Credit Card', 1);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (2, TO_DATE('2023-09-30', 'YYYY-MM-DD'), 'mary_smith', 'mary.smith@example.com', 28.0, 'PayPal', 2);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (3, TO_DATE('2023-09-30', 'YYYY-MM-DD'), 'mary_smith', 'mary.smith@example.com', 25.99, 'PayPal', 2);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (4, TO_DATE('2022-08-10', 'YYYY-MM-DD'), 'sam_jones', 'sam.jones@example.com', 10.99, 'Credit Card', 3);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (5, TO_DATE('2022-08-10', 'YYYY-MM-DD'), 'sam_jones', 'sam.jones@example.com', 30.0, 'Credit Card', 3);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (6, TO_DATE('2022-08-10', 'YYYY-MM-DD'), 'sam_jones', 'sam.jones@example.com', 28.0, 'Credit Card', 3);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (7, TO_DATE('2022-08-10', 'YYYY-MM-DD'), 'sam_jones', 'sam.jones@example.com', 25.99, 'Credit Card', 3);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (8, TO_DATE('2023-09-15', 'YYYY-MM-DD'), 'emily_jackson', 'emily.jackson@example.com', 25.99, 'PayPal', 4);
INSERT INTO billing(TRANSACTION_ID, BILL_DATE, USERNAME, EMAIL, ORDER_TOTAL, PAYMENT_METHOD, USER_ID) VALUES (9, TO_DATE('2023-07-05', 'YYYY-MM-DD'), 'sara_miller', 'sara.miller@example.com', 30.0, 'PayPal', 6);

INSERT INTO movie_actor(movie_id, actor_name) VALUES (1, 'Tim Robbins');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (1, 'Morgan Freeman');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (4, 'Marlon Brando');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (4, 'Al Pacino');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (3, 'John Travolta');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (3, 'Uma Thurman');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (5, 'Leonardo DiCaprio');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (5, 'Elliot Page');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (6, 'Mike Myers');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (6, 'Eddie Murphy');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (6, 'Cameron Diaz');
INSERT INTO movie_actor(movie_id, actor_name) VALUES (6, 'John Lithgow');

INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (1, 1, 2);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (2, 2, 3);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (3, 2, 2);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (4, 3, 1);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (5, 3, 4);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (6, 3, 3);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (7, 3, 2);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (8, 4, 2);
INSERT INTO billing_movies (transaction_id, user_id, movie_id) VALUES (9, 6, 4);
"""

            for command in commands.replace('\n','').replace('    ','').split(';'):
                if command != '':
                    c.execute(command)

            self.conn.commit()
            self.conn.close()
            #columns = [col[0] for col in c.description]
            #rows = [[cell for cell in row] for row in c]
            return "All Tables Were Sucessfully Populated"
        except Exception as e:
            error_obj, = e.args
            self.conn.rollback()
            self.conn.close()
            return ("Error: " + error_obj.message)
        