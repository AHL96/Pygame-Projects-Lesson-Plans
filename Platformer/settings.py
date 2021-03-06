
# setting and options
TITLE = "Jumper"
WIDTH = 480
HEIGHT = 600
FPS = 60
# FONT_NAME = pygame.font.get_default_font()
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet_jumper.png'

# Player properties
PLAYER_ACC = 1
FRICTION = -0.10
GRAVITY = .9
PLAYER_JUMP = 20

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = .1
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# starting platforms
# PLATFORM_LIST = [
#     (0, HEIGHT - 40, WIDTH, 40),
#     (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
#     (125, HEIGHT - 350, 100, 20),
#     (350, 100, 100, 20),
#     (175, 100, 50, 20)
# ]
PLATFORM_LIST = [
    (0, HEIGHT - 60),
    (WIDTH / 2 - 50, HEIGHT * 3 / 4),
    (125, HEIGHT - 350),
    (350, 100),
    (175, 100)
]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

BGCOLOR = LIGHTBLUE
