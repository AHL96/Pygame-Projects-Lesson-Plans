import pygame as pg
vec = pg.math.Vector2

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (186, 55, 5)
CYAN = (0, 255, 255)

# game settings
TILESIZE = 64
WIDTH = TILESIZE * 16  # multiple of TILESIZE
HEIGHT = TILESIZE * 10  # multiple of TILESIZE
FPS = 60
TITLE = 'Tilemap Demo'
BGCOLOR = BROWN

# GRIDWIDTH = WIDTH / TILESIZE
# GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)
PLAYER_HEALTH = 100

# Gun settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {
    'bullet_speed': 500,
    'bullet_lifetime': 1000,
    'fire_rate': 150,
    'kickback': 200,
    'spread': 5,
    'damage': 10,
    'size': 'lg',
    'bullet_count': 1
}

WEAPONS['shotgun'] = {
    'bullet_speed': 400,
    'bullet_lifetime': 500,
    'fire_rate': 1000,
    'kickback': 300,
    'spread': 20,
    'damage': 5,
    'size': 'sm',
    'bullet_count': 20
}

WEAPONS['sniper'] = {
    'bullet_speed': 600,
    'bullet_lifetime': 2000,
    'fire_rate': 2000,
    'kickback': 500,
    'spread': 2,
    'damage': 100,
    'size': 'xl',
    'bullet_count': 1
}

# BULLET_SPEED = 500
# BULLET_LIFETIME = 1000
# BULLET_RATE = 150
# KICKBACK = 200
# GUN_SPREAD = 5
# BULLET_DAMAGE = 10
# BULLET_HIT_RECT = pg.Rect(0, 0, 20, 20)

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 100, 200, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400


# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png',
                  'whitePuff17.png', 'whitePuff18.png']
SPLAT = 'splat_green.png'
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = 'light_350_med.png'

# Layers
ITEM_LAYER = 1
PLAYER_LAYER = 2
MOB_LAYER = 2
BULLET_LAYER = 3
EFFECTS_LAYER = 4

# Items
ITEM_IMAGES = {
    'health': 'health_pack.png',
    'shotgun': 'shotgun.png',
    'sniper': 'sniper.png'
}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.6

# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav',
                     'pain/11.wav', 'pain/12.wav', 'pain/13.wav', 'pain/14.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav',
                      'zombie-roar-1.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {
    'pistol': ['pistol.wav'],
    'shotgun': ['shotgun.wav'],
    'sniper': ['shotgun.wav']
}
EFFECTS_SOUNDS = {
    'level_start': 'level_start.wav',
    'health_up': 'health_pack.wav',
    'gun_pickup': 'gun_pickup.wav'
}
