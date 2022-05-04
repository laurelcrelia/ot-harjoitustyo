# Vaatimusmäärittely

## Sovelluksen tarkoitus:

Sovellus on labyrinttipeli jossa pelaajan tulee väistää vastustajia pysyäkseen elossa ja löytää ovi päästäkseen uudelle tasolle.
Käyttäjä voi valita itselleen tietyn pelihahmon rajatusta hahmovalikoimasta.
Sovelluksella on vain yhdenlaista käyttäjätyyppiä sillä kaikilla käyttäjillä on samat oikeudet.

## Käyttöliittymäluonnos

Pelissä on kolme erilaista näkymää:
- Aloitusnäkymä/valikko **"tehty"**(alustava versio aloitusnäkymästä)
- Itse pelinäkymä **"tehty"**(pelin ensimmäinen taso)
- Häviämisnäkymä/pelin läpäisynäkymä **"tehty"**

Alla kuva käyttöliittymäluonnoksesta joka on tehty projektin hyvin varhaisessa suunnitteluvaiheessa. Käyttöliittymäluonnoksessa on esitetty perusominaisuuksien lisäksi myös jatkokehitysideoita kuten esimerkiksi hahmon valitsemiseen sekä pelin säännöille luotu näkymä.
![Käyttöliittymäluonnos](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kayttoliittymaluonnos.jpg)

## Suunnitellut toiminnallisuudet perusversiolle:

- Aluksi aukeaa valikkonäkymä **"tehty"**
  - Valikosta voi siirtyä pelin aloitukseen tai poistua pelistä
  
- Pelaajalla on aluksi 3 elämää **"tehty osittain"** (tällä hetkellä vain 1 elämä pelin aluksi. Kunhan saan vielä lisättyä uusia tasoja niin lisään peliin useampia elämiä)

- Peli alkaa tasosta 1 joka on ns harjoittelukierros **"tehty"**
  - Taso 1 ei sisällä vastustajia 
  - Pelaajan tulee löytää ovi josta pääsee uudelle tasolle
  
- Tasosta 2 lähtien peliin ilmestyy vastustajia **"tehty osittain"** (taso 2 on valmiina mutta monsteri ei liiku vielä)
  - Vastustajiin osuessa pelaaja menettää yhden elämän **"tehty"**
  
- Peli vaikeutuu taso tasolta
- Peli päättyy kun pelaaja menettää kaikki elämät

- Pelin päätyttyä aukeaa "Game Over" -näkymä **"tehty"**
  - Näkymästä voi siirtyä joko aloittamaan uuden pelin tai sulkemaan pelin
  
- Uusi peli alkaa aina alusta eli tasolta 1


## Mahdolliset suunnitelmat jatkokehitykselle:

- Aloitusnäkymästä voi siirtyä "peliohjeet"-osioon jossa selitetään pelin säännöt
- Ennen pelin alkamista käyttäjä voi valita itselleen pelihahmon
  - Jos käyttäjä ei muuta pelihahmoa pelaa hän automaattisesti oletushahmolla
  - Eri hahmojen ominaisuudet eivät muutu, vain hahmojen ulkonäöllä on eroja
- Käyttäjä voi luoda käyttäjätunnuksen järjestelmään
  - Käyttäjätunnuksen tulee olla vähintään 2 merkkiä pitkä
  - Vain vapaana olevat käyttäjätunnukset sallitaan
  - Pelaajan valitsema hahmo tallentuu käyttäjätunnuksen oletushahmoksi
  - Käyttäjän tulokset tallentuvat käyttäjän omaan tulostauluun
  - Tulokset tallentuvat tauluun niin että paras tulos näkyy ylimpänä ja huonoin alimpana
- Kaikille käyttäjille näkyy yhteinen ennätystaulu jossa näkyy top 10 tulosta.
- Pelissä on useampaa kuin yhtä erilaista vastustajahahmoa
  - Eri vastustajahahmot tekevät eri määrän "damagea" eli vievät pelaajalta eri määrän sydämiä
- Tietyn tason ylittäminen antaa lisäsydämiä
- Tietyt tasot ovat checkpointeja eli kun kuolee pelissä niin saa jatkaa checkpointista eikä tarvitsee aloittaa peliä alusta
  - Esimerkiksi joka viides taso on checkpoint
