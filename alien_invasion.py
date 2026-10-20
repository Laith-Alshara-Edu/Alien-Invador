import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    pygame.mixer.music.load("audio/background.mp3")
    pygame.mixer.music.play(-1)
    #Jet Noise
    fly_sound = pygame.mixer.Sound("audio/fly.mp3")
    fly_channel = None

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    stats.game_active = True
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(
            ai_settings, screen, stats, sb, None, ship, aliens, bullets
        )

        # Play the flying sound while A or D is held.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_d]:
            if fly_channel is None or not fly_channel.get_busy():
                fly_channel = fly_sound.play(loops=-1)
        else:
            if fly_channel is not None:
                fly_channel.stop()
                fly_channel = None

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, None
        )
        
if __name__ == "__main__":
    run_game()
