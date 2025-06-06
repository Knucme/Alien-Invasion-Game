class Settings:
    """A class to store all settings for Aliend Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image_location = "assets/game_background.jpg"
        self.ship_image = "assets/ship.bmp"

        # Ship settings
        self.ship_speed = 5.5

