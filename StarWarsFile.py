import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# music setup
# --- MUSIC SETUP ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MENU_MUSIC = os.path.join(BASE_DIR, "Music", "menu_music.mp3")
BATTLE_MUSIC = os.path.join(BASE_DIR, "Music", "battle_music.mp3")

pygame.mixer.music.set_volume(0.5)

def play_music(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1, start = 15.0)

# Game Setup Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BG_DARK = (20, 24, 38)
BG_MID = (35, 42, 60)
BG_LIGHT = (55, 65, 85)
FLOOR_COLOR = (25, 25, 35)     
LUKE_BLUE = (0, 160, 255)      
SABER_GREEN = (50, 255, 50)
VADER_RED = (255, 0, 50)       
MAUL_RED = (255, 30, 0)
LIGHTNING_YELLOW = (255, 220, 50)
SOLO_ORANGE = (255, 130, 0)
HEALTH_GREEN = (0, 255, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (120, 80, 50)          
BEIGE = (230, 190, 150)        
GRAY = (100, 105, 115)
PURPLE = (160, 50, 255)

# Setup Display Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star Wars: Galactic Arcade Duel")
clock = pygame.time.Clock()

# Generate Starfield Coordinates for the Background
STARS = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT - 60), random.choice([1, 2, 3])) for _ in range(80)]

# --- RETRO BITMAP FONT MATRIX ---
PIXEL_ALPHABET = {
    'A': [(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(2,1),(2,2),(2,3),(2,4)],
    'B': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(1,4),(2,1),(2,3)],
    'C': [(0,1),(0,2),(0,3),(1,0),(1,4),(2,0),(2,4)],
    'D': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,4),(2,1),(2,2),(2,3)],
    'E': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(1,4),(2,0),(2,2),(2,4)],
    'F': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(2,0),(2,2)],
    'G': [(0,1),(0,2),(0,3),(1,0),(1,4),(2,0),(2,2),(2,3),(2,4)],
    'H': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(2,0),(2,1),(2,2),(2,3),(2,4)],
    'I': [(0,0),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,4)],
    'J': [(0,3),(1,4),(2,0),(2,1),(2,2),(2,3)],
    'K': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,2),(2,0),(2,1),(2,3),(2,4)],
    'L': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4)],
    'M': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(2,0),(2,1),(2,2),(2,3),(2,4)],
    'N': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,1),(2,2),(2,3),(2,4)],
    'O': [(0,1),(0,2),(0,3),(1,0),(1,4),(2,1),(2,2),(2,3)],
    'P': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(2,1),(2,2)],
    'Q': [(0,1),(0,2),(0,3),(1,0),(1,4),(2,1),(2,2),(2,3),(2,4),(3,4)],
    'R': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(2,1),(2,2),(2,3),(2,4)],
    'S': [(0,1),(0,2),(0,4),(1,0),(1,2),(1,4),(2,0),(2,2),(2,3)],
    'T': [(0,0),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0)],
    'U': [(0,0),(0,1),(0,2),(0,3),(1,4),(2,0),(2,1),(2,2),(2,3)],
    'V': [(0,0),(0,1),(0,2),(1,3),(1,4),(2,0),(2,1),(2,2)],
    'W': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,3),(2,0),(2,1),(2,2),(2,3),(2,4)],
    'X': [(0,0),(0,4),(1,1),(1,2),(1,3),(2,0),(2,4)],
    'Y': [(0,0),(0,1),(1,2),(1,3),(1,4),(2,0),(2,1)],
    'Z': [(0,0),(0,4),(1,0),(1,2),(1,4),(2,0),(2,4)],
    '1': [(0,1),(1,0),(1,1),(1,2),(1,3),(1,4),(2,4)],
    '2': [(0,0),(0,2),(0,3),(0,4),(1,0),(1,2),(1,4),(2,0),(2,1),(2,4)],
    '3': [(0,0),(0,4),(1,0),(1,2),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4)],
    '4': [(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2),(2,3),(2,4)],
    '5': [(0,0),(0,1),(0,2),(0,4),(1,0),(1,2),(1,4),(2,0),(2,2),(2,3)],
    '6': [(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(1,4),(2,1),(2,2),(2,3),(2,4)],
    '7': [(0,0),(1,0),(1,1),(2,2),(2,3),(2,4)],
    '8': [(0,1),(0,2),(0,3),(1,0),(1,2),(1,4),(2,1),(2,2),(2,3)],
    '9': [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(2,3),(2,4)],
    '0': [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4)],
    '-': [(0,2),(1,2),(2,2)],
    ':': [(1,1),(1,3)],
    ' ': [],
    '(': [(1,0),(0,1),(0,2),(0,3),(1,4)],
    ')': [(0,0),(1,1),(1,2),(1,3),(0,4)],
    '/': [(2,0),(1,1),(1,2),(1,3),(0,4)]
}

def draw_pixel_text(surface, text, x, y, size=3, color=WHITE):
    current_x = x
    for char in text.upper():
        if char in PIXEL_ALPHABET:
            pixels = PIXEL_ALPHABET[char]
            for px, py in pixels:
                pygame.draw.rect(surface, color, (current_x + px * size, y + py * size, size, size))
        current_x += 4 * size

# Character Definitions
# Expanded Character Parameter Balance Sheet
CHARACTERS = [
    {
        "name": "OBI-WAN",
        "color": LUKE_BLUE,
        "ability": "FORCE PUSH",
        "max_health": 250,
        "speed": 7,
        "jump": -18,
        "weapon": "BLUE_SABER",
        "attack_type": "SABER_SWING"
    },
    {
        "name": "LUKE",
        "color": SABER_GREEN,
        "ability": "SABER THROW",
        "max_health": 250,
        "speed": 7,
        "jump": -18,
        "weapon": "GREEN_SABER",
        "attack_type": "SABER_SWING"
    },
    {
        "name": "HAN SOLO",
        "color": SOLO_ORANGE,
        "ability": "BLASTER",
        "max_health": 200,
        "speed": 9,
        "jump": -17,
        "weapon": "BLASTER",
        "attack_type": "GUNSHOT"
    },
    {
        "name": "VADER",
        "color": VADER_RED,
        "ability": "FORCE CHOKE",
        "max_health": 350,
        "speed": 5,
        "jump": -16,
        "weapon": "RED_SABER",
        "attack_type": "SABER_SWING"
    },
    {
        "name": "MAUL",
        "color": MAUL_RED,
        "ability": "DUAL THROW",
        "max_health": 240,
        "speed": 8.5,
        "jump": -19,
        "weapon": "DOUBLE_SABER",
        "attack_type": "SABER_SWING"
    },
    {
        "name": "DOOKU",
        "color": LIGHTNING_YELLOW,
        "ability": "LIGHTNING",
        "max_health": 280,
        "speed": 6.5,
        "jump": -16,
        "weapon": "RED_SABER",
        "attack_type": "SABER_SWING"
    },
    {
        "name": "PALPATINE",
        "color": PURPLE,
        "ability": "FORCE LIGHTNING",
        "max_health": 220,
        "speed": 5,
        "jump": -15,
        "weapon": None,
        "attack_type": "FORCE_LIGHTNING"
    }
]

