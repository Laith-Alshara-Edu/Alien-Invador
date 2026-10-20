import pygame
import alien_invasion
pygame.init()

# Window settings
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
WHITE = (255, 255, 255)

# Fonts
title_font = pygame.font.SysFont(None, 90)
button_font = pygame.font.SysFont(None, 60)


def draw_menu():
    """Draw the main menu."""
    screen.fill(BLACK)
    # Title
    title = title_font.render("Alien Invasion", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH // 2, 250))
    screen.blit(title, title_rect)
    # START button
    button_rect = pygame.Rect(0, 0, 300, 100)
    button_rect.center = (WIDTH // 2, 450)

    pygame.draw.rect(screen, GREEN, button_rect)

    start_text = button_font.render("START", True, WHITE)
    start_text_rect = start_text.get_rect(center=button_rect.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()

    return button_rect


def main():
    """Run the main menu."""
    running = True

    while running:
        start_button = draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    running = False

        pygame.time.Clock().tick(60)

    pygame.quit()

    # Start the actual Alien Invasion game
    alien_invasion.run_game()


if __name__ == "__main__":
    main()