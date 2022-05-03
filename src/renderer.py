import pygame


class Renderer:
    """Ikkunan renderöinnistä vastaava luokka."""

    def __init__(self, display, level):
        """Luokan konstruktori.

        Args:
            display: 
                Pygame-olio joka hallitsee sovelluksen näkymää.
            level:
                Level-luokan instanssi.
        """
        self.display = display
        self.level = level

    def render(self):
        """Renderöi pelinäkymän."""
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