class SpecialProjectile:
    def __init__(self, x, y, direction, color, p_type, owner):
        # Establish unique hitbox sizes for each blast style
        if p_type == "FORCE PUSH":
            # Obi-Wan sends a massive tall wall of force
            self.rect = pygame.Rect(x, y - 30, 25, 90)
        elif p_type == "SABER THROW":
            # Luke throws a standard spinning projectile square
            self.rect = pygame.Rect(x, y + 10, 40, 40)
        elif p_type == "BLASTER":
            # Han Solo shoots a tiny, ultra-fast laser bolt
            self.rect = pygame.Rect(x, y + 15, 30, 8)
        elif p_type == "FORCE CHOKE":
            # Vader sends a low-traveling heavy purple blast wave
            self.rect = pygame.Rect(x, y + 40, 60, 20)
        elif p_type == "DUAL THROW":
            # Maul throws a long double-sided weapon block
            self.rect = pygame.Rect(x, y + 5, 80, 16)
        elif p_type == "LIGHTNING":
            # Dooku throws a thick crackling energy mass
            self.rect = pygame.Rect(x, y, 65, 35)
        elif p_type == "FORCE LIGHTNING":
            self.rect = pygame.Rect(x, y + 10, 80, 45)
        else:
            self.rect = pygame.Rect(x, y, 35, 15)
            
        # Tweak speeds based on attack type (Han's laser is fastest)
        if p_type == "BLASTER":
            self.speed = 18 * direction
        elif p_type == "FORCE PUSH":
            self.speed = 9 * direction
        elif p_type == "FORCE LIGHTNING":
            self.speed = 11 * direction
        else:
            self.speed = 12 * direction
            
        self.color = color
        self.p_type = p_type
        self.active = True
        self.animation_tick = 0 # Used for flickering energy effects
        self.owner = owner  

    def update(self):
        self.rect.x += self.speed
        self.animation_tick += 1
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.active = False

    def draw(self, surface):
        self.animation_tick += 1
        if self.p_type == "FORCE PUSH":
            # Draw a tall energy wave with layered transparent rings
            pygame.draw.rect(surface, LUKE_BLUE, self.rect, 4)
            pygame.draw.rect(surface, WHITE, (self.rect.x + 8, self.rect.y + 10, 8, self.rect.height - 20))
            
        elif self.p_type == "SABER THROW":
            # Draw a solid green square core with a glowing white outline
            pygame.draw.rect(surface, SABER_GREEN, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, 3)
            
        elif self.p_type == "BLASTER":
            # A bright glowing blaster core bolt
            pygame.draw.rect(surface, VADER_RED, self.rect)
            pygame.draw.rect(surface, WHITE, (self.rect.x + 5, self.rect.y + 2, self.rect.width - 10, 4))
            
        elif self.p_type == "FORCE CHOKE":
            # Low dark purple psychic block waves
            pygame.draw.rect(surface, PURPLE, self.rect)
            if self.animation_tick % 4 < 2:
                pygame.draw.rect(surface, BLACK, (self.rect.x + 10, self.rect.y + 4, self.rect.width - 20, 12))
                
        elif self.p_type == "DUAL THROW":
            # Draw Maul's rotating dual blade concept as a dual-block stack
            pygame.draw.rect(surface, MAUL_RED, self.rect)
            pygame.draw.rect(surface, GRAY, (self.rect.x + 30, self.rect.y - 4, 20, 24)) # Rotating center hilt
            pygame.draw.rect(surface, WHITE, (self.rect.x + 5, self.rect.y + 4, self.rect.width - 10, 8))

        elif self.p_type == "FORCE LIGHTNING":
            # Palpatine's branching lightning
            pygame.draw.line(
                surface,
                LIGHTNING_YELLOW,
                (self.rect.left, self.rect.centery),
                (self.rect.left + 20, self.rect.top),
                5
            )

            pygame.draw.line(
                surface,
                LIGHTNING_YELLOW,
                (self.rect.left + 15, self.rect.centery),
                (self.rect.left + 35, self.rect.bottom),
                5
            )

            pygame.draw.line(
                surface,
                WHITE,
                (self.rect.left + 10, self.rect.centery),
                (self.rect.right, self.rect.centery),
                4
            )

            pygame.draw.line(
            surface,
                LIGHTNING_YELLOW,
                (self.rect.left + 35, self.rect.centery),
                (self.rect.right - 10, self.rect.top + 8),
                4
            )

            pygame.draw.line(
                surface,
                LIGHTNING_YELLOW,
                (self.rect.left + 40, self.rect.centery),
                (self.rect.right - 5, self.rect.bottom - 8),
                4
            )
        
        elif self.p_type == "LIGHTNING":
            # Crackling electric block pattern that flickers yellow and white
            if self.animation_tick % 2 == 0:
                pygame.draw.rect(surface, LIGHTNING_YELLOW, self.rect)
                pygame.draw.rect(surface, WHITE, (self.rect.x + 6, self.rect.y + 6, self.rect.width - 12, self.rect.height - 12))
            else:
                # Invert colors on next frame for a crackling strobe effect
                pygame.draw.rect(surface, WHITE, self.rect)
                pygame.draw.rect(surface, LIGHTNING_YELLOW, (self.rect.x + 4, self.rect.y + 4, self.rect.width - 8, self.rect.height - 8))
def draw_lightsaber(surface, x, y, direction, color, length=55, double=False):
    saber_h = 7
    hilt_w = 15
    hilt_h = 10

    if direction > 0:
        # Hilt
        pygame.draw.rect(
            surface,
            GRAY,
            (x, y - 3, hilt_w, hilt_h)
        )

        # Main blade
        pygame.draw.rect(
            surface,
            color,
            (x + hilt_w, y, length, saber_h)
        )

        # White center highlight
        pygame.draw.rect(
            surface,
            WHITE,
            (x + hilt_w + 5, y + 2, length - 10, 2)
        )

        # Second blade for Maul
        if double:
            pygame.draw.rect(
                surface,
                color,
                (x - length, y, length, saber_h)
            )

            pygame.draw.rect(
                surface,
                WHITE,
                (x - length + 5, y + 2, length - 10, 2)
            )

    else:
        # Hilt
        pygame.draw.rect(
            surface,
            GRAY,
            (x - hilt_w, y - 3, hilt_w, hilt_h)
        )

        # Main blade
        pygame.draw.rect(
            surface,
            color,
            (x - hilt_w - length, y, length, saber_h)
        )

        # White center highlight
        pygame.draw.rect(
            surface,
            WHITE,
            (x - hilt_w - length + 5, y + 2, length - 10, 2)
        )

        # Second blade for Maul
        if double:
            pygame.draw.rect(
                surface,
                color,
                (x, y, length, saber_h)
            )

            pygame.draw.rect(
                surface,
                WHITE,
                (x + 5, y + 2, length - 10, 2)
            )

