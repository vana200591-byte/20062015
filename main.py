import pygame
import sys
import os
import math
import random

# =========================================================
# FOOTBALL ULTIMATE 3D - BETA 0.4
# Pygame 3D perspective renderer + 11v11 gameplay
# =========================================================

pygame.init()

try:
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except Exception:
    AUDIO_AVAILABLE = False

WIDTH, HEIGHT = 1280, 720
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Ultimate 3D - Beta 0.4")
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(BASE_DIR, "Resources")
# Support the older lowercase folder layout too.
if not os.path.isdir(RESOURCE_DIR):
    RESOURCE_DIR = os.path.join(BASE_DIR, "resources")

IMAGE_DIR = os.path.join(RESOURCE_DIR, "Images")
SOUND_DIR = os.path.join(RESOURCE_DIR, "Sounds", "SFX")

PLAYER_IMAGE = os.path.join(IMAGE_DIR, "Players", "Bodies", "Male", "player.png")
BALL_IMAGE = os.path.join(IMAGE_DIR, "Ball", "Ball.png")
BALL_SHADOW_IMAGE = os.path.join(IMAGE_DIR, "Ball", "Ball_Shadow.png")
PLAYER_SHADOW_IMAGE = os.path.join(IMAGE_DIR, "Players", "Shadow", "player_shadow.png")

# Match intro club logos. Put real club PNGs here later if desired.
LOGO_DIR = os.path.join(IMAGE_DIR, "Teams", "Logos")
HOME_LOGO_PATH = os.path.join(LOGO_DIR, "blue_sharks.png")
AWAY_LOGO_PATH = os.path.join(LOGO_DIR, "red_lions.png")
HOME_TEAM_NAME = "BLUE SHARKS"
AWAY_TEAM_NAME = "RED LIONS"
MATCH_INTRO_DURATION = 3.2
match_intro_timer = 0.0
selected_team = "blue"
selected_player_number = 10

# ---------------------------------------------------------
# Fonts / colors
# ---------------------------------------------------------
font_title = pygame.font.Font(None, 82)
font_big = pygame.font.Font(None, 60)
font_button = pygame.font.Font(None, 40)
font_subtitle = pygame.font.Font(None, 34)
font_small = pygame.font.Font(None, 27)
font_tiny = pygame.font.Font(None, 20)

WHITE = (255, 255, 255)
BLACK = (5, 8, 10)
DARK = (8, 15, 24)
DARK2 = (15, 28, 42)
GRAY = (150, 160, 170)
GREEN = (40, 155, 55)
GREEN_LIGHT = (95, 230, 90)
BLUE = (35, 100, 210)
BLUE_LIGHT = (70, 145, 255)
RED = (210, 45, 45)
RED_LIGHT = (245, 75, 75)
GOLD = (255, 190, 40)
CYAN = (40, 200, 230)

# ---------------------------------------------------------
# Assets
# ---------------------------------------------------------
def load_image(path):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        return None

player_sprite = load_image(PLAYER_IMAGE)
ball_sprite = load_image(BALL_IMAGE)
ball_shadow_sprite = load_image(BALL_SHADOW_IMAGE)
player_shadow_sprite = load_image(PLAYER_SHADOW_IMAGE)

def make_fallback_logo(main_color, accent_color, letter):
    surf = pygame.Surface((220, 220), pygame.SRCALPHA)
    pygame.draw.circle(surf, (8, 14, 22, 235), (110, 110), 104)
    pygame.draw.circle(surf, main_color, (110, 110), 88)
    pygame.draw.circle(surf, accent_color, (110, 110), 88, 7)
    f = pygame.font.Font(None, 92)
    txt = f.render(letter, True, WHITE)
    surf.blit(txt, txt.get_rect(center=(110, 108)))
    return surf

def load_logo(path, fallback_color, accent_color, letter):
    img = load_image(path)
    if img:
        return pygame.transform.smoothscale(img, (220, 220))
    return make_fallback_logo(fallback_color, accent_color, letter)

home_logo = load_logo(HOME_LOGO_PATH, BLUE, BLUE_LIGHT, "B")
away_logo = load_logo(AWAY_LOGO_PATH, RED, RED_LIGHT, "R")

sounds = {}
if AUDIO_AVAILABLE:
    for name in ("goal", "whistle", "pass", "kick"):
        p = os.path.join(SOUND_DIR, f"{name}.wav")
        if os.path.exists(p):
            try:
                sounds[name] = pygame.mixer.Sound(p)
            except Exception:
                pass

