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
        self.heart = pygame.image.load("src/assets/heart.png")

    def hearts(self):
        """Piirtää pelinäkymän alakulmaan elämät"""
        heart = pygame.transform.scale(self.heart, (40, 40))
        self.display.blit(heart, (50, 405))

    def render(self):
        """Renderöi pelinäkymän."""
        self.display.fill((255, 255, 255))
        self.hearts()
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
