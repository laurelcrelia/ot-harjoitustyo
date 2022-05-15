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

Pelin tason läpäisee liikuttamalla pelihahmon labyrintin perällä sijaitsevalle ovelle.

![taso1](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pelinakyma_taso1.png)

Tämän jälkeen avautuu näkymä joka ilmoittaa että olet juuri läpäissyt tason. Tästä näkymästä peli jatkuu seuraavalle tasolle painamalla *space*-näppäintä.

![taso1 läpäisty](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tason_lapaisy.png)

Toisesta tasosta lähtien peliin ilmestyy monsteri jota tulee väistää. 

![taso2](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/taso2.png)

### Häviö

Peli päättyy häviööön mikäli pelihahmo osuu monsteriin ja yhtäkään elämää ei ole enää jäljellä.

![häviönäkymä](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/havionakyma.png)

Mikäli pelaaja läpäisee kaikki pelin tasot ilmestyy ruudulle taas normaalisti tason läpäisynäkymä.

Nyt peliruudusta voi poistua joko painamalla *esc*-näppäintä tai sovellusruudun yläkulmassa sijaitsevaa raksia.

### Voitto

Peli päättyy voittoon, mikäli pelaaja pääsee kaikki 5 tasoa läpi.
   
![peli läpäisty](https://github.com/laurelcrelia/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/voitto.png)

Lopetusruudusta voi poistua painamalla *esc*-näppäintä tai sovellusruudun yläkulmassa sijaitsevaa raksia.

