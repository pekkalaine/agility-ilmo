# Käyttötapaukset ja niihin liittyvät tietokantakyselyt


## Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasanan

INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);



## Käyttäjä voi kirjautua sivulle

SELECT account.id, account.date_created, account.date_modified, account_name, account_username, account.password
FROM account
WHERE account.username = ? AND account.password = ?;



## Käyttäjä voi lisätä itselleen koiran

INSERT INTO dog (date_created, date_modified, name, race, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);



## Käyttäjä voi tarkastella listaa kaikista koiristaan

SELECT Dog.id, Dog.name, Dog.race FROM Dog WHERE Dog.account_id  =  ?;



## Käyttäjä voi päivittää koiran tietoja

UPDATE dog SET date_modified=CURRENT_TIMESTAMP, name=?, race=? 
WHERE dog.id = ?;



## Käyttäjä voi poistaa koiran (poistettuaan ensin koiran ilmoittautumiset)

DELETE FROM dog WHERE dog.id = ?;



## Käyttäjä voi tarkastella yksittäisen koiransa ilmoittautumisia

SELECT * FROM Enrolment WHERE Enrolment.dog_id  =  ?;



## Käyttäjä voi ilmoittaa koiransa kurssille, jos kurssilla on tilaa

INSERT INTO enrolment (dog_name, course_name, course_id, dog_id) VALUES (?, ?, ?, ?);



## Käyttäjä voi poistaa oman koiransa ilmoittautumisen

DELETE FROM enrolment WHERE enrolment.id = ?;



## Käyttäjä voi tarkastella listaa kaikista kursseista

SELECT * FROM course;



## Käyttäjä voi lisätä kurssin

INSERT INTO course (date_created, date_modified, name, description, max_participants) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);



## Käyttäjä voi päivittää kurssin tietoja

UPDATE course SET date_modified=CURRENT_TIMESTAMP, name=?, description=?, max_participants=? WHERE course.id = ?;



## Käyttäjä voi poistaa kurssin (jos kurssille ei ole ilmoittautunut koiria)

DELETE FROM course WHERE course.id = ?;



## Käyttäjä voi tarkastella listaa kurssille ilmoitetuista koirista

SELECT Dog.id, Dog.name, Dog.race, dog.account_id FROM Dog 

LEFT JOIN Enrolment ON Enrolment.dog_id = Dog.id 

WHERE (Enrolment.course_id  =  ?) 

GROUP BY Dog.id;



## Käyttäjä voi tarkastella listaa kaikista asiakkaista ja näiden koirista

Tämä on toteutettu kahdella eri tietokantakyselyllä:

SELECT * FROM account;

SELECT * FROM dog;

HTML-näkymä luodaan siten, että kunkin asiakkaan kohdalla loopataan koiralista läpi ja valitaan kunkin asiakkaan kohdalle koirat, joiden foreign keynä on ko. asiakkaan id. Ei ehkä kaikkein elegantein ratkaisu...



## Käyttäjä voi hakea asiakkaita koiran rodun perusteella

SELECT Account.id, Account.name FROM Account 

LEFT JOIN Dog ON Dog.account_id = Account.id

WHERE (Dog.race  =  ?) 

GROUP BY Account.id;
