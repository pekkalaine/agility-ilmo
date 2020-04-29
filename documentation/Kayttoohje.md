## Sovelluksen käyttäminen

Sovellukseen voi luoda käyttäjätunnuksen, jolla sovellukseen kirjaudutaan. Sovellukseen voi lisätä koiria lisää koira -näkymästä. Sovellukseen voi lisätä kursseja lisää kurssi -näkymästä. 

**Listaa koirat -näkymä**

Omien koirien tiedot saa näkyviin Listaa koirat -näkymästä. Näkymästä pääsee myös päivittämään koiran tietoja tai poistamaan koiran. Koiran voi poistaa vain jos sillä ei ole ilmoittautumisia, eli ennen poistamista pitää ilmoittautumiset perua. Tässä näkymässä tapahtuu myös kursseille ilmoittautuminen alasvetovalikosta. Näkymästä pääsee napin kautta tarkastelemaan kaikkia yksittäisten kirjautuneen käyttäjän omien koirien ilmoittautumisia. Ilmoittautumislistauksessa on myös ilmoittautumisten perumismahdollisuus.

**Listaa kurssit -näkymä**

Kaikki sovellukseen tallennetut kurssit ovat Listaa kurssit -näkymässä. Täällä tapahtuu myös kurssin tietojen päivittäminen ja kurssin poistaminen. Kurssin osallistujamäärää ei pysty päivittämään alhaisemmaksi kuin mikä on kurssille jo ilmoitettujen koirien lukumäärä. Kurssia ei myöskään voi poistaa, jos sille on ilmoittautunut koiria. Tästä näkymästä saa napin kautta näkyviin myös kaikki kurssille ilmoittautuneet koirat. Tämän listauksen kautta käyttäjä voi perua omien koiriensa ilmoittautumisia mutta ei muiden.

**Listaa käyttäjät -näkymä**

Tässä näkymässä listataan kaikki sovellukseen lisätyt käyttäjät ja heidän koiransa. Täällä on myös hakutoiminto, jolla voi etsiä käyttäjiä, joilla on sovellukseen lisättynä jonkin tietyn rodun koiria. 


## Sovelluksen asentaminen paikallisesti

Kun sovelluksen zipin on ladannut koneelleen esim. Githubista ja purkanut sen, saa sovelluksen riippuvuudet käyttöönsä menemällä komentorivillä sovelluksen juureen ja antamalla käskyn `pip install -r requirements.txt`. Tämä toki edellyttää että asennettavalla koneella on pip. Myös tuki Python-kielisten ohjelmien suorittamiseen tarvitaan. Lisäksi lienee hyvä idea että virtuaaliympäristö on luotuna.  Tämän jälkeen sovelluksen saa käynnistettyä komennolla `py run.py`. Nyt sovellus on käytettävissä selaimella osoitteessa http://localhost:5000.

## Sovelluksen asentaminen Herokuun

Tässä oletetaan että käytössä on git sekä Herokun työvälineet komentoriville ja että sovelluskansiosta on tehty paikallinen repositorio.


Luodaan sovellukselle paikka Herokuun (Kohdan agility-ilmo tilalle pitää laittaa jotain muuta, koska nimi on jo varattu):

`heroku create agility-ilmo`


Lisätään paikalliseen versionhallintaan tieto siitä, että sovellus on Herokussa

`git remote add heroku https://git.heroku.com/agility-ilmo.git`


Lähetetään sovellus Herokuun:

`git add .`

`git commit -m "Sovellus Herokuun"`

`git push heroku master`


Lisätään sovelluksen käyttöön tieto siitä, että sovellus on Herokussa:
`heroku config:set HEROKU=1`


Lisätään Herokuun PostgreSQL-tietokanta:

`heroku addons:add heroku-postgresql:hobby-dev`