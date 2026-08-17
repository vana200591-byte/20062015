import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720
        self.fps = 60

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption("Football Game v0.4 Beta")

        self.clock = pygame.time.Clock()
        self.running = True

        # Player
        self.player_x = 500
        self.player_y = 360
        self.player_speed = 5

        # Ball
        self.ball_x = 640
        self.ball_y = 360
        self.ball_radius = 12

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Player movement
        if keys[pygame.K_w]:
            self.player_y -= self.player_speed

        if keys[pygame.K_s]:
            self.player_y += self.player_speed

        if keys[pygame.K_a]:
            self.player_x -= self.player_speed

        if keys[pygame.K_d]:
            self.player_x += self.player_speed

        # Giới hạn cầu thủ trong sân
        self.player_x = max(90, min(1190, self.player_x))
        self.player_y = max(70, min(650, self.player_y))

    def draw_field(self):
        # Sân
        self.screen.fill((35, 140, 60))

        field = pygame.Rect(80, 60, 1120, 600)

        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            field,
            5
        )

        # Đường giữa
        pygame.draw.line(
            self.screen,
            (255, 255, 255),
            (640, 60),
            (640, 660),
            5
        )

        # Vòng tròn giữa
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (640, 360),
            90,
            5
        )

        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (640, 360),
            6
        )

        # Vòng cấm trái
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(80, 210, 180, 300),
            5
        )

        # Vòng cấm phải
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(1020, 210, 180, 300),
            5
        )

        # Khung thành
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(45, 285, 35, 150),
            5
        )

        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(1200, 285, 35, 150),
            5
        )

    def draw_player(self):
        pygame.draw.circle(
            self.screen,
            (30, 80, 220),
            (int(self.player_x), int(self.player_y)),
            20
        )

    def draw_ball(self):
        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (int(self.ball_x), int(self.ball_y)),
            self.ball_radius
        )

        pygame.draw.circle(
            self.screen,
            (20, 20, 20),
            (int(self.ball_x), int(self.ball_y)),
            self.ball_radius,
            2
        )

    def render(self):
        self.draw_field()
        self.draw_player()
        self.draw_ball()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(self.fps)

        pygame.quit()