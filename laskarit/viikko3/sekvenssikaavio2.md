```mermaid
 sequenceDiagram
	participant M as main
	participant L as laitehallinto
	participant Rau as rautatietori
	participant Rat as ratikka6
	participant B as bussi244
	participant LL as lippu_luukku
	participant K as kortti
	M->>L: lisaa_lataaja(rautatietori)
	M->>L: lisaa_lukija(ratikka6)
	M->>L: lisaa_lukija(bussi244)
	M->>LL: osta_matkakortti("Kalle")
	M->>Rau: lataa_arvoa(kallen_kortti, 3)
	Rau->>+K: kasvata_arvoa(3)
	K-->>-M: True
	M->>+Rat: osta_lippu(kallen_kortti, 0)
	Rat->>-K: vahenna_arvoa(1.5)
	K-->>-M: True
	M->>+B: osta_lippu(kallen_kortti, 2)
	B-->>-M: False
```