class Fighter:
    def __init__(self, x, y, char_data, control_type):
        self.name = char_data["name"]
        self.color = char_data["color"]
        self.ability = char_data["ability"]
        self.weapon = char_data["weapon"]
        self.control_type = control_type 
        self.attack_type = char_data["attack_type"]
        
        # Pull Custom Attributes from the Stats Sheet
        self.health = char_data["max_health"]
        self.max_health = char_data["max_health"]
        self.speed = char_data["speed"]
        self.jump_power = char_data["jump"]
        
        # Positioning Architecture
        self.width = 60
        self.height = 110
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 1
        self.is_grounded = False
        
        # Combat Action Trackers
        self.facing_right = True if x < SCREEN_WIDTH // 2 else False
        self.is_attacking = False
        self.attack_cooldown = 0
        self.attack_duration = 0
        self.attack_rect = None
        self.special_cooldown = 0
        self.force_choked = False
        self.force_choke_timer = 0
        self.force_choke_velocity = 0
        
        # --- NEW HITSTUN STATE PARAMETERS ---
        self.hitstun_frames = 0
        self.knockback_vel = 0

    def take_damage(self, damage_amount, standard_attack=True):
        """Deducts health, applies hitstun frames, and calculates directional physics knockback."""
        self.health -= damage_amount
        
        # Determine knockback direction based on orientation
        direction_multiplier = -1 if self.facing_right else 1
        
        if standard_attack:
            self.hitstun_frames = 12  # Frozen for ~0.2 seconds
            self.knockback_vel = 14 * direction_multiplier
        else: # Heavy Ranged Blast Impact
            self.hitstun_frames = 20  # Frozen for ~0.33 seconds
            self.knockback_vel = 22 * direction_multiplier

    def move(self, opponent_rect, projectiles_list):
        self.vel_x = 0
        keys = pygame.key.get_pressed()
        # --- FORCE CHOKE OVERRIDE ---
        if self.force_choked:
            self.force_choke_timer -= 1

            # Lift the victim upward
            self.rect.y -= 2

            # Push the victim backward
            self.rect.x += self.force_choke_velocity

            # Keep the victim inside the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

            # Release after the choke animation
            if self.force_choke_timer <= 0:
                self.force_choked = False
                self.vel_y = 0

            self.tick_cooldown_counters()
            return
        
        # Always evaluate screen orientation unless entirely incapacitated
        if self.hitstun_frames <= 0:
            if self.rect.centerx < opponent_rect.centerx:
                self.facing_right = True
            else:
                self.facing_right = False

        # --- HITSTUN AND KNOCKBACK OVERRIDE ROUTINE ---
        if self.hitstun_frames > 0:
            # Force velocity to reflect the knockback push, decay it gradually
            self.vel_x = self.knockback_vel
            self.knockback_vel *= 0.85 # Linear velocity friction decay
            self.hitstun_frames -= 1
            
            # Skip reading player input keys while frozen in hitstun
            self.apply_physics_and_boundaries()
            self.tick_cooldown_counters()
            return

        # --- NORMAL CONTROLLER INPUT PROCESSING ---
        if self.control_type == "player_1":
            if keys[pygame.K_LEFT]: self.vel_x = -self.speed
            if keys[pygame.K_RIGHT]: self.vel_x = self.speed
            if keys[pygame.K_UP] and self.is_grounded:
                self.vel_y = self.jump_power
                self.is_grounded = False
            if keys[pygame.K_SPACE] and self.attack_cooldown == 0:
                self.attack()
            if keys[pygame.K_m] and self.special_cooldown == 0:
                self.use_special(projectiles_list)
                
        elif self.control_type == "player_2":
            if keys[pygame.K_a]: self.vel_x = -self.speed
            if keys[pygame.K_d]: self.vel_x = self.speed
            if keys[pygame.K_w] and self.is_grounded:
                self.vel_y = self.jump_power
                self.is_grounded = False
            if keys[pygame.K_f] and self.attack_cooldown == 0:
                self.attack()
            if keys[pygame.K_g] and self.special_cooldown == 0:
                self.use_special(projectiles_list)

        elif self.control_type == "cpu":
            distance = abs(self.rect.centerx - opponent_rect.centerx)
            if distance > 250 and self.special_cooldown == 0 and random.random() < 0.05:
                self.use_special(projectiles_list)
            elif distance > 110:
                if self.rect.centerx < opponent_rect.centerx: self.vel_x = self.speed - 2
                else: self.vel_x = -(self.speed - 2)
            else:
                if self.attack_cooldown == 0 and random.random() < 0.08:
                    self.attack()
                if self.is_grounded and random.random() < 0.02:
                    self.vel_y = self.jump_power
                    self.is_grounded = False

        self.apply_physics_and_boundaries()
        self.tick_cooldown_counters()

    def apply_physics_and_boundaries(self):
        # Physics Step
        self.vel_y += self.gravity
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Platform bounds stabilization
        if self.rect.bottom >= SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0
            self.is_grounded = True

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH

    def tick_cooldown_counters(self):
        if self.attack_cooldown > 0: self.attack_cooldown -= 1
        if self.special_cooldown > 0: self.special_cooldown -= 1
        if self.is_attacking:
            self.attack_duration -= 1
            if self.attack_duration <= 0:
                self.is_attacking = False
                self.attack_rect = None

    def attack(self):
        self.is_attacking = True
        self.attack_duration = 10
        self.attack_cooldown = 30

        direction = 1 if self.facing_right else -1

        if self.attack_type == "SABER_SWING":
            attack_width = 75
            attack_height = 55

            if self.facing_right:
                self.attack_rect = pygame.Rect(
                    self.rect.right - 5,
                    self.rect.y + 25,
                    attack_width,
                    attack_height
                )
            else:
                self.attack_rect = pygame.Rect(
                    self.rect.left - attack_width + 5,
                    self.rect.y + 25,
                    attack_width,
                    attack_height
                )

        elif self.attack_type == "GUNSHOT":
            attack_width = 55
            attack_height = 30

            if self.facing_right:
                self.attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y + 40,
                    attack_width,
                    attack_height
                )
            else:
                self.attack_rect = pygame.Rect(
                    self.rect.left - attack_width,
                    self.rect.y + 40,
                    attack_width,
                    attack_height
                )

        elif self.attack_type == "FORCE_LIGHTNING":
            attack_width = 65
            attack_height = 70

            if self.facing_right:
                self.attack_rect = pygame.Rect(
                    self.rect.right,
                    self.rect.y + 20,
                    attack_width,
                    attack_height
                )
            else:
                self.attack_rect = pygame.Rect(
                    self.rect.left - attack_width,
                    self.rect.y + 20,
                    attack_width,
                    attack_height
                )

    def apply_force_choke(self):
        self.force_choked = True
        self.force_choke_timer = 45
        self.force_choke_velocity = 0

    def use_special(self, projectiles_list):
        if self.special_cooldown > 0:
            return

        self.special_cooldown = 90

        direction = 1 if self.facing_right else -1

        spawn_x = self.rect.right if self.facing_right else self.rect.left - 40

        p = SpecialProjectile(
            spawn_x,
            self.rect.y + 30,
            direction,
            self.color,
            self.ability,
            self
        )

        projectiles_list.append(p)

    def draw(self, surface):
        x, y = self.rect.x, self.rect.y
        PIX = 4
        
        # Apply flash color effect if character is stuck processing hitstun frames
        draw_color = WHITE if self.hitstun_frames > 0 and self.hitstun_frames % 4 < 2 else self.color
        
        # Unique Character Pixel Models
        if self.name == "OBI-WAN":
            # --- Hair / head ---
            pygame.draw.rect(surface, BROWN, (x + 16, y, 28, 7))
            pygame.draw.rect(surface, BROWN, (x + 12, y + 6, 8, 12))
            pygame.draw.rect(surface, BEIGE, (x + 18, y + 7, 24, 22))

            # Ears
            pygame.draw.rect(surface, BEIGE, (x + 14, y + 13, 4, 8))
            pygame.draw.rect(surface, BEIGE, (x + 42, y + 13, 4, 8))

            # Face shadows / eyes
            pygame.draw.rect(surface, BROWN, (x + 18, y + 7, 24, 4))
            pygame.draw.rect(surface, BLACK, (x + 22, y + 15, 3, 3))
            pygame.draw.rect(surface, BLACK, (x + 35, y + 15, 3, 3))
            pygame.draw.rect(surface, BROWN, (x + 27, y + 19, 7, 3))

            # Beard
            pygame.draw.rect(surface, BROWN, (x + 22, y + 22, 16, 7))
            pygame.draw.rect(surface, BROWN, (x + 26, y + 27, 8, 4))

            # --- Jedi robe / torso ---
            pygame.draw.rect(surface, BROWN, (x + 8, y + 31, 44, 45))
            pygame.draw.rect(surface, BEIGE, (x + 17, y + 31, 26, 45))

            # Robe opening
            pygame.draw.rect(surface, WHITE, (x + 22, y + 34, 16, 42))
            pygame.draw.rect(surface, BROWN, (x + 27, y + 34, 6, 42))

            # Belt
            pygame.draw.rect(surface, BROWN, (x + 10, y + 72, 40, 8))
            pygame.draw.rect(surface, GRAY, (x + 27, y + 72, 8, 8))

            # --- Arms ---
            pygame.draw.rect(surface, BROWN, (x + 2, y + 34, 12, 42))
            pygame.draw.rect(surface, BROWN, (x + 46, y + 34, 12, 42))

            #        Hands
            pygame.draw.rect(surface, BEIGE, (x + 2, y + 73, 10, 8))
            pygame.draw.rect(surface, BEIGE, (x + 48, y + 73, 10, 8))

            # --- Legs ---
            pygame.draw.rect(surface, BROWN, (x + 12, y + 80, 15, 30))
            pygame.draw.rect(surface, BROWN, (x + 33, y + 80, 15, 30))

            # Boots
            pygame.draw.rect(surface, BLACK, (x + 10, y + 103, 18, 7))
            pygame.draw.rect(surface, BLACK, (x + 32, y + 103, 18, 7))
        elif self.name == "LUKE":
            # --- Hair / head ---
            pygame.draw.rect(surface, BROWN, (x + 16, y, 28, 7))
            pygame.draw.rect(surface, BROWN, (x + 12, y + 5, 8, 13))
            pygame.draw.rect(surface, BEIGE, (x + 18, y + 6, 24, 23))

            # Ears
            pygame.draw.rect(surface, BEIGE, (x + 14, y + 13, 4, 8))
            pygame.draw.rect(surface, BEIGE, (x + 42, y + 13, 4, 8))

            # Face shading
            pygame.draw.rect(surface, BROWN, (x + 18, y + 6, 24, 4))

            # Eyes
            pygame.draw.rect(surface, BLACK, (x + 22, y + 15, 3, 3))
            pygame.draw.rect(surface, BLACK, (x + 35, y + 15, 3, 3))

            # Nose / mouth
            pygame.draw.rect(surface, BROWN, (x + 28, y + 18, 5, 3))
            pygame.draw.rect(surface, BROWN, (x + 26, y + 23, 10, 3))

            # --- Jedi tunic ---
            pygame.draw.rect(surface, WHITE, (x + 10, y + 29, 40, 47))
            pygame.draw.rect(surface, GRAY, (x + 15, y + 32, 30, 44))

            # Tunic opening
            pygame.draw.rect(surface, BLACK, (x + 27, y + 32, 6, 42))

            # Belt
            pygame.draw.rect(surface, BROWN, (x + 10, y + 72, 40, 8))
            pygame.draw.rect(surface, GRAY, (x + 27, y + 72, 8, 8))

            # --- Arms ---
            pygame.draw.rect(surface, WHITE, (x + 2, y + 34, 12, 42))
            pygame.draw.rect(surface, WHITE, (x + 46, y + 34, 12, 42))

        # Hands
            pygame.draw.rect(surface, BEIGE, (x + 2, y + 73, 10, 8))
            pygame.draw.rect(surface, BEIGE, (x + 48, y + 73, 10, 8))

            # --- Legs ---
            pygame.draw.rect(surface, GRAY, (x + 12, y + 80, 15, 30))
            pygame.draw.rect(surface, GRAY, (x + 33, y + 80, 15, 30))

            # Boots
            pygame.draw.rect(surface, BROWN, (x + 10, y + 103, 18, 7))
            pygame.draw.rect(surface, BROWN, (x + 32, y + 103, 18, 7))
        elif self.name == "HAN SOLO":
            # --- Head / hair ---
            pygame.draw.rect(surface, BEIGE, (x + 18, y + 2, 24, 24))

            # Brown hair
            pygame.draw.rect(surface, BROWN, (x + 14, y - 2, 32, 8))
            pygame.draw.rect(surface, BROWN, (x + 10, y + 4, 10, 14))
            pygame.draw.rect(surface, BROWN, (x + 40, y + 4, 8, 12))

            # Ear / face detail
            pygame.draw.rect(surface, BEIGE, (x + 40, y + 12, 5, 8))
            pygame.draw.rect(surface, BEIGE, (x + 15, y + 12, 5, 8))

            # Eye
            pygame.draw.rect(surface, BLACK, (x + 34, y + 12, 4, 4))
            pygame.draw.rect(surface, BLACK, (x + 23, y + 12, 4, 4))

            # --- White shirt ---
            pygame.draw.rect(surface, WHITE, (x + 14, y + 25, 32, 38))

            # Shirt collar
            pygame.draw.rect(surface, BEIGE, (x + 25, y + 25, 10, 8))

            # --- Black vest ---
            pygame.draw.rect(surface, BLACK, (x + 10, y + 28, 9, 35))
            pygame.draw.rect(surface, BLACK, (x + 41, y + 28, 9, 35))

            # Vest center opening
            pygame.draw.rect(surface, BLACK, (x + 19, y + 34, 5, 29))
            pygame.draw.rect(surface, BLACK, (x + 35, y + 34, 6, 29))

            # --- Arms ---
            # Left arm
            pygame.draw.rect(surface, WHITE, (x + 4, y + 32, 10, 22))
            pygame.draw.rect(surface, BEIGE, (x + 2, y + 50, 12, 10))

            # Right arm
            pygame.draw.rect(surface, WHITE, (x + 46, y + 32, 10, 22))
            pygame.draw.rect(surface, BEIGE, (x + 50, y + 50, 12, 10))

            # --- Belt ---
            pygame.draw.rect(surface, BROWN, (x + 12, y + 61, 36, 7))
            pygame.draw.rect(surface, GRAY, (x + 27, y + 61, 7, 7))

            # --- Dark pants ---
            pygame.draw.rect(surface, BLACK, (x + 14, y + 68, 14, 30))
            pygame.draw.rect(surface, BLACK, (x + 34, y + 68, 14, 30))

            # Blue/gray pants highlights
            pygame.draw.rect(surface, GRAY, (x + 17, y + 70, 7, 25))
            pygame.draw.rect(surface, GRAY, (x + 37, y + 70, 7, 25))

            # --- Boots ---
            pygame.draw.rect(surface, BLACK, (x + 10, y + 94, 18, 12))
            pygame.draw.rect(surface, BLACK, (x + 34, y + 94, 18, 12))
             
        elif self.name == "VADER":
            # --- Large Vader helmet / dome ---
            pygame.draw.rect(surface, BLACK, (x + 16, y+8, 28, 5))
            pygame.draw.rect(surface, BLACK, (x + 12, y + 12, 36, 8))
            pygame.draw.rect(surface, BLACK, (x + 9, y + 19, 42, 12))
            pygame.draw.rect(surface, BLACK, (x + 7, y + 28, 46, 13))

            # Helmet dome highlights
            pygame.draw.rect(surface, (45, 45, 50), (x + 17, y + 8, 7, 5))
            pygame.draw.rect(surface, (45, 45, 50), (x + 36, y + 8, 7, 5))
            pygame.draw.rect(surface, GRAY, (x + 12, y + 15, 5, 7))
            pygame.draw.rect(surface, GRAY, (x + 43, y + 15, 5, 7))

            # --- Vader face / mask ---
            pygame.draw.rect(surface, BLACK, (x + 15, y + 27, 30, 22))
            pygame.draw.rect(surface, GRAY, (x + 19, y + 27, 22, 8))

            # Eye sockets
            pygame.draw.rect(surface, BLACK, (x + 19, y + 29, 9, 5))
            pygame.draw.rect(surface, BLACK, (x + 32, y + 29, 9, 5))

            # Red eye slits
            pygame.draw.rect(surface, VADER_RED, (x + 21, y + 31, 6, 2))
            pygame.draw.rect(surface, VADER_RED, (x + 34, y + 31, 6, 2))

            # --- Triangular mouth / respirator mask ---
            pygame.draw.rect(surface, BLACK, (x + 22, y + 35, 16, 5))
            pygame.draw.rect(surface, BLACK, (x + 19, y + 40, 22, 7))
            pygame.draw.rect(surface, GRAY, (x + 24, y + 39, 12, 3))
            pygame.draw.rect(surface, GRAY, (x + 27, y + 43, 6, 3))

            # --- Neck ---
            pygame.draw.rect(surface, BLACK, (x + 21, y + 46, 18, 8))

            # --- Wide cape / shoulders ---
            pygame.draw.rect(surface, BLACK, (x + 7, y + 48, 46, 12))
            pygame.draw.rect(surface, BLACK, (x + 3, y + 56, 54, 25))
            pygame.draw.rect(surface, BLACK, (x + 7, y + 75, 46, 10))

            # Cape folds / subtle highlights
            pygame.draw.rect(surface, (35, 35, 40), (x + 7, y + 59, 5, 22))
            pygame.draw.rect(surface, (35, 35, 40), (x + 48, y + 59, 5, 22))

            # --- Chest armor ---
            pygame.draw.rect(surface, BLACK, (x + 14, y + 52, 32, 31))
            pygame.draw.rect(surface, (40, 40, 45), (x + 18, y + 55, 24, 25))

            # Chest control panel
            pygame.draw.rect(surface, BLACK, (x + 20, y + 57, 20, 17))

            # Control panel lights
            pygame.draw.rect(surface, VADER_RED, (x + 23, y + 60, 5, 4))
            pygame.draw.rect(surface, LIGHTNING_YELLOW, (x + 32, y + 60, 5, 4))
            pygame.draw.rect(surface, VADER_RED, (x + 23, y + 67, 5, 3))
            pygame.draw.rect(surface, GRAY, (x + 32, y + 67, 5, 3))

            # --- Arms ---
            pygame.draw.rect(surface, BLACK, (x + 1, y + 51, 14, 31))
            pygame.draw.rect(surface, BLACK, (x + 45, y + 51, 14, 31))

            # Arm armor
            pygame.draw.rect(surface, (40, 40, 45), (x + 4, y + 56, 8, 17))
            pygame.draw.rect(surface, (40, 40, 45), (x + 48, y + 56, 8, 17))

            # Gloves
            pygame.draw.rect(surface, BLACK, (x + 2, y + 73, 11, 10))
            pygame.draw.rect(surface, BLACK, (x + 47, y + 73, 11, 10))

            # --- Belt ---
            pygame.draw.rect(surface, BLACK, (x + 9, y + 78, 42, 9))
            pygame.draw.rect(surface, GRAY, (x + 17, y + 80, 8, 5))
            pygame.draw.rect(surface, GRAY, (x + 35, y + 80, 8, 5))

            # --- Legs ---
            pygame.draw.rect(surface, BLACK, (x + 12, y + 86, 15, 24))
            pygame.draw.rect(surface, BLACK, (x + 33, y + 86, 15, 24))

            # Subtle leg highlights
            pygame.draw.rect(surface, (35, 35, 40), (x + 15, y + 88, 5, 18))
            pygame.draw.rect(surface, (35, 35, 40), (x + 36, y + 88, 5, 18))

            # Boots
            pygame.draw.rect(surface, BLACK, (x + 9, y + 103, 19, 7))
            pygame.draw.rect(surface, BLACK, (x + 32, y + 103, 19, 7)) 
        elif self.name == "MAUL":
            # --- Horns ---
            pygame.draw.rect(surface, BEIGE, (x + 16, y - 4, 6, 8))
            pygame.draw.rect(surface, BEIGE, (x + 24, y - 7, 6, 11))
            pygame.draw.rect(surface, BEIGE, (x + 32, y - 7, 6, 11))
            pygame.draw.rect(surface, BEIGE, (x + 40, y - 4, 6, 8))

            # --- Head ---
            pygame.draw.rect(surface, VADER_RED, (x + 14, y + 2, 32, 29))
            pygame.draw.rect(surface, VADER_RED, (x + 10, y + 10, 40, 15))

            # --- Black facial markings ---
            pygame.draw.rect(surface, BLACK, (x + 18, y + 5, 7, 8))
            pygame.draw.rect(surface, BLACK, (x + 33, y + 5, 7, 8))

            pygame.draw.rect(surface, BLACK, (x + 13, y + 14, 9, 5))
            pygame.draw.rect(surface, BLACK, (x + 39, y + 14, 9, 5))

            pygame.draw.rect(surface, BLACK, (x + 22, y + 17, 5, 8))
            pygame.draw.rect(surface, BLACK, (x + 33, y + 17, 5, 8))

            pygame.draw.rect(surface, BLACK, (x + 27, y + 12, 6, 5))
            pygame.draw.rect(surface, BLACK, (x + 25, y + 24, 10, 5))

            # Eyes
            pygame.draw.rect(surface, BEIGE, (x + 22, y + 13, 5, 3))
            pygame.draw.rect(surface, BEIGE, (x + 33, y + 13, 5, 3))

            # --- Neck ---
            pygame.draw.rect(surface, BLACK, (x + 22, y + 29, 16, 7))

            # --- Robes / torso ---
            pygame.draw.rect(surface, BLACK, (x + 8, y + 34, 44, 48))
            pygame.draw.rect(surface, GRAY, (x + 14, y + 38, 32, 40))

            # Robe center
            pygame.draw.rect(surface, BLACK, (x + 27, y + 38, 6, 40))

            # Robe folds
            pygame.draw.rect(surface, GRAY, (x + 15, y + 50, 5, 27))
            pygame.draw.rect(surface, GRAY, (x + 40, y + 50, 5, 27))

            # --- Arms ---
            pygame.draw.rect(surface, BLACK, (x + 1, y + 36, 13, 44))
            pygame.draw.rect(surface, BLACK, (x + 46, y + 36, 13, 44))

            # Arm highlights
            pygame.draw.rect(surface, GRAY, (x + 4, y + 42, 7, 22))
            pygame.draw.rect(surface, GRAY, (x + 49, y + 42, 7, 22))

            # Hands
            pygame.draw.rect(surface, VADER_RED, (x + 2, y + 74, 10, 9))
            pygame.draw.rect(surface, VADER_RED, (x + 48, y + 74, 10, 9))

            # --- Belt ---
            pygame.draw.rect(surface, BLACK, (x + 9, y + 76, 42, 9))
            pygame.draw.rect(surface, GRAY, (x + 25, y + 78, 10, 5))

            # --- Legs ---
            pygame.draw.rect(surface, BLACK, (x + 12, y + 84, 15, 26))
            pygame.draw.rect(surface, BLACK, (x + 33, y + 84, 15, 26))

        #    Boots
            pygame.draw.rect(surface, BLACK, (x + 9, y + 103, 19, 7))
            pygame.draw.rect(surface, BLACK, (x + 32, y + 103, 19, 7)) 
        elif self.name == "DOOKU":
            # --- White hair ---
            pygame.draw.rect(surface, WHITE, (x + 17, y, 26, 6))
            pygame.draw.rect(surface, WHITE, (x + 13, y + 4, 8, 12))
            pygame.draw.rect(surface, WHITE, (x + 41, y + 4, 8, 12))
            pygame.draw.rect(surface, WHITE, (x + 20, y + 5, 22, 5))

            # --- Face ---
            pygame.draw.rect(surface, BEIGE, (x + 19, y + 9, 22, 23))
            pygame.draw.rect(surface, BEIGE, (x + 15, y + 15, 5, 8))
            pygame.draw.rect(surface, BEIGE, (x + 41, y + 15, 5, 8))

            # Forehead
            pygame.draw.rect(surface, WHITE, (x + 20, y + 9, 20, 4))

            # Eyes
            pygame.draw.rect(surface, BLACK, (x + 23, y + 16, 3, 3))
            pygame.draw.rect(surface, BLACK, (x + 34, y + 16, 3, 3))

            # Nose
            pygame.draw.rect(surface, BROWN, (x + 29, y + 19, 5, 3))

            # --- White mustache ---
            pygame.draw.rect(surface, WHITE, (x + 23, y + 22, 7, 4))
            pygame.draw.rect(surface, WHITE, (x + 30, y + 22, 7, 4))

            # --- Pointed beard ---
            pygame.draw.rect(surface, WHITE, (x + 25, y + 25, 10, 5))
            pygame.draw.rect(surface, WHITE, (x + 26, y + 29, 8, 5))
            pygame.draw.rect(surface, WHITE, (x + 27, y + 33, 6, 4))

            # --- Neck ---
            pygame.draw.rect(surface, BEIGE, (x + 24, y + 34, 12, 7))

            # --- Brown cape / shoulders ---
            pygame.draw.rect(surface, BROWN, (x + 9, y + 37, 42, 10))
            pygame.draw.rect(surface, BROWN, (x + 5, y + 43, 50, 37))
            
            # Black cape outer edges
            pygame.draw.rect(surface, BLACK, (x + 5, y + 43, 7, 38))
            pygame.draw.rect(surface, BLACK, (x + 48, y + 43, 7, 38))

            # --- Dark tunic underneath ---
            pygame.draw.rect(surface, BLACK, (x + 16, y + 40, 28, 40))
            pygame.draw.rect(surface, GRAY, (x + 21, y + 42, 18, 35))

            # Tunic center
            pygame.draw.rect(surface, BLACK, (x + 27, y + 42, 6, 35))

            # --- Brown sleeves ---
            pygame.draw.rect(surface, BROWN, (x + 1, y + 42, 13, 39))
            pygame.draw.rect(surface, BROWN, (x + 46, y + 42, 13, 39))

            # Sleeve shadows
            pygame.draw.rect(surface, BLACK, (x + 1, y + 60, 6, 20))
            pygame.draw.rect(surface, BLACK, (x + 53, y + 60, 6, 20))

            # Hands
            pygame.draw.rect(surface, BEIGE, (x + 2, y + 74, 10, 9))
            pygame.draw.rect(surface, BEIGE, (x + 48, y + 74, 10, 9))

            # --- Belt ---
            pygame.draw.rect(surface, BLACK, (x + 10, y + 76, 40, 9))
            pygame.draw.rect(surface, GRAY, (x + 25, y + 78, 10, 5))

            # --- Legs ---
            pygame.draw.rect(surface, BLACK, (x + 13, y + 84, 14, 26))
            pygame.draw.rect(surface, BLACK, (x + 33, y + 84, 14, 26))

            # Boots
            pygame.draw.rect(surface, BROWN, (x + 10, y + 103, 18, 7))
            pygame.draw.rect(surface, BROWN, (x + 32, y + 103, 18, 7))

        elif self.name == "PALPATINE":
            # --- Large black hood ---
            pygame.draw.rect(surface, BLACK, (x + 16, y, 28, 5))
            pygame.draw.rect(surface, BLACK, (x + 11, y + 4, 38, 9))
            pygame.draw.rect(surface, BLACK, (x + 7, y + 11, 46, 15))
            pygame.draw.rect(surface, BLACK, (x + 3, y + 20, 54, 18))

            # Hood opening
            pygame.draw.rect(surface, (25, 25, 30), (x + 15, y + 15, 30, 23))

            # --- Small pale face ---
            pygame.draw.rect(surface, BEIGE, (x + 19, y + 17, 22, 19))

            # Sunken / shadowed sides of face
            pygame.draw.rect(surface, GRAY, (x + 19, y + 26, 6, 7))
            pygame.draw.rect(surface, GRAY, (x + 35, y + 26, 6, 7))

            # Forehead shadow
            pygame.draw.rect(surface, GRAY, (x + 22, y + 18, 16, 4))

            # Glowing yellow eyes
            pygame.draw.rect(surface, LIGHTNING_YELLOW, (x + 22, y + 23, 6, 3))
            pygame.draw.rect(surface, LIGHTNING_YELLOW, (x + 34, y + 23, 6, 3))

            # Nose
            pygame.draw.rect(surface, GRAY, (x + 29, y + 24, 4, 6))

            # Mouth
            pygame.draw.rect(surface, BLACK, (x + 24, y + 31, 16, 4))
            pygame.draw.rect(surface, GRAY, (x + 27, y + 31, 10, 2))

            # --- Neck ---
            pygame.draw.rect(surface, BLACK, (x + 22, y + 35, 16, 8))

            # --- Huge black robes / shoulders ---
            pygame.draw.rect(surface, BLACK, (x + 9, y + 38, 42, 43))
            pygame.draw.rect(surface, BLACK, (x + 5, y + 45, 50, 36))

            # Dark robe interior
            pygame.draw.rect(surface, (35, 35, 40), (x + 17, y + 43, 26, 36))

            # Robe center
            pygame.draw.rect(surface, BLACK, (x + 27, y + 43, 6, 37))

            # Subtle robe folds
            pygame.draw.rect(surface, (45, 45, 50), (x + 18, y + 50, 5, 27))
            pygame.draw.rect(surface, (45, 45, 50), (x + 37, y + 50, 5, 27))

            # --- Long sleeves / arms ---
            pygame.draw.rect(surface, BLACK, (x + 1, y + 42, 14, 42))
            pygame.draw.rect(surface, BLACK, (x + 45, y + 42, 14, 42))

            # Sleeve shadows
            pygame.draw.rect(surface, (35, 35, 40), (x + 4, y + 48, 5, 27))
            pygame.draw.rect(surface, (35, 35, 40), (x + 50, y + 48, 5, 27))

            # Hands
            pygame.draw.rect(surface, BEIGE, (x + 2, y + 74, 10, 10))
            pygame.draw.rect(surface, BEIGE, (x + 48, y + 74, 10, 10))

            # --- Belt ---
            pygame.draw.rect(surface, BLACK, (x + 9, y + 77, 42, 8))
            pygame.draw.rect(surface, GRAY, (x + 26, y + 78, 9, 5))

            # --- Lower robes ---
            pygame.draw.rect(surface, BLACK, (x + 11, y + 84, 17, 26))
            pygame.draw.rect(surface, BLACK, (x + 32, y + 84, 17, 26))

            # Subtle lower robe highlights
            pygame.draw.rect(surface, (40, 40, 45), (x + 14, y + 87, 5, 19))
            pygame.draw.rect(surface, (40, 40, 45), (x + 41, y + 87, 5, 19))

            # Boots
            pygame.draw.rect(surface, BLACK, (x + 9, y + 103, 20, 7))
            pygame.draw.rect(surface, BLACK, (x + 31, y + 103, 20, 7))

        # Weapon
        direction = 1 if self.facing_right else -1

        if self.weapon == "BLUE_SABER":
            draw_lightsaber(
                surface,
                x + 30,
                y + 70,
                direction,
                LUKE_BLUE
            )

        elif self.weapon == "GREEN_SABER":
            draw_lightsaber(
                surface,
                x + 30,
                y + 70,
                direction,
                SABER_GREEN
            )

        elif self.weapon == "RED_SABER":
            draw_lightsaber(
                surface,
                x + 30,
                y + 70,
                direction,
                VADER_RED
            )

        elif self.weapon == "DOUBLE_SABER":
            draw_lightsaber(
                surface,
                x + 30,
                y + 70,
                direction,
                MAUL_RED,
                double=True
            )

        elif self.weapon == "BLASTER":
            # Han's blaster
            if self.facing_right:
                pygame.draw.rect(
                    surface,
                    GRAY,
                    (x + 42, y + 38, 22, 7)
                )
                pygame.draw.rect(
                    surface,
                    BLACK,
                    (x + 50, y + 43, 7, 10)
                )
            else:
                pygame.draw.rect(
                    surface,
                    GRAY,
                    (x - 4, y + 38, 22, 7)
                )
                pygame.draw.rect(
                    surface,
                    BLACK,
                    (x + 3, y + 43, 7, 10)
                )

        ## close range strike visual box overlay
        if self.is_attacking and self.attack_rect:

            if self.attack_type == "SABER_SWING":
                        # Pixelated saber swing arc
                    if self.weapon == "BLUE_SABER":
                            swing_color = LUKE_BLUE
                    elif self.weapon == "GREEN_SABER":
                            swing_color = SABER_GREEN
                    elif self.weapon == "RED_SABER":
                            swing_color = VADER_RED
                    elif self.weapon == "DOUBLE_SABER":
                            swing_color = MAUL_RED
                    else:
                            swing_color = self.color

                    if self.facing_right:
                            pygame.draw.line(
                                surface,
                                swing_color,
                                (self.rect.right, self.rect.y + 35),
                                (self.rect.right + 45, self.rect.y + 5),
                                7
                            )
                            pygame.draw.line(
                                surface,
                                WHITE,
                                (self.rect.right + 5, self.rect.y + 32),
                                (self.rect.right + 40, self.rect.y + 8),
                                2
                            )
                    else:
                            pygame.draw.line(
                                surface,
                                swing_color,
                                (self.rect.left, self.rect.y + 35),
                                (self.rect.left - 45, self.rect.y + 5),
                                7
                            )
                            pygame.draw.line(
                                surface,
                                WHITE,
                                (self.rect.left - 5, self.rect.y + 32),
                                (self.rect.left - 40, self.rect.y + 8),
                                2
                            )

            elif self.attack_type == "GUNSHOT":
                # Han's blaster flash
                muzzle_x = self.rect.right + 8 if self.facing_right else self.rect.left - 8

                pygame.draw.rect(
                    surface,
                    LIGHTNING_YELLOW,
                    (muzzle_x - 5, self.rect.y + 40, 12, 8)
                )

                pygame.draw.rect(
                    surface,
                    WHITE,
                    (muzzle_x - 2, self.rect.y + 42, 6, 4)
                )

            elif self.attack_type == "FORCE_LIGHTNING":
                # Palpatine reaches out with lightning
                start_x = self.rect.right if self.facing_right else self.rect.left
                end_x = (
                    self.rect.right + 55
                    if self.facing_right
                    else self.rect.left - 55
                )

                pygame.draw.line(
                    surface,
                    LIGHTNING_YELLOW,
                    (start_x, self.rect.y + 45),
                    (end_x, self.rect.y + 25),
                    5
                )

                pygame.draw.line(
                    surface,
                    WHITE,
                    (start_x, self.rect.y + 45),
                    (end_x, self.rect.y + 25),
                    2
                )

