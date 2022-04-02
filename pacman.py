import pygame

pygame.init();

screen = pygame.display.set_mode((800, 600), 0);
font = pygame.font.SysFont("arial", 20, True, False);

YELLOW = (255, 255, 0);
BLACK = (0, 0, 0);
BLUE = (0, 0, 255);
SPEED = 1;

class Scenario:
    def __init__(self, size, pac):
        self.pacman = pac;
        self.points = 0;
        self.size = size;
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ];

    def paintPoints(self, screen):
        points_x = self.size * 30;
        points_img = font.render("Score {}".format(self.points), True, YELLOW);
        screen.blit(points_img, (points_x, 50));

    def paintLine(self, screen, number_line, line):
        for number_column, column in enumerate(line):
            x = number_column * self.size;
            y = number_line * self.size;
            half = self.size // 2;
            color = BLACK;
            if column == 2:
                color = BLUE;
            pygame.draw.rect(screen, color, (x, y, self.size, self.size), 0)
            if column == 1:
                pygame.draw.circle(screen, YELLOW, (x + half, y + half), self.size // 10, 0);

    def paint(self, screen):
        for number_line, line in enumerate(self.matriz):
            self.paintLine(screen, number_line, line);

        self.paintPoints(screen);

    def calcRules(self):
        col = self.pacman.intention_column;
        lin = self.pacman.intention_line;
        if 0 <= col < 28 and 0 <= lin < 29:
            if self.matriz[lin][col] != 2:
                self.pacman.yes_movement();
                if self.matriz[lin][col] == 1:
                    self.points += 1;
                    self.matriz[lin][col] = 0;
                    print(self.points);



class Pacman:
    def __init__(self, size):
        self.column = 1;
        self.line = 1;
        self.axis_x = 400;
        self.axis_y = 300;
        self.size = size;
        self.speed_x = 0;
        self.speed_y = 0;
        self.radius = self.size // 2;
        self.intention_column = self.column;
        self.intention_line = self.line;

    def calcRules(self):
        self.intention_column = self.column + self.speed_x;
        self.intention_line = self.line + self.speed_y;
        self.axis_x = int(self.column * self.size + self.radius);
        self.axis_y = int(self.line * self.size + self.radius);

    def paint(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.axis_x, self.axis_y), self.radius, 0);

        mouth = (self.axis_x, self.axis_y);
        higher = (self.axis_x + self.radius, self.axis_y - self.radius);
        bottom = (self.axis_x + self.radius, self.axis_y);
        points = [mouth, higher, bottom];
        pygame.draw.polygon(screen, BLACK, points, 0);

        eye_x = int(self.axis_x + self.radius / 3);
        eye_y = int(self.axis_y - self.radius * 0.70);
        eye_radius = int(self.radius / 10);
        pygame.draw.circle(screen, BLACK, (eye_x, eye_y), eye_radius, 0);

    def events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.speed_x = SPEED;
                elif e.key == pygame.K_LEFT:
                    self.speed_x = -SPEED;
                elif e.key == pygame.K_UP:
                    self.speed_y = -SPEED;
                elif e.key == pygame.K_DOWN:
                    self.speed_y = SPEED;
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.speed_x = 0;
                elif e.key == pygame.K_LEFT:
                    self.speed_x = 0;
                elif e.key == pygame.K_UP:
                    self.speed_y = 0;
                elif e.key == pygame.K_DOWN:
                    self.speed_y = 0;

    def yes_movement(self):
        self.line = self.intention_line;
        self.column = self.intention_column;


if __name__ == "__main__":
    size = 600 // 30;
    pacman = Pacman(size);
    Scenario = Scenario(size, pacman);

    while True:
        pacman.calcRules();
        Scenario.calcRules();

        screen.fill(BLACK);
        Scenario.paint(screen);
        pacman.paint(screen);
        pygame.display.update();
        pygame.time.delay(100);

        events = pygame.event.get();
        for e in events:
            if e.type == pygame.QUIT:
                exit();
        pacman.events(events)