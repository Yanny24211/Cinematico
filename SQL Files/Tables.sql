CREATE TABLE director (
    director_id          INTEGER NOT NULL PRIMARY KEY,
    first_name           VARCHAR2(500),
    last_name            VARCHAR2(500),
    nationality          VARCHAR2(500),
    director_description VARCHAR2(3000),
    date_of_birth        DATE
);

CREATE TABLE genre (
    genre_id       INTEGER NOT NULL PRIMARY KEY,
    genre          VARCHAR2(300 CHAR)
);

CREATE TABLE thelanguage (
    language_id    INTEGER NOT NULL PRIMARY KEY,
    thelanguage       VARCHAR2(500)
);

CREATE TABLE productioncompany (
    company_id          INTEGER NOT NULL PRIMARY KEY,
    company_name        VARCHAR2(500),
    filmstyle_info      VARCHAR2(3000),
    movies              VARCHAR2(500)
);

CREATE TABLE theUser (
    user_id                 INTEGER NOT NULL PRIMARY KEY,
    username                VARCHAR2(500),
    fname                   VARCHAR2(500),
    lname                   VARCHAR2(500),
    current_points          NUMBER,
    email                   VARCHAR2(500),
    date_of_birth           DATE,
    passkey                 VARCHAR2(500)

);

CREATE TABLE billing (
    transaction_id       INTEGER NOT NULL PRIMARY KEY,
    bill_date            DATE,
    username             VARCHAR2(500),
    email                VARCHAR2(500),
    order_total          NUMBER,
    payment_method       VARCHAR2(500),
    user_id              INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES theUser(user_id) ON DELETE CASCADE
);

CREATE TABLE movie (
    movie_id                        INTEGER NOT NULL PRIMARY KEY,
    title                           VARCHAR2(500),
    country_origin                  VARCHAR2(500),
    runtime                         NUMBER,
    thecost                         NUMBER(5, 2),
    video_format                    VARCHAR2(500),
    release_date                    DATE,
    rating                          NUMBER(2),
    movie_description               VARCHAR2(3000),
    genre_id                        INTEGER NOT NULL,
    director_id                     INTEGER NOT NULL,
    language_id                     INTEGER NOT NULL,
    company_id                      INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (director_id) REFERENCES director ( director_id ) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES theLanguage(language_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES productioncompany(company_id) ON DELETE CASCADE
);

CREATE TABLE billing_movies (
    transaction_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    PRIMARY KEY (transaction_id, user_id, movie_id),
    FOREIGN KEY (transaction_id) REFERENCES billing (TRANSACTION_ID) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES theUser (USER_ID) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movie (MOVIE_ID) ON DELETE CASCADE
);

CREATE TABLE movie_actor (
    movie_id INTEGER NOT NULL,
    actor_name VARCHAR2(500) NOT NULL,
    PRIMARY KEY (movie_id, actor_name),
    FOREIGN KEY (movie_id) REFERENCES movie (movie_id) ON DELETE CASCADE
);

drop table billing cascade constraints purge;
drop table director cascade constraints purge;
drop table genre cascade constraints purge;
drop table thelanguage cascade constraints purge;
drop table movie cascade constraints purge;
drop table productioncompany cascade constraints purge;
drop table theUser cascade constraints purge;
drop table billing_movies cascade constraints purge;
drop table movie_actor cascade constraints purge;