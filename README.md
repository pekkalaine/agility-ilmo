# Agility-ilmo

[Sovellus Herokussa](https://infinite-taiga-05928.herokuapp.com/customers)

[Tietokantakaavio](https://github.com/pekkalaine/agility-ilmo/blob/master/documentation/tietokantakaavio.jpg)

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
* poistaa omia koiriaan.

Kouluttaja voi
* kirjautua
* lisätä/muokata/poistaa asiakkaiden ja koirien tietoja
* lisätä kursseja
* päivittää kurssien tietoja
* poistaa ilmoittautumisia.

## Tietokantataulut

Asiakas
* Id
* Nimi
* Yhteystiedot

Koira
* Id
* Nimi
* Rotu

Kurssi
* Id
* Nimi
* Ajankohta
* Maksimi osallistujamäärä

Kouluttaja
* id
* Nimi
* yhteystiedot
