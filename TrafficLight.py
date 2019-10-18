import pygame
import sys

size = wight, height = 120, 240
black = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class RedLight:
    def __init__(self):
        pass
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (60, 30), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 90), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 150), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 210), 30)


class YellowLight:
    def __init__(self):
        pass
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (60, 30), 30)
        pygame.draw.circle(screen, (255, 255, 0), (60, 90), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 150), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 210), 30)


class GreenLight:
    def __init__(self):
        pass
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (60, 30), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 90), 30)
        pygame.draw.circle(screen, (0, 255, 0), (60, 150), 30)
        pygame.draw.circle(screen, (255, 255, 255), (60, 210), 30)


class BlueLight:
    def __init__(self):
        pass
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), (60, 30), 30)
        pygame.draw.circle(screen, (0, 0, 255), (60, 90), 30)
        pygame.draw.circle(screen, (0, 0, 255), (60, 150), 30)
        pygame.draw.circle(screen, (0, 0, 255), (60, 210), 30)


class TrafficLight:
    def __init__(self):
        self.red_state = RedLight()
        self.yellow_state = YellowLight()
        self.green_state = GreenLight()
        self.blue_state = BlueLight()
        self.cycles = 1
        self.state = 'green'
        self.blue_count = 0

    def draw(self):
        if self.state == 'red':
            self.red_state.draw()
            pass
        elif  self.state == 'yellow':
            self.yellow_state.draw()
            pass
        elif self.state == 'green':
            self.green_state.draw()
            pass
        elif self.state == 'blue':
            self.blue_state.draw()
            pass

    def working(self):
        if self.state == 'green':
            self.state = 'yellow'
            self.blue_count = 0
            pass
        elif self.state == 'yellow':
            if self.cycles % 2 == 1:
                self.state = 'red'
                pass
            else:
                self.state = 'blue'
                self.blue_count += 1
                pass
            pass
        elif self.state == 'red':
            self.state = 'green'
            self.cycles += 1
            pass
        elif self.state == 'blue':
            if self.blue_count < 3:
                self.blue_count += 1
                pass
            elif self.blue_count == 3:
                self.state = 'green'
                self.cycles += 1
                pass
            pass



def main():
    TL = TrafficLight()
    pygame.init()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pass
        screen.fill(black)
        TL.draw()
        pygame.display.flip()
        pygame.time.wait(2000)
        TL.working()
   sys.exit()


if __name__ == "__main__":
    main()
