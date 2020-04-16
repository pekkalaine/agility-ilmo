# Agility-ilmo

[Sovellus Herokussa](https://infinite-taiga-05928.herokuapp.com)

Käyttäjätunnus: Kalle, Salasana: Hello

Sovelluksen Heroku-versio toimii joten kuten incognitossa.

[Tietokantakaavio](https://github.com/pekkalaine/agility-ilmo/blob/master/documentation/Tietokantakaavio.png)

[Käyttötapaukset](https://github.com/pekkalaine/agility-ilmo/blob/master//documentation/kayttotapaukset.md)

## Sovelluksen kuvaus

Tekeillä on agility- ja muita koirakursseja järjestävän koirakoulun tietokantasovellus. Sovellukseen voi kirjautua joko asiakkaana tai kouluttajana. Asiakkaalla voi olla sovelluksessa yksi tai useampi koira, jotka hän voi ilmoittaa yhdelle tai useammalle kurssille. Yhdellä koiralla voi olla vain yksi omistaja (asiakas). Yksi koira voi olla monella kurssilla ja toisaalta yhdellä kurssilla on yleensä monia koiria. Kouluttaja voi olla kouluttajana yhdellä tai useammalla kurssilla. Yhdellä kurssilla voi olla vain yksi kouluttaja.

Asiakas voi:
* lisätä itsensä järjestelmään
* kirjautua
* päivittää omia tietojaan
* lisätä itselleen yhden tai useamman koiran
* päivittää koiriensa tietoja
* selata sovelluksessa olevia kursseja
* lisätä yhden tai useamman koiransa yhdelle tai useammalle kurssille
* perua ilmoittautumisia
* poistaa omia koiriaan (poistettuaan ensin koiran ilmoittautumiset).

Kouluttaja voi
* kirjautua
* lisätä/muokata/poistaa asiakkaiden ja koirien tietoja
* lisätä kursseja
* päivittää kurssien tietoja
* poistaa kursseja (poistettuaan ensin ilmoittautumiset)
* poistaa ilmoittautumisia.

## Tietokantataulut

**Asiakas**
* (pk) id: int
* nimi: string
* käyttäjätunnus: string
* salasana: string
* yhteystiedot: string

**Koira**
* (pk) id: int
* (fk) asiakas_id: Asiakas
* nimi: string
* rotu: string

**Kurssi**
* (pk) id: int
* (fk) kouluttaja_id: Kouluttaja
* nimi: string
* kurssikuvaus: string
* ajankohta: string
* maksimi osallistujamäärä: int

**Kurssi-ilmoittautuminen**
* (fk) koira_id: Koira
* (fk) kurssi_id: Kurssi

**Kouluttaja**
* (pk) id: int
* nimi: string
* käyttäjätunnus: string
* salasana: string
* yhteystiedot: string