def draw_mustafar_background(surface):
    # Dark volcanic sky
    surface.fill((28, 10, 12))

    # Red/orange glow near horizon
    pygame.draw.rect(
        surface,
        (75, 20, 12),
        (0, 70, SCREEN_WIDTH, 250)
    )

    pygame.draw.rect(
        surface,
        (110, 30, 12),
        (0, 230, SCREEN_WIDTH, 120)
    )

    # Distant volcanic mountains
    pygame.draw.polygon(
        surface,
        (35, 15, 15),
        [
            (0, 300),
            (100, 220),
            (180, 290),
            (280, 190),
            (380, 285),
            (500, 210),
            (610, 285),
            (720, 180),
            (830, 280),
            (930, 210),
            (1000, 270),
            (1000, 360),
            (0, 360)
        ]
    )

    # Volcano peaks
    pygame.draw.polygon(
        surface,
        (18, 12, 14),
        [
            (70, 300),
            (145, 190),
            (220, 300)
        ]
    )

    pygame.draw.polygon(
        surface,
        (18, 12, 14),
        [
            (420, 300),
            (500, 170),
            (580, 300)
        ]
    )

    pygame.draw.polygon(
        surface,
        (18, 12, 14),
        [
            (760, 300),
            (835, 185),
            (910, 300)
        ]
    )

    # Volcano glow
    pygame.draw.polygon(
        surface,
        (180, 45, 10),
        [
            (475, 205),
            (500, 175),
            (525, 205)
        ]
    )

    # Lava rivers in the background
    pygame.draw.polygon(
        surface,
        (210, 55, 8),
        [
            (130, 350),
            (210, 350),
            (300, 600),
            (190, 600)
        ]
    )

    pygame.draw.polygon(
        surface,
        (245, 90, 10),
        [
            (160, 350),
            (190, 350),
            (250, 600),
            (215, 600)
        ]
    )

    pygame.draw.polygon(
        surface,
        (210, 55, 8),
        [
            (690, 350),
            (760, 350),
            (850, 600),
            (720, 600)
        ]
    )

    pygame.draw.polygon(
        surface,
        (245, 90, 10),
        [
            (720, 350),
            (745, 350),
            (805, 600),
            (770, 600)
        ]
    )

    # Foreground volcanic ground
    pygame.draw.polygon(
        surface,
        (20, 16, 18),
        [
            (0, 370),
            (100, 350),
            (200, 390),
            (300, 360),
            (400, 400),
            (500, 350),
            (600, 395),
            (700, 355),
            (800, 390),
            (900, 350),
            (1000, 380),
            (1000, 600),
            (0, 600)
        ]
    )

    # Foreground lava cracks
    lava_color = (220, 60, 10)

    pygame.draw.line(
        surface,
        lava_color,
        (80, 600),
        (140, 450),
        5
    )

    pygame.draw.line(
        surface,
        lava_color,
        (140, 450),
        (120, 390),
        4
    )

    pygame.draw.line(
        surface,
        lava_color,
        (400, 600),
        (460, 470),
        5
    )

    pygame.draw.line(
        surface,
        lava_color,
        (460, 470),
        (440, 400),
        4
    )

    pygame.draw.line(
        surface,
        lava_color,
        (900, 600),
        (850, 470),
        5
    )

    pygame.draw.line(
        surface,
        lava_color,
        (850, 470),
        (870, 395),
        4
    )

    # Small glowing lava pools
    pygame.draw.rect(surface, (180, 45, 8), (250, 440, 70, 12))
    pygame.draw.rect(surface, (240, 80, 8), (265, 444, 40, 5))

    pygame.draw.rect(surface, (180, 45, 8), (620, 420, 90, 12))
    pygame.draw.rect(surface, (240, 80, 8), (640, 424, 50, 5))

    # Ash / smoke particles
    ash_particles = [
        (80, 150, 3),
        (150, 100, 2),
        (250, 180, 2),
        (340, 120, 3),
        (430, 90, 2),
        (550, 140, 3),
        (650, 100, 2),
        (760, 150, 3),
        (870, 90, 2),
        (940, 160, 3)
    ]

    for ax, ay, size in ash_particles:
        pygame.draw.rect(
            surface,
            (90, 70, 65),
            (ax, ay, size, size)
        )

