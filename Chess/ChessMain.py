"""Main File. Responsible for handing user inout and siplaying the GameState """

import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations
IMAGES = {}
"""Initialize a global dictionary of images. This will be called once in main"""

def loadImages():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wp", "bR", "bN", "bB", "bQ", "bK", "bp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp]'


"""Main driver for code. Will handle user imput and updating graphics"""

def main():
    p.init()
    screen = p.display.set_mode(WIDTH, HEIGHT)
    clock = p.time.Clock()
    screen.fill(p.color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        clock.tick(MAX_FPS)
        p.display.flip()










