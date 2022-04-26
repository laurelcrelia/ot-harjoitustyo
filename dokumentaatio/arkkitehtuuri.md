# Luokkakaavio

```mermaid
 classDiagram
	class Game{
  main()
	}
	class GameLoop{
  start()
  draw_menu()
  draw_level_completed()
  movements()
  render()
  menu_initialization()
  level_completed_initialization()
	}		
	class Renderer{
  render()
	}
	class Level{
  _set_sprites()
  movement_is_true()
  move_stickman()
  stickman_finds_door()
  is_completed()
	}
	class Door{
	}
	class Floor{
	}
	class Stickman{
	}
	class Wall{
	}
	Game --> Renderer
	Game --> GameLoop
	GameLoop ..> Renderer
	Game --> Level
	Level --> "1" Door
	Level --> "*" Floor
	Level --> "1" Stickman
	Level --> "*" Wall
```

# Sekvenssikaavio

Tämä sekvenssikaavio kuvaa sitä tilannetta kun pelaaja aloittaa pelin painamalla "play" buttonia aloitusruudulla ja tämän jälkeen pelatessa häviää pelin osumalla monsteriin. Häviämisen seurauksena avautuu "game over" näkymä. 

Huom tämä sekvenssikaavio on yksinkertaistettu eikä kuvaa tarkempia tapahtumia pelihahmon liikuttamisesta ja monsteriin osumisesta pelin aikana!

```mermaid	
 sequenceDiagram
	actor U as User
	participant G as Game_loop
	participant M as Menu
	participant R as Renderer
	participant L as Level
	U->>G: click "play" button
	G->>M: initialize()
	M-->>G: False
	G->>R: render()
	R->>L: all_sprites.draw()
	G->>L: stickman_dies()
	L-->>G: True
	G->G: draw_game_over()
```