def draw_hud(p1, p2):
    # Floor Construction
    pygame.draw.rect(screen, FLOOR_COLOR, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    pygame.draw.rect(screen, GRAY, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 4))
    
    # Left Health Box (P1)
    pygame.draw.rect(screen, (100, 0, 0), (50, 30, 350, 25))
    if p1.health > 0:
        # Scale width dynamically based on individual character's max health parameter
        p1_ratio = 350 / p1.max_health
        pygame.draw.rect(screen, HEALTH_GREEN, (50, 30, p1.health * p1_ratio, 25))
    draw_pixel_text(screen, p1.name, 50, 5, size=2, color=p1.color)
        
    # Right Health Box (P2)
    pygame.draw.rect(screen, (100, 0, 0), (SCREEN_WIDTH - 400, 30, 350, 25))
    if p2.health > 0:
        p2_ratio = 350 / p2.max_health
        pygame.draw.rect(screen, HEALTH_GREEN, (SCREEN_WIDTH - 400, 30, p2.health * p2_ratio, 25))
    p2_lbl = f"{p2.name} (CPU)" if p2.control_type == "cpu" else p2.name
    draw_pixel_text(screen, p2_lbl, SCREEN_WIDTH - 250, 5, size=2, color=p2.color)



# --- CORE GAME LOOP CONTROL SYSTEM ---
game_mode = "MENU" 
opponent_mode = "CPU" 
selected_map = 0
p1_selected_idx = 0
p2_selected_idx = 3

