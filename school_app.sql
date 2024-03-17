DROP TABLE IF EXISTS student;
CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT
);

COPY student FROM '/Users/crystaljobe/code_platoon/week-four-modules/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(20)
);

COPY subjects FROM '/Users/crystaljobe/code_platoon/week-four-modules/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT
);

COPY teachers FROM '/Users/crystaljobe/code_platoon/week-four-modules/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;
