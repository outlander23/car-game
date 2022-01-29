import random
import pygame

pygame.init()

width = 800
height = 800
screenSize = (width, height)
fps = 120

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
color = (0, 250, 0)


heroCar = pygame.image.load("assets/hero/car.png")
heroCar = pygame.transform.scale(heroCar, (128, 128))
heroCar = pygame.transform.flip(heroCar, False, True)
roadImg = pygame.image.load("assets/road.png")
roadImg = pygame.transform.scale(roadImg, (512, 2048))


badCar = pygame.image.load("assets/villains/car (1).png")
badCar2 = pygame.image.load("assets/villains/car (2).png")
badCar3 = pygame.image.load("assets/villains/car (3).png")
badCar = pygame.transform.flip(badCar, False, True)
badCar2 = pygame.transform.flip(badCar2, False, True)
badCar3 = pygame.transform.flip(badCar3, False, True)
pointImg = pygame.image.load("assets/basketball.png")
pointImg = pygame.transform.scale(pointImg, (5, 5))
pointImg2 = pygame.transform.scale(pointImg, (10, 10))
# assets

tree1 = pygame.image.load("assets/trees/tree (1).png")
tree1 = pygame.transform.scale(tree1, (128, 128))
tree2 = pygame.image.load("assets/trees/tree (2).png")
tree2 = pygame.transform.scale(tree2, (128, 128))
tree3 = pygame.image.load("assets/trees/tree (3).png")
tree3 = pygame.transform.scale(tree3, (128, 128))
house1 = pygame.image.load("assets/houses/house.png")
house1 = pygame.transform.scale(house1, (128, 128))

lstOfAssets = [tree1, tree2, tree3, house1]

posOfHeroCarX = 350
posOfHeroCarY = 400
speedOfHeroCar = 1
imgLeft = random.choice(lstOfAssets)
imgRight = random.choice(lstOfAssets)
imgLeftY = 0
imgRightY = 256
roadY = -512
heroCarChangeX = 0

lstBadCars = [badCar, badCar2, badCar3]
villianOne = random.choice(lstBadCars)
villianTwo = random.choice(lstBadCars)
lstOfPosOfBadCarsY = [-128, -512]
villianTwoY = -128
villianOneY = -512
villianSpeed = 1

# Buttons


def start_button(): return pygame.draw.rect(
    screen, (120, 120, 123), (150, 90, 100, 50), border_radius=20)


def continue_button(): return pygame.draw.rect(
    screen, (0, 244, 0), (150, 160, 100, 50))


def quit_button(): return pygame.draw.rect(
    screen, (244, 0, 0), (150, 230, 100, 50))


def startGame():
    gameStart = True


def showImg(img, x, y):
    screen.blit(img, (x, y))


def isOutOfScreenY(screenY, imgY):

    return screenY < imgY


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return [self.x, self.y]


class Rect:
    def __init__(self, poin1, poin2):
        self.X1 = poin1[0]
        self.X2 = poin2[0]
        self.Y1 = poin1[1]
        self.Y2 = poin2[1]


# def doOverlap(RectA, RectB):

#     return RectA.X1 < RectB.X2 and RectA.X2 > RectB.X1 and RectA.Y1 > RectB.Y2 and RectA.Y2 < RectB.Y1

def doOverlap(l1, r1, heroLeft, heroRight):
    if heroLeft.y-128 <= l1.y and heroLeft.y+130>=l1.y:
            return True
        return False




def isOutOfRoad(roadX1, roadX2, posCarX):
    return roadX1 <= posCarX and roadX2 >= posCarX


running = True
gameStart = True    

while running:
    screen.fill(color)
    clock.tick(fps)
    showImg(roadImg, 150, roadY)
    showImg(heroCar, posOfHeroCarX, posOfHeroCarY)
    showImg(pointImg, 200, 12)
    showImg(pointImg, 100+512, 12)
    showImg(imgLeft, 50, imgLeftY)
    showImg(imgRight, 620, imgRightY)
    showImg(villianOne, 260, villianOneY)

    showImg(villianTwo, 415, villianTwoY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                    running = False

            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                    startGame()
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                heroCarChangeX = -2
            elif pressed[pygame.K_RIGHT]:
                heroCarChangeX = 2
            elif pressed[pygame.K_SPACE]:
                gameStart = not gameStart 
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                heroCarChangeX = 0
            elif event.key == pygame.K_RIGHT:
                heroCarChangeX = 0
            # elif event.key == pygame.K_SPACE:
            #     gameStart = True                                        
              

    # All calculation will be here
    if not gameStart:
        continue
    imgRightY += speedOfHeroCar
    imgLeftY += speedOfHeroCar
    roadY += speedOfHeroCar
    villianOneY += villianSpeed
    villianTwoY += villianSpeed
    posOfHeroCarX += heroCarChangeX

    l1 = Point(260, villianOneY)
    r1 = Point(260+128, villianOneY+128)

    l2 = Point(415, villianTwoY)
    r2 = Point(415+128, villianTwoY+128)

    carLeftCorner = Point(posOfHeroCarX+20, posOfHeroCarY)

    carRightCorner = Point(posOfHeroCarX+128-35, posOfHeroCarY+130)

    showImg(pointImg, *l1.pos())
    showImg(pointImg2, *r1.pos())
    showImg(pointImg, *carLeftCorner.pos())
    showImg(pointImg2, *carRightCorner.pos())

    # showImg(pointImg, *l2.pos())
    # showImg(pointImg2, *r2.pos())
    # print(*l1.pos(),*r1.pos())
    if (doOverlap(l1, r1, carLeftCorner, carRightCorner)):
        print("Crushed")
    if (doOverlap(l2, r, carLeftCorner, carRightCorner)):
        print("Crushed")

    if isOutOfScreenY(height, imgLeftY):
        imgLeftY = -128
        imgLeft = random.choice(lstOfAssets)

    if isOutOfScreenY(height, imgRightY):
        imgRightY = -128
        imgRight = random.choice(lstOfAssets)

    if isOutOfScreenY(-512, roadY):
        roadY = -985
    if isOutOfScreenY(height, villianOneY):
        villianOneY = -128
        villianOne = random.choice(lstBadCars)
    if isOutOfScreenY(height, villianTwoY):
        villianTwoY = -512
        villianTwo = random.choice(lstBadCars)

    if posOfHeroCarX >= 100+370:
        heroCarChangeX = 0
    if posOfHeroCarX <= 210:
        heroCarChangeX = 0
    pygame.display.flip()
