import pygame


class Renderer():
    """Ikkunan renderöinnistä vastaava luokka."""

    def __init__(self, display, level):
        """Luokan konstruktori.

        Args:
            display:
                Pygame-olio joka hallitsee sovelluksen näkymää.
            level:
                Level-luokan instanssi.
            screen_width:
                Peliruudun leveys
        """
        self.display = display
        self.level = level

    def render(self):
        """Renderöi pelinäkymän."""
        self.display.fill((255, 255, 255))
        self.level.draw_hearts()
        self.level.draw_level_text()
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