def play_sound(name):
    try:
        if sound_on and name in sounds:
            sounds[name].play()
    except Exception:
        pass

# ---------------------------------------------------------
# Menu state
# ---------------------------------------------------------
current_page = "menu"
music_on = True
sound_on = True
username = "PLAYER"
level, xp, xp_max = 1, 120, 500
coins, gems = 1250, 50
matches, wins, goals_total = 0, 0, 0

def draw_text(text, font, color, x, y, center=False):
    surf = font.render(str(text), True, color)
    rect = surf.get_rect()
    rect.center = (x, y) if center else rect.center
    if not center:
        rect.topleft = (x, y)
    screen.blit(surf, rect)

def panel(rect, color=DARK2, border=GRAY, radius=12):
    pygame.draw.rect(screen, color, rect, border_radius=radius)
    if border:
        pygame.draw.rect(screen, border, rect, 2, border_radius=radius)

class Button:
    def __init__(self, x, y, w, h, text, color=DARK2, hover=BLUE):
        self.rect = pygame.Rect(x, y, w, h)
        self.text, self.color, self.hover = text, color, hover

    def draw(self):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, self.hover if hovered else self.color,
                         self.rect, border_radius=12)
        pygame.draw.rect(screen, WHITE if hovered else GRAY,
                         self.rect, 2, border_radius=12)
        draw_text(self.text, font_button, WHITE,
                  self.rect.centerx, self.rect.centery, True)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                play_sound("pass")
                return True
        return False

play_button = Button(60, 260, 390, 75, "PLAY", GREEN, GREEN_LIGHT)
profile_button = Button(60, 350, 390, 65, "PROFILE")
team_button = Button(60, 430, 390, 65, "TEAM")
settings_button = Button(60, 510, 390, 65, "SETTINGS")
shop_button = Button(480, 590, 150, 60, "SHOP")
news_button = Button(645, 590, 150, 60, "NEWS")
league_button = Button(810, 590, 180, 60, "LEAGUES")
quit_button = Button(1005, 590, 150, 60, "QUIT", RED, RED_LIGHT)

quick_match_button = Button(350, 290, 580, 80, "QUICK MATCH", GREEN, GREEN_LIGHT)
tournament_button = Button(350, 390, 580, 80, "TOURNAMENT")
back_button = Button(40, 630, 180, 55, "BACK")
music_button = Button(350, 280, 580, 65, "MUSIC")
sound_button = Button(350, 360, 580, 65, "SOUND")
fullscreen_button = Button(350, 440, 580, 65, "FULLSCREEN")

# =========================================================
# 3D WORLD
# =========================================================
FIELD_W = 105.0
FIELD_L = 150.0
GOAL_W = 18.0
GOAL_H = 5.5
PENALTY_W = 40.0
PENALTY_L = 22.0

# Camera position / target. This is a real perspective projection,
# not a flat top-down 2D field.
CAM_POS = (0.0, -125.0, 72.0)
CAM_TARGET = (0.0, 18.0, 0.0)
FOV = math.radians(62)

def vsub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def vmul(a, s):
    return (a[0]*s, a[1]*s, a[2]*s)

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def norm(v):
    l = math.sqrt(dot(v, v)) or 1.0
    return (v[0]/l, v[1]/l, v[2]/l)

forward = norm(vsub(CAM_TARGET, CAM_POS))
world_up = (0.0, 0.0, 1.0)
right = norm(cross(forward, world_up))
up = norm(cross(right, forward))

focal = (WIDTH / 2) / math.tan(FOV / 2)

def project(x, y, z=0.0):
    """Project world XYZ into screen coordinates with perspective."""
    rel = (x-CAM_POS[0], y-CAM_POS[1], z-CAM_POS[2])
    cx = dot(rel, right)
    cy = dot(rel, up)
    cz = dot(rel, forward)
    if cz <= 1.0:
        return None
    scale = focal / cz
    return (WIDTH/2 + cx*scale, HEIGHT/2 - cy*scale, cz, scale)

def draw_world_line(a, b, color, width=2):
    pa, pb = project(*a), project(*b)
    if pa and pb:
        pygame.draw.line(screen, color, pa[:2], pb[:2],
                         max(1, int(width * min(pa[3], pb[3]) * 3)))

def draw_ground_polygon(points, color):
    ps = [project(*p) for p in points]
    if all(ps):
        pygame.draw.polygon(screen, color, [p[:2] for p in ps])

