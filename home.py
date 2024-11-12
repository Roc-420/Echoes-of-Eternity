# Example file showing a basic pygame "game loop"
import pygame
import time


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font('font/Pixeltype.ttf',155)
test_font_1 = pygame.font.Font('font/Pixeltype.ttf',139)

text_timer = 0

# home screen status variables
home_screen_text = 0 # stops generation if text = 0

start_state = 1
end_state = 0

def home_screen():
    def title_screen():
        if start_state == 1:
            start_color = "#6D51B9"
        if start_state == 0:
            start_color = '#382A5E'
        if end_state == 1:
            end_color = "#6D51B9"
        if end_state == 0:
            end_color = '#382A5E'
        image = pygame.image.load('scenes/title.png')
        start_text = test_font_1.render('Start Game',False,'Black')
        start_rect = start_text.get_rect(midbottom = (640,360))
        quit_text = test_font_1.render('Quit Game',False,'Black')
        quit_rect = quit_text.get_rect(midbottom = (640,550))
        screen.blit(image,(0,0))
        pygame.draw.rect(screen,start_color,start_rect)
        pygame.draw.rect(screen,start_color,start_rect,border_radius=200)
        screen.blit(start_text,start_rect)
        pygame.draw.rect(screen,end_color,quit_rect)
        pygame.draw.rect(screen,end_color,quit_rect,20000000)
        screen.blit(quit_text,quit_rect)

    def text_generator(texts,pos):
        global text_timer
        global home_screen_text
        sound_effect = pygame.mixer.Sound('music/text_type.wav')
        


        text = texts[: int(text_timer)  ]
        if text == texts:
            home_screen_text = 1
        text_surface = test_font.render(text,False,'Black')
        text_rect = text_surface.get_rect(midbottom = pos)
        screen.blit(text_surface,text_rect)
        text_timer += 0.4
        
        
        print(f" Text: {text}, Text timer: { text_timer}, screen text: {home_screen_text}   ")
        
        return text
    
    title_text = "Echoes of Eternity"
    title_screen()
    if home_screen_text == 0:
        text_generator(title_text,(640,110))
        
    else:
        text_surface = test_font.render(title_text,False,'Black')
        text_rect = text_surface.get_rect(midbottom = (640,110))
        screen.blit(text_surface,text_rect)
    
  
    

    
 #  pygame.display.toggle_fullscreen() can be used to fullscreen for demonstration
music = pygame.mixer.Sound('music/title.mp3')
music.play(-1)
while running:
   

    # generating text one word at a time
    home_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                scroll = pygame.mixer.Sound('music/move.mp3')
                scroll.play(0)  
            if event.key == pygame.K_UP:
                if end_state == 1:
                    end_state =0
                    start_state = 1
                else:
                    pass
            if event.key == pygame.K_DOWN:
                if start_state == 1:
                    start_state = 0
                    end_state = 1
                else:
                    pass
            
            if event.key == pygame.K_SPACE:
                select = pygame.mixer.Sound('music/select.mp3')
                select.play(0)
                if start_state == 1:
                    print("exiting!!")
                else:
                    pygame.quit()


    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()