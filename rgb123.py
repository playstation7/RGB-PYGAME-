import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
pygame.display.set_caption('RGB')
pygame.mouse.set_visible(0)   #Disable cursor

def check_events(time_sleep):
    print(time_sleep)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                time_sleep -= 0.01
            elif event.key == pygame.K_LEFT:
                time_sleep += 0.01
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        
    
    if time_sleep < 0:
            time_sleep = 0.001
    if time_sleep > 5:
            time_sleep = 5
        
                
    return time_sleep        
    
def color():
    bg_color = [0, 0, 255]
    time_sleep = 0.25
    time_move_right = False
    time_move_left = False
    while True:
        while bg_color[0] != 255:
            bg_color[0] += 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)
            

        while bg_color[2] != 0:
            bg_color[2] -= 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)

        while bg_color[1] != 255:
            bg_color[1] += 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)
        
        while bg_color[0] != 0:
            bg_color[0] -= 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)

        while bg_color[2] != 255:
            bg_color[2] += 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)

        while bg_color[1] != 0:
            bg_color[1] -= 1
            screen.fill(bg_color)
            pygame.display.flip()
            time_sleep = check_events(time_sleep) 
            time.sleep(time_sleep)

color()    
    

   
 

        
 


            
                
               
            

        
    
        
            
            
        
        
