# Agility-ilmo

[Sovellus Herokussa](https://agility-ilmo.herokuapp.com/)

Käyttäjätunnus: Testi, Salasana: Testi


[Käyttöohje](https://github.com/pekkalaine/agility-ilmo/blob/master/documentation/Kayttoohje.md)

[Tietokantakaavio](https://github.com/pekkalaine/agility-ilmo/blob/master/documentation/Tietokantakaavio2.png)

[Käyttötapaukset ja niihin liittyvät tietokantakyselyt](https://github.com/pekkalaine/agility-ilmo/blob/master//documentation/kayttotapaukset.md)


[Tietokantakantataulut ja niiden create-lauseet](https://github.com/pekkalaine/agility-ilmo/blob/master/documentation/Tietokantataulut.md)


## Sovelluksen kuvaus

Tietokantasovellus on agility- ja muita koirakursseja järjestävän koirakoulun ilmoittautumisjärjestelmä. Käyttäjä voi luoda sovellukseen tunnuksen ja kirjautua. Käyttäjällä voi olla sovelluksessa yksi tai useampi koira, jotka hän voi ilmoittaa yhdelle tai useammalle kurssille. Yhdellä koiralla voi olla vain yksi omistaja (käyttäjä). Yksi koira voi olla monella kurssilla ja toisaalta yhdellä kurssilla on yleensä monia koiria. Käyttäjä voi luoda sovellukseen kursseja. Kaikki käyttäjät voivat ilmoittaa koiriaan kaikille kursseille, jos niillä on tilaa. Käyttäjä voi perua oman koiransa ilmoittautumisia. Käyttäjät voivat tarkastella listaa muista asiakkaista ja näiden koirista.

## Mitä jäi toteuttamatta
Alkuperäisen suunnitelman mukaan sovelluksessa olisi ollut käyttäjärooleina asiakas ja kouluttaja. Kouluttaja olisi luonut kurssit ja vain kouluttaja olisi voinut päivittää kurssin tietoja. Kouluttajalla olisi lisäksi ollut mahdollisuus tarkastella kaikkien asiakkaiden tietoja ja toisaalta oikeus päivittää ja poistaa kaikkia asiakkaita, koiria, ilmoittautumisia ja kursseja. Roolit jäivät toteuttamatta, ja sovelluksen nykyisessä versiossa kouluttajalle alunperin ajatellut käyttötapaukset on suurilta osin siirretty käyttäjälle.

## Jatkokehitysdeoita
Edellä mainitun käyttäroolien toteuttamisen lisäksi kehittäisin edelleen kurssien käsittelyä sovelluksessa. Kursseilla pitäisi olla määriteltynä ajankohta, jolloin ne järjestetään. Päättyneet kurssit siirtyisivät "Menneet kurssit" -listaukseen. Kursseille ei voisi niiden alettua enää ilmoittautua tai vaihtoehtoisesti ilmoittautumisaika määriteltäisiin erikseen.

Lisäksi käyttäjien tietojen hallintaa pitäisi kehittää. Päädyin siihen ratkaisuun, että käyttäjän tietoja ei tässä versiossa voi päivittää eikä poistaa lainkaan. Ilmeinen jatkokehityskohde on myös se, että tällä hetkellä salasanat tallennetaan tietokantaan sellaisenaan. 