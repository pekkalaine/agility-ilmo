## Tietokantataulut ja niiden Create table -lauseet

**Käyttäjä**
* (pk) id: int
* nimi: string
* käyttäjätunnus: string
* salasana: string
* yhteystiedot: string

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(200) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
)


**Koira**
* (pk) id: int
* (fk) käyttäjä_id: Käyttäjä
* nimi: string
* rotu: string

CREATE TABLE dog (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(200) NOT NULL,
        race VARCHAR(200) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)

**Kurssi**
* (pk) id: int
* nimi: string
* kurssikuvaus: string
* maksimi osallistujamäärä: int

CREATE TABLE course (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(200) NOT NULL,
        description VARCHAR(400) NOT NULL,
        max_participants INTEGER NOT NULL,
        PRIMARY KEY (id)
)


**Kurssi-ilmoittautuminen**
* (fk) koira_id: Koira
* (fk) kurssi_id: Kurssi

CREATE TABLE enrolment (
        id INTEGER NOT NULL,
        dog_name VARCHAR(200) NOT NULL,
        course_name VARCHAR(200) NOT NULL,
        course_id INTEGER NOT NULL,
        dog_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(course_id) REFERENCES course (id),
        FOREIGN KEY(dog_id) REFERENCES dog (id)
)