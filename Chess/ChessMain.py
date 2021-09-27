"""Main File. Responsible for handing user inout and siplaying the GameState """

import pygame as p
from Chess import ChessEngine


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


"""Main driver for code. Will handle user input and updating graphics"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = ChessEngine.GameState()
    print(gs.board)
    loadImages()
    running = True
    sqSelected = () #no square selected
    playerClicks = [] #keep track of player clicks (2 tuples: [(6,4), (4,4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                   playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""Responsible for all graphics within game state"""

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

"""Draw the squares on the board"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""Draw the pieces on the board using GameState.board"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__ == "__main__":
    main()