p1_fighter = None
p2_fighter = None
projectiles = []

running = True

play_music(MENU_MUSIC)

while running:
    clock.tick(FPS)
    if selected_map == 0:
        # --- ORIGINAL MAP ---
        screen.fill(BG_DARK)

        # Star Wars-style background architecture
        pygame.draw.rect(
            screen,
            BG_MID,
            (0, 70, SCREEN_WIDTH, 230)
        )

        pygame.draw.rect(
            screen,
            BG_LIGHT,
            (0, 70, SCREEN_WIDTH, 8)
        )

        # Large background structures
        for x in range(40, SCREEN_WIDTH, 160):
            pygame.draw.rect(
                screen,
                BG_MID,
                (x, 120, 80, 180)
            )

            pygame.draw.rect(
                screen,
                BG_LIGHT,
                (x + 15, 140, 50, 8)
            )

            pygame.draw.rect(
                screen,
                BG_LIGHT,
                (x + 15, 170, 50, 8)
            )

            pygame.draw.rect(
                screen,
                BG_LIGHT,
                (x + 15, 200, 50, 8)
            )

        for sx, sy, size in STARS:
            pygame.draw.rect(
                screen,
                WHITE,
                (sx, sy, size, size)
            )

    else:
        # --- MUSTAFAR MAP ---
        draw_mustafar_background(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        elif game_mode == "MENU" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                opponent_mode = "CPU"
                game_mode = "CHAR_SELECT"
            elif event.key == pygame.K_2:
                opponent_mode = "PLAYER2"
                game_mode = "CHAR_SELECT"
                
        elif game_mode == "CHAR_SELECT" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1_selected_idx = (p1_selected_idx - 1) % len(CHARACTERS)
            elif event.key == pygame.K_RIGHT:
                p1_selected_idx = (p1_selected_idx + 1) % len(CHARACTERS)
                
            if opponent_mode == "PLAYER2":
                if event.key == pygame.K_a:
                    p2_selected_idx = (p2_selected_idx - 1) % len(CHARACTERS)
                elif event.key == pygame.K_d:
                    p2_selected_idx = (p2_selected_idx + 1) % len(CHARACTERS)
            else: 
                # Anti-Duplicate CPU Selection Engine
                p2_selected_idx = random.randint(0, len(CHARACTERS) - 1)
                while p2_selected_idx == p1_selected_idx:
                    p2_selected_idx = random.randint(0, len(CHARACTERS) - 1)
                
            if event.key == pygame.K_RETURN:
                game_mode = "MAP_SELECT"

        elif game_mode == "MAP_SELECT" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_map = 0

            elif event.key == pygame.K_RIGHT:
                selected_map = 1

            elif event.key == pygame.K_RETURN:
                p1_fighter = Fighter(
                    200, 400,
                    CHARACTERS[p1_selected_idx],
                    "player_1"
                )

                p2_ctrl = "cpu" if opponent_mode == "CPU" else "player_2"

                p2_fighter = Fighter(
                    740, 400,
                    CHARACTERS[p2_selected_idx],
                    p2_ctrl
                )

                projectiles = []

                play_music(BATTLE_MUSIC)

                game_mode = "PLAYING"
                
        elif game_mode == "GAMEOVER" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: 
                p1_fighter = None
                p2_fighter = None
                projectiles = []
                play_music(MENU_MUSIC)
                game_mode = "MENU"

    # --- MACHINE STATE DRAW MATRIX ---
    if game_mode == "MENU":
        draw_pixel_text(screen, "STAR WARS: RETRO DUEL", 200, 80, size=5, color=WHITE)
        
        pygame.draw.rect(screen, LUKE_BLUE, (150, 200, 700, 65)) 
        draw_pixel_text(screen, "PRESS (1) FOR SINGLE PLAYER (VS CPU)", 180, 222, size=3, color=WHITE)
        
        pygame.draw.rect(screen, VADER_RED, (150, 300, 700, 65))  
        draw_pixel_text(screen, "PRESS (2) FOR LOCAL 2 PLAYER", 240, 322, size=3, color=WHITE)
        
        pygame.draw.rect(screen, GRAY, (150, 410, 700, 120), 2)
        draw_pixel_text(screen, "CHOOSE MODE TO ENTER CHARACTER SELECTION", 210, 455, size=2, color=GRAY)

    elif game_mode == "CHAR_SELECT":
        draw_pixel_text(screen, "SELECT YOUR FIGHTER", 260, 40, size=4, color=WHITE)
        
        for i, char in enumerate(CHARACTERS):
            row = i // 3
            col = i % 3
            bx = 120 + col * 270
            by = 130 + row * 190
            
            pygame.draw.rect(screen, FLOOR_COLOR, (bx, by, 220, 160))
            draw_pixel_text(screen, char["name"], bx + 15, by + 15, size=2, color=char["color"])
            draw_pixel_text(screen, "POWER:", bx + 15, by + 110, size=1, color=GRAY)
            draw_pixel_text(screen, char["ability"], bx + 15, by + 130, size=1, color=WHITE)
            
            if i == p1_selected_idx:
                pygame.draw.rect(screen, LUKE_BLUE, (bx - 4, by - 4, 228, 168), 4)
                draw_pixel_text(screen, "(P1)", bx + 160, by + 15, size=2, color=LUKE_BLUE)
            if i == p2_selected_idx and opponent_mode == "PLAYER2":
                pygame.draw.rect(screen, VADER_RED, (bx - 8, by - 8, 236, 176), 3)
                draw_pixel_text(screen, "(P2)", bx + 160, by + 40, size=2, color=VADER_RED)

                draw_pixel_text(screen, "P1: USE LEFT/RIGHT ARROWS TO MOVE CURSOR", 180, 510, size=2, color=LUKE_BLUE)
        if opponent_mode == "PLAYER2":
            draw_pixel_text(screen, "P2: USE (A) / (D) KEYS TO CHOOSE FIGHTER", 180, 535, size=2, color=VADER_RED)
        draw_pixel_text(screen, "PRESS [ENTER] TO COMMENCE BATTLE", 270, 565, size=2, color=HEALTH_GREEN)

    elif game_mode == "MAP_SELECT":
        draw_pixel_text(
            screen,
            "CHOOSE YOUR BATTLEFIELD",
            245,
            45,
            size=4,
            color=WHITE
        )

        # Map 1 preview
        pygame.draw.rect(
            screen,
            BG_MID,
            (100, 150, 350, 220)
        )

        pygame.draw.rect(
            screen,
            BG_LIGHT,
            (100, 150, 350, 8)
        )

        for x in range(120, 450, 80):
            pygame.draw.rect(
                screen,
                BG_LIGHT,
                (x, 210, 45, 100)
            )

        for sx, sy, size in STARS:
            if 100 <= sx <= 450 and 150 <= sy <= 370:
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (sx, sy, size, size)
                )

        draw_pixel_text(
            screen,
            "ORIGINAL MAP",
            180,
            390,
            size=2,
            color=LUKE_BLUE
        )

        # Map 2 preview
        pygame.draw.rect(
            screen,
            (28, 10, 12),
            (550, 150, 350, 220)
        )

        # Mustafar preview sky
        pygame.draw.rect(
            screen,
            (100, 25, 12),
            (550, 220, 350, 150)
        )

        # Mountains
        pygame.draw.polygon(
            screen,
            (25, 12, 14),
            [
                (550, 330),
                (620, 250),
                (690, 330),
                (760, 235),
                (830, 330),
                (900, 255),
                (900, 370),
                (550, 370)
            ]
        )

        # Lava
        pygame.draw.polygon(
            screen,
            (220, 60, 8),
            [
                (620, 370),
                (680, 370),
                (720, 370),
                (800, 370),
                (850, 370),
                (900, 370)
            ]
        )

        draw_pixel_text(
            screen,
            "MUSTAFAR",
            670,
            390,
            size=2,
            color=VADER_RED
        )

        # Selection boxes
        if selected_map == 0:
            pygame.draw.rect(
                screen,
                LUKE_BLUE,
                (90, 140, 370, 260),
                5
            )
        else:
            pygame.draw.rect(
                screen,
                VADER_RED,
                (540, 140, 370, 260),
                5
            )

        draw_pixel_text(
            screen,
            "USE LEFT / RIGHT TO CHOOSE",
            275,
            470,
            size=2,
            color=GRAY
        )

        draw_pixel_text(
            screen,
            "PRESS [ENTER] TO BATTLE",
            300,
            520,
            size=2,
            color=HEALTH_GREEN
        )
    elif game_mode == "PLAYING":
        p1_fighter.move(p2_fighter.rect, projectiles)
        p2_fighter.move(p1_fighter.rect, projectiles)
        
        # --- RANGED PROJECTILE INTERSECTIONS WITH HITSTUN ENGINE ---
        # Update projectiles and check collisions
        for p in projectiles:
            p.update()

            if p.owner == p1_fighter:
                if p.rect.colliderect(p2_fighter.rect):

                    if p.p_type == "FORCE CHOKE":
                        p2_fighter.apply_force_choke()

                        # Push the opponent away from Vader
                        p2_fighter.force_choke_velocity = (
                            2 if p1_fighter.facing_right else -2
                        )

                        p2_fighter.take_damage(20)

                    else:
                        p2_fighter.take_damage(20)

                    p.active = False

            elif p.owner == p2_fighter:
                if p.rect.colliderect(p1_fighter.rect):

                    if p.p_type == "FORCE CHOKE":
                        p1_fighter.apply_force_choke()

                        p1_fighter.force_choke_velocity = (
                            2 if p2_fighter.facing_right else -2
                        )

                        p1_fighter.take_damage(20)

                    else:
                        p1_fighter.take_damage(20)

                    p.active = False

        # Remove inactive projectiles
        projectiles = [p for p in projectiles if p.active]

        # --- CLOSE RANGE LIGHTSABER INTERSECTIONS WITH HITSTUN ENGINE ---
        if p1_fighter.is_attacking and p1_fighter.attack_rect and p1_fighter.attack_rect.colliderect(p2_fighter.rect):
            p2_fighter.take_damage(10, standard_attack=True) # Applies standard melee hitstun
            p1_fighter.is_attacking = False  
            
        if p2_fighter.is_attacking and p2_fighter.attack_rect and p2_fighter.attack_rect.colliderect(p1_fighter.rect):
            p1_fighter.take_damage(10, standard_attack=True)
            p2_fighter.is_attacking = False

        # --- RENDER STEP (Leave everything else below this inside your loop as-is) ---
        for p in projectiles:
            p.draw(screen)
        p1_fighter.draw(screen)
        p2_fighter.draw(screen)
        draw_hud(p1_fighter, p2_fighter)

        # Draw Cooldown Timers
        p1_cooldown_lbl = "READY" if p1_fighter.special_cooldown == 0 else "CHARGING"
        draw_pixel_text(screen, f"SPECIAL (M): {p1_cooldown_lbl}", 50, 60, size=1, color=GRAY)
        if p2_fighter.control_type == "player_2":
            p2_cooldown_lbl = "READY" if p2_fighter.special_cooldown == 0 else "CHARGING"
            draw_pixel_text(screen, f"SPECIAL (G): {p2_cooldown_lbl}", SCREEN_WIDTH - 240, 60, size=1, color=GRAY)

        if p1_fighter.health <= 0 or p2_fighter.health <= 0:
            game_mode = "GAMEOVER"


    elif game_mode == "GAMEOVER":
        p1_fighter.draw(screen)
        p2_fighter.draw(screen)
        draw_hud(p1_fighter, p2_fighter)
        
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT // 2 - 60, SCREEN_WIDTH, 120))
        pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT // 2 - 60, SCREEN_WIDTH, 120), 4)
        
        if p1_fighter.health <= 0:
            draw_pixel_text(screen, f"{p2_fighter.name} WINS!", 320, SCREEN_HEIGHT // 2 - 35, size=5, color=VADER_RED)
        else:
            draw_pixel_text(screen, f"{p1_fighter.name} WINS!", 320, SCREEN_HEIGHT // 2 - 35, size=5, color=LUKE_BLUE)
            
        draw_pixel_text(screen, "PRESS [R] TO RETURN TO MAIN MENU", 310, SCREEN_HEIGHT // 2 + 25, size=2, color=GRAY)

    pygame.display.update()

