import pygame

class Control:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.next = pygame.image.load("templates/next.png")
        self.next = pygame.transform.scale(self.next, (50, 50))
        self.rectNext = self.next.get_rect()
        self.rectNext.x += 10
        self.rectNext.y += 100

        self.pause = pygame.image.load("templates/pause.png")
        self.pause = pygame.transform.scale(self.pause, (50, 50))
        self.rectPause = self.pause.get_rect()
        self.rectPause.x += 10
        self.rectPause.y += 200

        self.play = pygame.image.load("templates/play.png")
        self.play = pygame.transform.scale(self.play, (50, 50))
        self.rectPlay = self.play.get_rect()
        self.rectPlay.x += 10
        self.rectPlay.y += 300

        self.prev = pygame.image.load("templates/prev.png")
        self.prev = pygame.transform.scale(self.prev, (50, 50))
        self.rectPrev = self.prev.get_rect()
        self.rectPrev.x += 10
        self.rectPrev.y += 400

        self.stop = pygame.image.load("templates/stop.png")
        self.stop = pygame.transform.scale(self.stop, (50, 50))
        self.rectStop = self.stop.get_rect()
        self.rectStop.x += 10
        self.rectStop.y += 500


