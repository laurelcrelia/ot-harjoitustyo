```mermaid
 sequenceDiagram
	participant M as main
	participant L as laitehallinto
	participant Rau as rautatietori
	participant Rat as ratikka6
	participant B as bussi244
	participant LL as lippu_luukku
	participant UK as uusi_kortti
	M->>L: lisaa_lataaja(rautatietori)
	M->>L: lisaa_lukija(ratikka6)
	M->>L: lisaa_lukija(bussi244)
	M->>LL: osta_matkakortti("Kalle")
	M->>Rau: lataa_arvoa(kallen_kortti, 3)
	Rau->>+UK: kasvata_arvoa(3)
	UK-->>-M: "Kalle"
	UK-->>-M: 0
	UK-->>-M: 0
	UK-->>-M: 3 
	M->>Rat: osta_lippu(kallen_kortti, 0)
	Rat->>+UK: vahenna_arvoa(1.5)
	UK-->>-M: True
	M->>+B: osta_lippu(kallen_kortti, 2)
	B-->>-M: False
```