# ---------------------------------------------------------
# Match objects
# ---------------------------------------------------------
class Player3D:
    def __init__(self, team, number, x, y, role):
        self.team = team
        self.number = number
        self.x, self.y, self.z = x, y, 0.0
        self.home_x, self.home_y = x, y
        self.role = role
        self.speed = 18.0 if role != "GK" else 16.0
        self.sprint = 25.0
        self.facing_x = 0.0
        self.facing_y = 1.0 if team == "blue" else -1.0
        self.selected = (team == selected_team and number == selected_player_number)

    def distance_to_ball(self):
        return math.hypot(self.x-ball.x, self.y-ball.y)

    def move_towards(self, tx, ty, dt, speed=None):
        dx, dy = tx-self.x, ty-self.y
        d = math.hypot(dx, dy)
        if d > 0.01:
            sp = speed or self.speed
            step = min(d, sp*dt)
            self.x += dx/d*step
            self.y += dy/d*step
            self.facing_x, self.facing_y = dx/d, dy/d

    def clamp(self):
        self.x = max(-FIELD_W/2+2, min(FIELD_W/2-2, self.x))
        self.y = max(-FIELD_L/2+2, min(FIELD_L/2-2, self.y))

blue = []
red = []
ball = None
score_blue = 0
score_red = 0
match_message = ""
message_timer = 0.0

blue_formation = [
    ("GK", 1, 0, -67), ("DEF", 2, -35, -53), ("DEF", 3, -12, -56),
    ("DEF", 4, 12, -56), ("DEF", 5, 35, -53),
    ("MID", 6, -27, -25), ("MID", 8, 0, -20), ("MID", 7, 27, -25),
    ("ATT", 11, -30, 8), ("ATT", 10, 0, 15), ("ATT", 9, 30, 8)
]
red_formation = [
    ("GK", 1, 0, 67), ("DEF", 2, 35, 53), ("DEF", 3, 12, 56),
    ("DEF", 4, -12, 56), ("DEF", 5, -35, 53),
    ("MID", 6, 27, 25), ("MID", 8, 0, 20), ("MID", 7, -27, 25),
    ("ATT", 11, 30, -8), ("ATT", 10, 0, -15), ("ATT", 9, -30, -8)
]

class Ball3D:
    def __init__(self):
        self.x = self.y = self.z = 0.0
        self.vx = self.vy = self.vz = 0.0
        self.owner = None
        self.last_touch = None
        self.radius = 1.15

    def reset(self):
        self.x = self.y = self.z = 0.0
        self.vx = self.vy = self.vz = 0.0
        self.owner = None
        self.last_touch = None

    def kick(self, vx, vy, vz=2.2):
        self.owner = None
        self.vx, self.vy, self.vz = vx, vy, vz

def setup_match():
    global blue, red, ball, score_blue, score_red, match_message, message_timer, match_intro_timer
    blue = [Player3D("blue", n, x, y, role) for role,n,x,y in blue_formation]
    red = [Player3D("red", n, x, y, role) for role,n,x,y in red_formation]
    # Exactly one controlled player, on the selected team.
    for p in blue + red:
        p.selected = (p.team == selected_team and p.number == selected_player_number)
    ball = Ball3D()
    score_blue = score_red = 0
    match_message = "KICK OFF!"
    message_timer = 2.0
    match_intro_timer = MATCH_INTRO_DURATION

def controlled_player():
    team = blue if selected_team == "blue" else red
    for p in team:
        if p.selected:
            return p
    team[0].selected = True
    return team[0]

def select_player(player):
    global selected_player_number
    team = blue if selected_team == "blue" else red
    for p in team:
        p.selected = False
    player.selected = True
    selected_player_number = player.number

def nearest_player(team):
    return min(team, key=lambda p: p.distance_to_ball())

def acquire_ball():
    if ball.owner is not None or ball.z > 2.2:
        return
    candidates = blue + red
    p = min(candidates, key=lambda q: q.distance_to_ball())
    if p.distance_to_ball() < 2.6 and math.hypot(ball.vx, ball.vy) < 8:
        ball.owner = p
        ball.vx = ball.vy = ball.vz = 0.0
        ball.last_touch = p

