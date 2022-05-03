# Käyttöohje
Lataa uusimman releasen lähdekoodi painamalla *Assets*-osiossa sijaitsevaa *Source code*a.

## Ohjelman käynnistäminen

1. Asenna riippuvuudet komennolla

   ``poetry install``
   
2. Suorita ohjelman alustustoimenpiteet komennolla
  
   ``poetry run invoke build``
   
3. Käynnistä ohjelma komennolla
  
   ``poetry run invoke start``
   
## Pelin aloitus

Pelin käynnistettyä aukeaa aloitusnäkymä:

![aloitusruutu](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/aloitusruutu.png)

Pelin pääset aloittamaan painamalla "Play"-painiketta ja pelin voi sulkea painamalla "Exit"-painiketta.

## Pelin kulku

![taso1](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pelinakyma_taso1.png)

Pelin tason läpäisee liikuttamalla pelihahmon labyrintin perällä sijaitsevalle ovelle.

* tähän on tulossa kuva tason läpäisynäkymästä

Toisesta tasosta lähtien peliin ilmestyy monsteri jota tulee väistää. Peli päättyy häviööön mikäli pelihahmo osuu monsteriin.

* tähän on tulossa kuva "game over"-näkymästä

Mikäli pelaaja läpäisee kaikki pelin tasot ilmestyy ruudulle pelin lopetusnäkymä.

* tähän on tulossa kuva pelin läpäisynäkymästä

Peliruudusta voi poistua painamalla sovellusruudun yläkulmassa sijaitsevaa raksia.
   
