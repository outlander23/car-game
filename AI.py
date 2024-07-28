import pygame
class SimpleAI:
    def __init__(self, car_x, car_y, speed):
        self.car_x = car_x
        self.car_y = car_y
        self.speed = speed
        self.change_x = 0
    
    def update(self, obstacles, road_bounds):
        # Basic avoidance logic
        self.change_x = 0
        for obstacle in obstacles:
            if self.is_collision(obstacle):
                if self.car_x < obstacle[0]:
                    self.change_x = -2  # Move left
                else:
                    self.change_x = 2  # Move right
        
        # Stay within road bounds
        if self.car_x <= road_bounds[0]:
            self.change_x = 2
        elif self.car_x >= road_bounds[1]:
            self.change_x = -2
        
        # Update car position
        self.car_x += self.change_x
    
    def is_collision(self, obstacle):
        # Simple collision detection logic
        car_rect = pygame.Rect(self.car_x, self.car_y, 128, 128)
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[3])
        return car_rect.colliderect(obstacle_rect)
    
    def get_position(self):
        return self.car_x, self.car_y
