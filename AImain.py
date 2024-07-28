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

def start_button():
    return pygame.draw.rect(screen, (120, 120, 123), (150, 90, 100, 50), border_radius=20)

def continue_button():
    return pygame.draw.rect(screen, (0, 244, 0), (150, 160, 100, 50))

def quit_button():
    return pygame.draw.rect(screen, (244, 0, 0), (150, 230, 100, 50))

def startGame():
    global gameStart
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

class SimpleAI:
    def __init__(self, car_x, car_y, speed):
        self.car_x = car_x
        self.car_y = car_y
        self.speed = speed
        self.change_x = 0
    
    def update(self, obstacles, road_bounds):
        self.change_x = 0
        for obstacle in obstacles:
            if self.is_collision(obstacle):
                if self.car_x < obstacle[0]:
                    self.change_x = -2  # Move left
                else:
                    self.change_x = 2  # Move right
        
        if self.car_x <= road_bounds[0]:
            self.change_x = 2
        elif self.car_x >= road_bounds[1]:
            self.change_x = -2
        
        self.car_x += self.change_x
    
    def is_collision(self, obstacle):
        car_rect = pygame.Rect(self.car_x, self.car_y, 128, 128)
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[3])
        return car_rect.colliderect(obstacle_rect)
    
    def get_position(self):
        return self.car_x, self.car_y

def doOverlap(l1, r1, l2, r2):
    if l1.x > r2.x or l2.x > r1.x:
        return False
    if l1.y > r2.y or l2.y > r1.y:
        return False
    return True

def isOutOfRoad(roadX1, roadX2, posCarX):
    return roadX1 <= posCarX and roadX2 >= posCarX

running = True
gameStart = True

ai_car = SimpleAI(posOfHeroCarX, posOfHeroCarY, speedOfHeroCar)
start = 1

while running:
    screen.fill(color)
    clock.tick(fps)
    
    ai_car.update([(260, villianOneY, 128, 128), (415, villianTwoY, 128, 128)], (210, 510))
    ai_car_x, ai_car_y = ai_car.get_position()

    showImg(roadImg, 150, roadY)
    showImg(heroCar, ai_car_x, ai_car_y)
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

    if not gameStart:
        continue

    imgRightY += speedOfHeroCar
    imgLeftY += speedOfHeroCar
    roadY += speedOfHeroCar
    villianOneY += villianSpeed
    villianTwoY += villianSpeed
    posOfHeroCarX += heroCarChangeX

    l1 = Point(280, villianOneY-10)
    r1 = Point(270+64+32, villianOneY+118)

    l2 = Point(430, villianTwoY-5)
    r2 = Point(415+64+32, villianTwoY+128)

    carLeftCorner = Point(ai_car_x+20, ai_car_y)
    carRightCorner = Point(ai_car_x+128-35, ai_car_y+130)

    showImg(pointImg, *l1.pos())
    showImg(pointImg2, *r1.pos())
    showImg(pointImg, *l2.pos())
    showImg(pointImg2, *r2.pos())
    showImg(pointImg, *carLeftCorner.pos())
    showImg(pointImg2, *carRightCorner.pos())

    if doOverlap(l1, r1, carLeftCorner, carRightCorner):
        start += 1
        print(l1.x, l1.y, r1.x, r1.y, carLeftCorner.x, carLeftCorner.y, carRightCorner.x, carRightCorner.y)
        print("Crushed", start)

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
