import pygame
import random
pygame.init()



try:
    with open("Traffic/high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0


# SCREEN 
WIDTH = 700
HEIGHT = 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()


# COLORS
GREY = (128, 128, 128)
WHITE = (255, 255, 255)


###########


# CAR 1 
RED_CAR_IMAGE = pygame.image.load('Traffic/car.png').convert_alpha()
RED_CAR = pygame.transform.scale(RED_CAR_IMAGE, (75, 75))
car_group = pygame.sprite.Group()



# Car 2 
RED_CAR_IMAGE_2 = pygame.image.load('Traffic/car2.png').convert_alpha()
RED_CAR_2 = pygame.transform.scale(RED_CAR_IMAGE_2, (75, 75))
car_group_2 = pygame.sprite.Group()


# Car 3
BLUE_CAR_IMAGE = pygame.image.load('Traffic/car3.png').convert_alpha()
BLUE_CAR = pygame.transform.scale(BLUE_CAR_IMAGE, (80, int(85 * BLUE_CAR_IMAGE.get_height() / BLUE_CAR_IMAGE.get_width())))
car_group_3 = pygame.sprite.Group()

# Car 4
BLUE_CAR_IMAGE_2 = pygame.image.load('Traffic/car4.png').convert_alpha()
BLUE_CAR_2 = pygame.transform.scale(BLUE_CAR_IMAGE_2, (80, int(85 * BLUE_CAR_IMAGE_2.get_height() / BLUE_CAR_IMAGE_2.get_width())))
car_group_4 = pygame.sprite.Group()


############



# ROAD 1  
ROAD = pygame.image.load('Traffic/road.png').convert_alpha()
ROAD_RECT = pygame.Rect((WIDTH - ROAD.get_width()) // 2, 0, 100, 100)





#LINES 
LINE_RECT_1 = pygame.Rect(285, 284 - 8 //2, 415 - 285, 8)
LINE_RECT_2 = pygame.Rect(286, HEIGHT - 284 -8 // 2, 415 - 285, 8)


LINE_RECT_3 = pygame.Rect(282 - 8 // 2, 285, 8, 135)
LINE_RECT_4 = pygame.Rect(419 - 8 // 2, 285, 8, 135)





# LIGHTS
RED_LIGHT = pygame.image.load('Traffic/red_light.png').convert_alpha()
GREEN_LIGHT = pygame.image.load('Traffic/green_light.png').convert_alpha()
toggle_t_rect = pygame.Rect(150, 200, GREEN_LIGHT.get_width(), GREEN_LIGHT.get_height())



RED_LIGHT_2 = RED_LIGHT
GREEN_LIGHT_2 = GREEN_LIGHT 
toggle_g_rect = pygame.Rect(450, 450, GREEN_LIGHT_2.get_width(), GREEN_LIGHT_2.get_height())


SIDE_LIGHT_RED = pygame.image.load('Traffic/red_light_side.png').convert_alpha()
SIDE_LIGHT_GREEN = pygame.image.load('Traffic/green_light_side.png').convert_alpha()
toggle_h_rect = pygame.Rect(200, 450, SIDE_LIGHT_GREEN.get_width(), SIDE_LIGHT_GREEN.get_height())


SIDE_LIGHT_RED_2 = pygame.image.load('Traffic/red_light_side.png').convert_alpha()
SIDE_LIGHT_GREEN_2 = pygame.image.load('Traffic/green_light_side.png').convert_alpha()
toggle_f_rect = pygame.Rect(450, 150, SIDE_LIGHT_GREEN.get_width(), SIDE_LIGHT_GREEN.get_height())




# FONTS
font = pygame.font.Font(None, 74)
score_font = pygame.font.Font(None, 56)




class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = RED_CAR
        self.rect = self.image.get_rect(midtop = (WIDTH // 2 - 35, -75))
        self.stopped = False




    def update(self, toggle_t):

        front_edge_rect = pygame.Rect(self.rect.x, self.rect.bottom - 1, self.rect.width, 2)

        if front_edge_rect.colliderect(LINE_RECT_1) and not toggle_t:
            self.stopped = True
        else: 
            self.stopped = False



        for other_car in car_group:
            if other_car == self:
                continue
            if self.rect.colliderect(other_car.rect):
                if self.rect.y < other_car.rect.y and (other_car.rect.y - self.rect.y) < 100:
                    self.stopped = True
                    break


        if not self.stopped:
            self.rect.y += 1


        if self.rect.y > HEIGHT:
            self.kill()


class CarUp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = RED_CAR_2
        self.rect = self.image.get_rect(midbottom=((WIDTH - 200) - 115, HEIGHT + 75))
        self.stopped = False



    def update(self, toggle_g):

        front_edge_rect = pygame.Rect(self.rect.x, self.rect.top + 1, self.rect.width, 2)



        if front_edge_rect.colliderect(LINE_RECT_2) and not toggle_g:
            self.stopped = True
        elif toggle_g:
            self.stopped = False




        for other_car in car_group_2:
            if other_car == self:
                continue
            if self.rect.colliderect(other_car.rect):
                if self.rect.y > other_car.rect.y and (self.rect.y + other_car.rect.y) > 100:
                    self.stopped = True
                    break



        if not self.stopped:
            self.rect.y -= 1

        if self.rect.y < - 75:
            self.kill()








class CarGoingRight(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = BLUE_CAR
        self.rect = self.image.get_rect(midleft = (-75, HEIGHT // 2 + 35))
        self.stopped = False



    def update(self, toggle_h):

        front_edge_rect = pygame.Rect(self.rect.right - 1, self.rect.y, 2, self.rect.height)

        if front_edge_rect.colliderect(LINE_RECT_3) and not toggle_h:
            self.stopped = True
        else: 
            self.stopped = False




        for other_car in car_group_3:
            if other_car == self:
                continue
            if self.rect.colliderect(other_car.rect):
                if self.rect.x < other_car.rect.x and (other_car.rect.x - self.rect.x) < 99:
                    self.stopped = True
                    break

        if not self.stopped:
            self.rect.x += 1


        if self.rect.x > WIDTH:
            self.kill()




class CarGoingLeft(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = BLUE_CAR_2
        self.rect = self.image.get_rect(midleft = (720, HEIGHT // 2 - 35))
        self.stopped = False



    def update(self, toggle_f):

        front_edge_rect = pygame.Rect(self.rect.left - 1, self.rect.y, 2, self.rect.height)

        if front_edge_rect.colliderect(LINE_RECT_4) and not toggle_f:
            self.stopped = True
        else: 
            self.stopped = False




        for other_car in car_group_4:
            if other_car == self:
                continue
            if self.rect.colliderect(other_car.rect):
                if self.rect.x > other_car.rect.x and (self.rect.x - other_car.rect.x) < 99:
                    self.stopped = True
                    break

        if not self.stopped:
            self.rect.x -= 1


        if self.rect.x < -80:
            self.kill()





def spawn_car():
    car = Car()
    car_group.add(car)


def spawn_car_up():
    car = CarUp()
    car_group_2.add(car)

def spawn_car_going_right():
    car = CarGoingRight()
    car_group_3.add(car)

def spawn_car_going_left():
    car = CarGoingLeft()
    car_group_4.add(car)




toggle_t = True
toggle_g = True
toggle_h = True
toggle_f = True





def draw_window(game_active, current_score, high_score):

    WIN.fill(GREY)

    pygame.display.set_caption('TRAFFIC')

    


    if game_active:
        WIN.blit(ROAD, (0, 0))
        score_text = score_font.render(f"Score: {current_score}", True, WHITE)
        WIN.blit(score_text, (10,10))


        if toggle_t:
            WIN.blit(GREEN_LIGHT, (150, 200))  # GREEN LIGHT
        else:
            WIN.blit(RED_LIGHT, (150, 200))  # RED LIGHT

        if toggle_g:

            WIN.blit(GREEN_LIGHT_2, (450, 450))  # GREEN LIGHT
        else:
            WIN.blit(RED_LIGHT_2, (450, 450))


        if toggle_h:
            WIN.blit(SIDE_LIGHT_GREEN, (200, 450))  # GREEN LIGHT
        else:
            WIN.blit(SIDE_LIGHT_RED, (200, 450))

        if toggle_f:
            WIN.blit(SIDE_LIGHT_GREEN, (450, 150))  # GREEN LIGHT
        else:
            WIN.blit(SIDE_LIGHT_RED, (450, 150))




        pygame.draw.rect(WIN, WHITE, LINE_RECT_1)
        pygame.draw.rect(WIN, WHITE, LINE_RECT_2)
        pygame.draw.rect(WIN, WHITE, LINE_RECT_3)
        pygame.draw.rect(WIN, WHITE, LINE_RECT_4)
        

        car_group.draw(WIN)
        car_group_2.draw(WIN)
        car_group_3.draw(WIN)
        car_group_4.draw(WIN)

    else:
        WIN.fill(GREY)
        game_over_text = font.render('GAME OVER', True, (255, 0, 0))
        final_score_text = score_font.render(f"Final Score: {current_score}", True, WHITE)


        if current_score > high_score:
            high_score_text = score_font.render(f"NEW HIGH SCORE: {current_score}", True, (255, 0, 0))
        else:
            high_score_text = score_font.render(f"High Score: {high_score}", True, WHITE)



        restart_text = font.render('Press SPACE to Restart', True, (255, 255, 255))


        WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
        WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
        WIN.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 50))
        WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 150))
    
    pygame.display.update()


def main():

    global toggle_t, toggle_g, toggle_h, toggle_f, start_time, high_score
    run = True
    game_active = True

    start_time = pygame.time.get_ticks()

    


    CAR_SPAWN_TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(CAR_SPAWN_TIMER, random.randint(1000, 6000))

    CAR_SPAWN_TIMER_2 = pygame.USEREVENT + 2
    pygame.time.set_timer(CAR_SPAWN_TIMER_2, random.randint(1000, 6000))

    CAR_SPAWN_TIMER_3 = pygame.USEREVENT + 3
    pygame.time.set_timer(CAR_SPAWN_TIMER_3, random.randint(1000, 6000))

    CAR_SPAWN_TIMER_4 = pygame.USEREVENT + 4
    pygame.time.set_timer(CAR_SPAWN_TIMER_4, random.randint(1000, 6000))



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            if game_active:
                if event.type == CAR_SPAWN_TIMER:
                    spawn_car()
                    pygame.time.set_timer(CAR_SPAWN_TIMER, random.randint(4000, 8000))

                if event.type == CAR_SPAWN_TIMER_2:
                    spawn_car_up()
                    pygame.time.set_timer(CAR_SPAWN_TIMER_2, random.randint(4000, 8000))

                if event.type == CAR_SPAWN_TIMER_3:
                    spawn_car_going_right()
                    pygame.time.set_timer(CAR_SPAWN_TIMER_3, random.randint(4000, 8000))

                if event.type == CAR_SPAWN_TIMER_4:
                    spawn_car_going_left()
                    pygame.time.set_timer(CAR_SPAWN_TIMER_4, random.randint(2400, 8000))
                

                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if toggle_t_rect.collidepoint(event.pos):
                            toggle_t = not toggle_t
                        if toggle_g_rect.collidepoint(event.pos):
                            toggle_g = not toggle_g
                        if toggle_h_rect.collidepoint(event.pos):
                            toggle_h = not toggle_h
                        if toggle_f_rect.collidepoint(event.pos):
                            toggle_f = not toggle_f

                    

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()
                    car_group.empty()
                    car_group_2.empty()
                    car_group_3.empty()
                    car_group_4.empty()
                    toggle_t = True
                    toggle_g = True
                    toggle_h = True
                    toggle_f = True


                    pygame.time.set_timer(CAR_SPAWN_TIMER, random.randint(4000, 8000))
                    pygame.time.set_timer(CAR_SPAWN_TIMER_2, random.randint(4000, 8000))
                    pygame.time.set_timer(CAR_SPAWN_TIMER_3, random.randint(4000, 8000))
                    pygame.time.set_timer(CAR_SPAWN_TIMER_4, random.randint(4000, 8000))
                

        if game_active:
            elapsed_time = pygame.time.get_ticks() - start_time
            current_score = elapsed_time // 1000
        else:
            if current_score > high_score:
                high_score = current_score
                with open("Traffic/high_score.txt", "w") as file:
                    file.write(str(high_score))


        if game_active: 
            for car in car_group:
                car.update(toggle_t)
            
            for car in car_group_2:
                car.update(toggle_g)

            for car in car_group_3:
                car.update(toggle_h)
            
            for car in car_group_4:
                car.update(toggle_f)

            
            


            for car in car_group:
                if car.stopped and car.rect.top < 0 and toggle_t == False:
                    game_active = False
                    break

            for car in car_group_2:
                if car.stopped and car.rect.bottom > HEIGHT and toggle_g == False:
                    game_active = False
                    break
            
            for car in car_group_3:
                if car.stopped and car.rect.left < 0 and toggle_h == False:
                    game_active = False
                    break
            
            for car in car_group_4:
                if car.stopped and car.rect.right > WIDTH and toggle_f == False:
                    game_active = False
                    break





            for car_right in car_group_3:
                for car_down in car_group:
                    if car_right.rect.colliderect(car_down.rect):
                        game_active = False
                        break
                
                for car_up in car_group_2:
                    if car_right.rect.colliderect(car_up.rect):
                        game_active = False
                        break

                if not game_active:
                    break

            for car_left in car_group_4:
                for car_down in car_group:
                    if car_left.rect.colliderect(car_down.rect):
                        game_active = False
                        break 
                
                for car_up in car_group_2:
                    if car_left.rect.colliderect(car_up.rect):
                        game_active = False
                
                if not game_active:
                    break
                



            draw_window(game_active, current_score, high_score)

    pygame.quit()



if __name__ == '__main__':
    main()