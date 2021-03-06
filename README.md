# Labyrinttipeli

Tässä pelissä pelaajan tulee väistellä labyrintin varrella olevia vihollisia ja löytää ovi päästäkseen seuraaville tasoille.

Pelinäkymässä on käytetty ohjelmoinnin jatkokurssin Sokoban-pelin png-kuvatiedostoja "seina.png" ja "lattia.png". 


## Release
[Release 1](https://github.com/laurelcrelia/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/laurelcrelia/ot-harjoitustyo/releases/tag/viikko6)


## Dokumentaatio:

[Käyttöohje](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet:
```poetry install```
2. Suorita vaadittavat alustustoimenpiteet:
```poetry run invoke build```
3. Käynnistä sovellus:
```poetry run invoke start```

## Komentorivitoiminnot

**Ohjelman käynnistys:**
```bash
poetry run invoke start
```

**Ohjelman testien ajaminen:**
```bash
poetry run invoke test
```

**Testikattavuusraportti:**
``` bash
poetry run invoke coverage-report
```

**Pylint-raportti:**
```bash
poetry run invoke lint
```