def user_update(dt):
    p = controlled_player()
    keys = pygame.key.get_pressed()
    dx = float(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - float(keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = float(keys[pygame.K_w] or keys[pygame.K_UP]) - float(keys[pygame.K_s] or keys[pygame.K_DOWN])
    moving = dx != 0 or dy != 0
    if moving:
        l = math.hypot(dx, dy)
        dx, dy = dx/l, dy/l
        speed = p.sprint if keys[pygame.K_LSHIFT] else p.speed
        p.x += dx*speed*dt
        p.y += dy*speed*dt
        p.facing_x, p.facing_y = dx, dy
    p.clamp()

    # Keep possession under the controlled player.
    if ball.owner is p:
        bx = p.x + p.facing_x*2.0
        by = p.y + p.facing_y*2.0
        ball.x, ball.y, ball.z = bx, by, 0.9

def switch_player():
    team = blue if selected_team == "blue" else red
    p = controlled_player()
    candidates = sorted(team, key=lambda q: q.distance_to_ball())
    if candidates:
        idx = candidates.index(p) if p in candidates else -1
        select_player(candidates[(idx + 1) % len(candidates)])

def shoot_user():
    p = controlled_player()
    if ball.owner is not p and p.distance_to_ball() > 3.2:
        return
    if ball.owner is not p:
        ball.owner = p
    # Shoot toward the opponent goal.
    target_x = 0.0
    target_y = FIELD_L/2 + 4 if p.team == "blue" else -FIELD_L/2 - 4
    dx, dy = target_x-ball.x, target_y-ball.y
    d = math.hypot(dx, dy) or 1
    power = 46.0
    ball.last_touch = p
    ball.kick(dx/d*power, dy/d*power, 7.0)
    play_sound("kick")

def pass_user():
    p = controlled_player()
    if ball.owner is not p and p.distance_to_ball() > 3.2:
        return
    teammates = [q for q in (blue if p.team == "blue" else red) if q is not p]
    target = min(teammates, key=lambda q: math.hypot(q.x-(p.x+p.facing_x*20), q.y-(p.y+p.facing_y*20)))
    dx, dy = target.x-ball.x, target.y-ball.y
    d = math.hypot(dx, dy) or 1
    ball.last_touch = p
    ball.kick(dx/d*30, dy/d*30, 2.5)
    play_sound("pass")

def ai_update(dt):
    for team, opponent in ((red, blue), (blue, red)):
        for p in team:
            if p.selected:
                continue
            if ball.owner is p:
                # AI attacks the opposite goal and shoots when close enough.
                goal_y = FIELD_L/2 + 5 if p.team == "red" else -FIELD_L/2 - 5
                # Red attacks -Y; Blue attacks +Y.
                goal_y = -FIELD_L/2 - 5 if p.team == "red" else FIELD_L/2 + 5
                dist_goal = abs(goal_y-p.y)
                if dist_goal < 34 and abs(p.x) < GOAL_W*0.9:
                    dx, dy = -p.x, goal_y-p.y
                    d = math.hypot(dx, dy) or 1
                    ball.kick(dx/d*40, dy/d*40, 6.0)
                    ball.last_touch = p
                    play_sound("kick")
                else:
                    p.move_towards(p.x + p.facing_x*12, p.y + p.facing_y*12, dt)
                    ball.x, ball.y, ball.z = p.x+p.facing_x*2, p.y+p.facing_y*2, 0.9
                continue

            nearest = nearest_player(team)
            if p is nearest and ball.owner is None:
                p.move_towards(ball.x, ball.y, dt, p.speed*1.15)
            else:
                # Maintain formation, with a little tactical reaction.
                tx = p.home_x + max(-7, min(7, ball.x*0.12))
                ty = p.home_y + max(-9, min(9, ball.y*0.10))
                if p.team == "red":
                    ty = p.home_y + max(-9, min(9, ball.y*0.10))
                p.move_towards(tx, ty, dt, p.speed*0.55)
            p.clamp()

    # The defending nearest player can steal a slowly moving ball.
    if ball.owner is not None:
        owner = ball.owner
        enemies = red if owner.team == "blue" else blue
        chaser = min(enemies, key=lambda q: q.distance_to_ball())
        if chaser.distance_to_ball() < 2.0 and ball.z < 1.5:
            ball.owner = chaser
            ball.last_touch = chaser

def update_ball(dt):
    if ball.owner is not None:
        return

    ball.x += ball.vx*dt
    ball.y += ball.vy*dt
    ball.z += ball.vz*dt
    ball.vz -= 18.0*dt
    drag = max(0.0, 1.0-2.0*dt)
    ball.vx *= drag
    ball.vy *= drag
    ball.vz *= 0.995

    if ball.z <= 0:
        ball.z = 0
        if abs(ball.vz) > 1.0:
            ball.vz *= -0.45
        else:
            ball.vz = 0
        ball.vx *= 0.96
        ball.vy *= 0.96

    # Side lines.
    if abs(ball.x) > FIELD_W/2:
        ball.x = math.copysign(FIELD_W/2, ball.x)
        ball.vx *= -0.65

def check_goal():
    global score_blue, score_red, match_message, message_timer, goals_total
    if abs(ball.x) <= GOAL_W/2 and ball.z <= GOAL_H:
        if ball.y >= FIELD_L/2 + 1:
            score_blue += 1
            goals_total += 1
            match_message = "GOAL!  BLUE SHARKS"
            message_timer = 2.8
            play_sound("goal")
            ball.reset()
            for p in blue + red:
                p.x, p.y = p.home_x, p.home_y
            return
        if ball.y <= -FIELD_L/2 - 1:
            score_red += 1
            match_message = "GOAL!  RED LIONS"
            message_timer = 2.8
            play_sound("goal")
            ball.reset()
            for p in blue + red:
                p.x, p.y = p.home_x, p.home_y

def update_match(dt):
    global message_timer
    user_update(dt)
    ai_update(dt)
    acquire_ball()
    update_ball(dt)
    check_goal()
    if message_timer > 0:
        message_timer -= dt

# =========================================================
# 3D DRAWING
# =========================================================
def draw_pitch_3d():
    screen.fill((18, 50, 78))
    # Ground plane.
    draw_ground_polygon([
        (-FIELD_W/2, -FIELD_L/2, 0),
        ( FIELD_W/2, -FIELD_L/2, 0),
        ( FIELD_W/2,  FIELD_L/2, 0),
        (-FIELD_W/2,  FIELD_L/2, 0)
    ], (35, 125, 48))

    # Alternating grass strips.
    strip = 15
    for y0 in range(int(-FIELD_L/2), int(FIELD_L/2), strip):
        c = (39, 135, 51) if ((y0+int(FIELD_L/2))//strip) % 2 == 0 else (35, 125, 48)
        draw_ground_polygon([
            (-FIELD_W/2, y0, 0.01), (FIELD_W/2, y0, 0.01),
            (FIELD_W/2, y0+strip, 0.01), (-FIELD_W/2, y0+strip, 0.01)
        ], c)

    # Lines.
    white = (235, 245, 240)
    x = FIELD_W/2
    y = FIELD_L/2
    draw_world_line((-x,-y,0.05),(x,-y,0.05),white,2)
    draw_world_line((x,-y,0.05),(x,y,0.05),white,2)
    draw_world_line((x,y,0.05),(-x,y,0.05),white,2)
    draw_world_line((-x,y,0.05),(-x,-y,0.05),white,2)
    draw_world_line((0,-y,0.05),(0,y,0.05),white,2)

    # Center circle.
    pts = []
    for i in range(49):
        a = 2*math.pi*i/48
        pts.append((math.cos(a)*12, math.sin(a)*12, 0.05))
    for a,b in zip(pts, pts[1:]):
        draw_world_line(a,b,white,2)

    # Penalty boxes + six-yard boxes.
    for side in (-1, 1):
        gy = side*y
        py = gy - side*PENALTY_L
        sy = gy - side*8
        for w, yy in ((PENALTY_W, py), (22, sy)):
            draw_world_line((-w/2, gy, .05),(w/2, gy, .05),white,2)
            draw_world_line((-w/2, gy, .05),(-w/2, yy, .05),white,2)
            draw_world_line((w/2, gy, .05),(w/2, yy, .05),white,2)
            draw_world_line((-w/2, yy, .05),(w/2, yy, .05),white,2)

    # Goals as 3D frames + net.
    for side in (-1, 1):
        gy = side*(FIELD_L/2)
        front = gy
        back = gy + side*7
        z = GOAL_H
        draw_world_line((-GOAL_W/2,front,0),(GOAL_W/2,front,0),white,3)
        draw_world_line((-GOAL_W/2,front,0),(-GOAL_W/2,front,z),white,3)
        draw_world_line((GOAL_W/2,front,0),(GOAL_W/2,front,z),white,3)
        draw_world_line((-GOAL_W/2,front,z),(GOAL_W/2,front,z),white,3)
        draw_world_line((-GOAL_W/2,front,0),(-GOAL_W/2,back,0),white,2)
        draw_world_line((GOAL_W/2,front,0),(GOAL_W/2,back,0),white,2)
        draw_world_line((-GOAL_W/2,front,z),(-GOAL_W/2,back,z),white,2)
        draw_world_line((GOAL_W/2,front,z),(GOAL_W/2,back,z),white,2)
        # Net lines.
        for i in range(1,5):
            xx = -GOAL_W/2 + GOAL_W*i/5
            draw_world_line((xx,front,0),(xx,back,0),(185,195,190),1)

def billboard_player(p):
    pr = project(p.x, p.y, 0)
    head = project(p.x, p.y, 2.8)
    if not pr or not head:
        return
    sx, sy, depth, scale = pr
    _, hy, _, _ = head
    height = max(24, min(155, int(abs(sy-hy))))
    width = max(12, int(height*0.48))
    rect = pygame.Rect(0,0,width,height)
    rect.midbottom = (int(sx), int(sy))

    # Ground shadow.
    pygame.draw.ellipse(screen, (15,35,18),
                        (rect.centerx-width//2, int(sy-height*0.05),
                         width, max(4, height//8)))

    if player_sprite:
        img = pygame.transform.smoothscale(player_sprite, (width,height))
        # Tint with a team jersey overlay so the same supplied player asset
        # can represent both teams.
        tinted = img.copy()
        tint = BLUE_LIGHT if p.team == "blue" else RED_LIGHT
        overlay = pygame.Surface((width,height), pygame.SRCALPHA)
        overlay.fill((*tint, 70))
        tinted.blit(overlay,(0,0),special_flags=pygame.BLEND_RGBA_ADD)
        screen.blit(tinted, rect)
    else:
        pygame.draw.ellipse(screen, BLUE_LIGHT if p.team=="blue" else RED_LIGHT, rect)

    if p.selected:
        # Bright 3D-style selection aura + arrow so the controlled player is obvious.
        glow = pygame.Surface((width*3, height*2), pygame.SRCALPHA)
        gx, gy = glow.get_width()//2, glow.get_height()-22
        for r, a in ((42,28),(34,45),(26,75)):
            pygame.draw.circle(glow, (*GOLD, a), (gx, gy), r, 5)
        pygame.draw.polygon(glow, (*GOLD, 240), [(gx,gy-22),(gx-11,gy-4),(gx+11,gy-4)])
        screen.blit(
    glow,
    (int(sx) - gx, int(sy) - glow.get_height() + 22)
)
        pygame.draw.ellipse(screen, GOLD, (int(sx-width*0.72), int(sy-height*0.04), int(width*1.44), max(5,int(height*0.10))), 3)

    # Shirt number.
    draw_text(str(p.number), font_tiny, WHITE, int(sx), int(sy-height*0.56), True)

def draw_ball_3d():
    pr = project(ball.x, ball.y, ball.z)
    ground = project(ball.x, ball.y, 0)
    if not pr or not ground:
        return
    sx, sy, depth, scale = pr
    radius = max(4, min(20, int(7.5*scale)))
    # Shadow shrinks toward the ball.
    gsx, gsy = ground[:2]
    shadow_w = max(7, radius*2)
    pygame.draw.ellipse(screen, (20,30,20),
                        (int(gsx-shadow_w/2), int(gsy-radius/3),
                         shadow_w, max(3,radius//2)))
    if ball_sprite:
        img = pygame.transform.smoothscale(ball_sprite, (radius*2,radius*2))
        screen.blit(img, (int(sx-radius), int(sy-radius)))
    else:
        pygame.draw.circle(screen, WHITE, (int(sx),int(sy)), radius)
        pygame.draw.circle(screen, BLACK, (int(sx),int(sy)), radius, 1)

def draw_match_intro():
    screen.fill((6, 12, 22))

    # Subtle stadium-style background.
    for y in range(HEIGHT):
        t = y / max(1, HEIGHT - 1)
        c = (int(8 + 12*t), int(18 + 22*t), int(32 + 28*t))
        pygame.draw.line(screen, c, (0, y), (WIDTH, y))

    # Pitch glow near the bottom.
    pygame.draw.ellipse(screen, (20, 80, 35), (WIDTH//2-520, 520, 1040, 260))

    draw_text("MATCH DAY", font_title, WHITE, WIDTH//2, 85, True)
    draw_text("FOOTBALL ULTIMATE 3D", font_small, GREEN_LIGHT, WIDTH//2, 145, True)

    left = pygame.Rect(WIDTH//2-430, 235, 260, 260)
    right_rect = pygame.Rect(WIDTH//2+170, 235, 260, 260)
    panel(left, (8,18,28), BLUE_LIGHT, 24)
    panel(right_rect, (8,18,28), RED_LIGHT, 24)
    screen.blit(home_logo, home_logo.get_rect(center=left.center))
    screen.blit(away_logo, away_logo.get_rect(center=right_rect.center))

    draw_text("VS", font_title, GOLD, WIDTH//2, 365, True)
    draw_text(HOME_TEAM_NAME, font_subtitle, BLUE_LIGHT, WIDTH//2-300, 535, True)
    draw_text(AWAY_TEAM_NAME, font_subtitle, RED_LIGHT, WIDTH//2+300, 535, True)

    # Countdown bar.
    progress = max(0.0, min(1.0, match_intro_timer / MATCH_INTRO_DURATION))
    pygame.draw.rect(screen, (35,45,55), (WIDTH//2-260, 610, 520, 12), border_radius=6)
    pygame.draw.rect(screen, GREEN_LIGHT, (WIDTH//2-260, 610, int(520*(1-progress)), 12), border_radius=6)
    draw_text("KICK OFF", font_small, WHITE, WIDTH//2, 655, True)


def draw_match():
    draw_pitch_3d()

    # Painter's algorithm: far players first.
    entities = [(p.y, p) for p in blue+red]
    entities.sort(key=lambda q:q[0])
    for _, p in entities:
        billboard_player(p)
    draw_ball_3d()

    # Scoreboard.
    score_rect = pygame.Rect(WIDTH//2-220, 12, 440, 72)
    panel(score_rect, (8,18,28), WHITE, 12)
    draw_text(f"BLUE SHARKS   {score_blue}", font_small, BLUE_LIGHT,
              WIDTH//2-110, 48, True)
    draw_text(f"{score_red}   RED LIONS", font_small, RED_LIGHT,
              WIDTH//2+110, 48, True)

    draw_text("3D MATCH • 11 v 11", font_tiny, WHITE, WIDTH//2, 94, True)
    draw_text("WASD/ARROWS MOVE   SHIFT SPRINT   SPACE SHOOT   E PASS   Q SWITCH   ESC MENU",
              font_tiny, WHITE, WIDTH//2, HEIGHT-18, True)

    if message_timer > 0:
        draw_text(match_message, font_big, GOLD, WIDTH//2, 145, True)

# =========================================================
# MENU DRAWING
# =========================================================
def draw_menu_background():
    screen.fill((7,15,25))
    pygame.draw.rect(screen, (12,25,38), (0,190,WIDTH,300))
    for y in range(240,430,20):
        for x in range(10,WIDTH,25):
            c = [(70,80,90),(40,50,65),(100,105,110)][(x+y)%3]
            pygame.draw.circle(screen,c,(x,y),4)
    pygame.draw.rect(screen,(25,95,32),(0,490,WIDTH,230))

def draw_menu():
    draw_menu_background()
    draw_text("FOOTBALL",font_title,WHITE,55,55)
    draw_text("ULTIMATE",font_title,WHITE,55,120)
    draw_text("3D",font_title,GREEN_LIGHT,360,120)
    draw_text("BETA 0.4",font_small,GREEN_LIGHT,60,200)

    play_button.draw(); profile_button.draw(); team_button.draw(); settings_button.draw()
    shop_button.draw(); news_button.draw(); league_button.draw(); quit_button.draw()

    info=pygame.Rect(760,120,430,150)
    panel(info,DARK,GREEN)
    draw_text(username,font_big,WHITE,790,145)
    draw_text(f"LEVEL {level}",font_small,GREEN_LIGHT,790,205)
    draw_text(f"COINS: {coins}",font_small,GOLD,950,205)
    draw_text(f"GEMS: {gems}",font_small,CYAN,950,240)
    pygame.draw.rect(screen,(50,60,70),(790,240,130,8),border_radius=4)
    pygame.draw.rect(screen,GREEN,(790,240,int(130*xp/xp_max),8),border_radius=4)

def draw_play_page():
    screen.fill(DARK)
    draw_text("PLAY",font_title,WHITE,WIDTH//2,100,True)
    draw_text("CHOOSE GAME MODE",font_subtitle,GRAY,WIDTH//2,170,True)
    quick_match_button.draw(); tournament_button.draw(); back_button.draw()

def draw_settings_page():
    screen.fill(DARK)
    draw_text("SETTINGS",font_title,WHITE,WIDTH//2,100,True)
    music_button.text=f"MUSIC: {'ON' if music_on else 'OFF'}"
    sound_button.text=f"SOUND: {'ON' if sound_on else 'OFF'}"
    music_button.draw(); sound_button.draw(); fullscreen_button.draw(); back_button.draw()

def draw_team_page():
    screen.fill(DARK)
    draw_text("CHOOSE YOUR TEAM", font_title, WHITE, WIDTH//2, 80, True)
    draw_text("Click a club to control its players", font_small, GRAY, WIDTH//2, 135, True)

    cards = [("blue", HOME_TEAM_NAME, home_logo, BLUE_LIGHT, pygame.Rect(150,205,420,300)),
             ("red", AWAY_TEAM_NAME, away_logo, RED_LIGHT, pygame.Rect(710,205,420,300))]
    for team,name,logo,col,r in cards:
        selected = team == selected_team
        panel(r, (10,20,32), col if selected else GRAY, 24)
        screen.blit(pygame.transform.smoothscale(logo,(155,155)), (r.centerx-78,r.y+25))
        draw_text(name, font_subtitle, col, r.centerx, r.y+220, True)
        draw_text("SELECTED" if selected else "SELECT", font_small, GOLD if selected else WHITE, r.centerx, r.y+265, True)
    back_button.draw()

def draw_simple_page(title,text):
    screen.fill(DARK)
    draw_text(title,font_title,WHITE,WIDTH//2,100,True)
    r=pygame.Rect(300,230,680,250)
    panel(r,DARK2,GREEN)
    draw_text(text,font_subtitle,GRAY,WIDTH//2,330,True)
    draw_text("BETA 0.4 FEATURE",font_small,GREEN_LIGHT,WIDTH//2,390,True)
    back_button.draw()

# =========================================================
# EVENTS
# =========================================================
def handle_event(event):
    global current_page, music_on, sound_on, matches, selected_team, selected_player_number
    if current_page=="menu":
        if play_button.clicked(event): current_page="play"
        elif profile_button.clicked(event): current_page="profile"
        elif team_button.clicked(event): current_page="team"
        elif settings_button.clicked(event): current_page="settings"
        elif shop_button.clicked(event): current_page="shop"
        elif news_button.clicked(event): current_page="news"
        elif league_button.clicked(event): current_page="leagues"
        elif quit_button.clicked(event):
            pygame.quit(); sys.exit()
    elif current_page=="play":
        if quick_match_button.clicked(event):
            matches += 1
            setup_match()
            current_page="match"
        elif tournament_button.clicked(event):
            setup_match()
            current_page="match"
        elif back_button.clicked(event): current_page="menu"
    elif current_page=="team":
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pygame.Rect(150,205,420,300).collidepoint(event.pos):
                selected_team = "blue"
                selected_player_number = 10
                setup_match()
            elif pygame.Rect(710,205,420,300).collidepoint(event.pos):
                selected_team = "red"
                selected_player_number = 10
                setup_match()
        if back_button.clicked(event):
            current_page = "menu"
    elif current_page=="settings":
        if music_button.clicked(event):
            music_on=not music_on
        elif sound_button.clicked(event):
            sound_on=not sound_on
        elif fullscreen_button.clicked(event):
            pygame.display.toggle_fullscreen()
        elif back_button.clicked(event): current_page="menu"
    elif current_page!="match":
        if back_button.clicked(event): current_page="menu"

# =========================================================
# MAIN
# =========================================================
setup_match()
running=True
while running:
    dt=min(clock.tick(FPS)/1000.0,0.035)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                if current_page=="match": current_page="menu"
                elif current_page!="menu": current_page="menu"
                else: running=False
            elif current_page=="match":
                if event.key==pygame.K_SPACE:
                    shoot_user()
                elif event.key==pygame.K_e:
                    pass_user()
                elif event.key==pygame.K_q:
                    switch_player()
        handle_event(event)

    if current_page=="match":
        if match_intro_timer > 0:
            match_intro_timer = max(0.0, match_intro_timer - dt)
        else:
            update_match(dt)

    if current_page=="menu": draw_menu()
    elif current_page=="play": draw_play_page()
    elif current_page=="settings": draw_settings_page()
    elif current_page=="match":
        if match_intro_timer > 0:
            draw_match_intro()
        else:
            draw_match()
    elif current_page=="profile": draw_simple_page("PROFILE","Player profile")
    elif current_page=="team": draw_team_page()
    elif current_page=="shop": draw_simple_page("SHOP","Players and items")
    elif current_page=="news": draw_simple_page("NEWS","Football news")
    elif current_page=="leagues": draw_simple_page("LEAGUES","ChatGPT Leagues")

    pygame.display.flip()

pygame.quit()
sys.exit()
