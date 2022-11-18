import pygame
from sys import exit
from random import randint
import functions as f

pygame.init()
WIDTH = 224*3
HEIGHT = 256*3
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()
ativo = False
fonte = pygame.font.Font("fonts/Retro Gaming.ttf",25)
start_time = 90
vidas = 10
end_game = False
dead=False

#tela de inicio
title_surf = pygame.image.load("graphics/title.png").convert_alpha()
title_rect = title_surf.get_rect(center = (WIDTH//2,150))

#score
score = 0
hi_score = 0

    #textos
#titlescreen
point_table = "TABELA DE PTS"
instrucaop1 = "10 PTS PARA CADA PASSO"
instrucaop2 = "50 PTS PARA CADA SAPO SALVO"
instrucaop3 = "PLUS BONUS:"
instrucaop4 = "10 PTS x TEMPO RESTANTE"
press2p = "APERTE ESPAÇO PARA JOGAR"
text_counter = 0

    #bg things
#background
bg_surf = pygame.image.load("graphics/bg.png").convert_alpha()
bg_rect = bg_surf.get_rect(topleft = (0,0))

#bordas
rect_direita = pygame.Rect((WIDTH-1,0),(30,HEIGHT))
rect_esquerda = pygame.Rect((-29,0),(30,HEIGHT))
rect_cima = pygame.Rect((0,0),(WIDTH,93))
rect_fim_1 = pygame.Rect((0,93),(18,45))
rect_fim_2 = pygame.Rect((78,93),(84,45))
rect_fim_3 = pygame.Rect((222,93),(84,45))
rect_fim_4 = pygame.Rect((366,93),(84,45))
rect_fim_5 = pygame.Rect((510,93),(84,45))
rect_fim_6 = pygame.Rect((WIDTH-21,93),(18,45))
y_max = 102
#rio
rio_rect = pygame.Rect((0,148),(672,217))
move_auth = True
rmove_auth = True
lmove_auth = True

#  audios
jump_sound = pygame.mixer.Sound("audios/moving.wav")
time_ending = pygame.mixer.Sound("audios/time_ending.wav")
water_death = pygame.mixer.Sound("audios/water.wav")
car_death = pygame.mixer.Sound("audios/car.wav")

#  sapo
#surfaces
sapo_stand = pygame.image.load("graphics/sapo/sapo_stand.png").convert_alpha()
sapo_jump1 = pygame.image.load("graphics/sapo/sapo_jump1.png").convert_alpha()
sapo_jump2 = pygame.image.load("graphics/sapo/sapo_jump2.png").convert_alpha()
sapo_l_1 = pygame.image.load("graphics/sapo/sapo_side_stand.png").convert_alpha()
sapo_l_2 = pygame.image.load("graphics/sapo/sapo_side_jump1.png").convert_alpha()
sapo_l_3 = pygame.image.load("graphics/sapo/sapo_side_jump2.png").convert_alpha()
sapo_r_1 = pygame.transform.flip(sapo_l_1,True,False)
sapo_r_2 = pygame.transform.flip(sapo_l_2,True,False)
sapo_r_3 = pygame.transform.flip(sapo_l_3,True,False)

#death
death_1 = pygame.image.load("graphics/sapo/death/death_1.png").convert_alpha()
death_2 = pygame.image.load("graphics/sapo/death/death_2.png").convert_alpha()
death_3 = pygame.image.load("graphics/sapo/death/death_3.png").convert_alpha()
death_4 = pygame.image.load("graphics/sapo/death/death_4.png").convert_alpha()


#framelists
sapo_fw = [sapo_stand,sapo_jump1,sapo_jump2]
sapo_left = [sapo_l_1,sapo_l_2,sapo_l_3]
sapo_right = [sapo_r_1,sapo_r_2,sapo_r_3]
sapo_index = 0
sapo_surf = sapo_fw[sapo_index]
sapo_rect = sapo_surf.get_rect(center = (336,699))
sapo_pos = (sapo_rect.x+18,sapo_rect.y)
fw = False
left = False
right = False

#death-related stuff
death_frame_list = [death_1,death_2,death_3,death_4]
death_index = 0
death_surf = death_frame_list[death_index]
death_rect = death_surf.get_rect(center = sapo_pos)

# cobra
snake_frame_1 = pygame.image.load("graphics/snake/snake_stand.png").convert_alpha()
snake_frame_2 = pygame.image.load("graphics/snake/snake_move1.png").convert_alpha()
snake_frame_3 = pygame.image.load("graphics/snake/snake_move2.png").convert_alpha()
snake_frames = [snake_frame_1,snake_frame_2,snake_frame_3]
snake_frame_index = 0
snake_surf = snake_frames[snake_frame_index]
snake_rect = snake_surf.get_rect(center = (-800,405))

# carros
car1_surf = pygame.image.load("graphics/carros/car1.png").convert_alpha()
car1_surf = pygame.transform.rotate(car1_surf,180)

car2_surf = pygame.image.load("graphics/carros/car2.png").convert_alpha()

car3_surf = pygame.image.load("graphics/carros/car3.png").convert_alpha()

smallcar_surf = pygame.image.load("graphics/carros/smallcar.png").convert_alpha()

truck_surf = pygame.image.load("graphics/carros/truck.png").convert_alpha()

# plataformas
wood_surf = pygame.image.load("graphics/river/wood/wood.png").convert_alpha()
wood_m_surf = pygame.image.load("graphics/river/wood/wood_m.png").convert_alpha()
wood_l_surf = pygame.image.load("graphics/river/wood/wood_l.png").convert_alpha()

turtle_frame_1 = pygame.image.load("graphics/river/turtle/turtle_1.png").convert_alpha()
turtle_frame_2 = pygame.image.load("graphics/river/turtle/turtle_2.png").convert_alpha()
turtle_frame_3 = pygame.image.load("graphics/river/turtle/turtle_3.png").convert_alpha()
turtle_frames = [turtle_frame_1,turtle_frame_2,turtle_frame_3]
turtle_frame_index = 0
turtle_surf = turtle_frames[turtle_frame_index]


wood_cll = False
turtle_cll = False

# objetivo
obj_frame_1 = pygame.image.load("graphics/obj/obj_1.png").convert_alpha()
obj_frame_2 = pygame.image.load("graphics/obj/obj_2.png").convert_alpha()
obj_frames = [obj_frame_1,obj_frame_2]
obj_frame_index = 0
obj_surf = obj_frames[obj_frame_index]
obj_rect_1 = pygame.Rect((24,93),(48,48))
obj_rect_2 = pygame.Rect((168,93),(48,48))
obj_rect_3 = pygame.Rect((312,93),(48,48))
obj_rect_4 = pygame.Rect((456,93),(48,48))
obj_rect_5 = pygame.Rect((600,93),(48,48))
#(-100,-100)
empty_rect_1 = pygame.Rect((-100,-100),(48,48))#(24,93)
empty_rect_2 = pygame.Rect((-100,-100),(48,48))#(168,93)
empty_rect_3 = pygame.Rect((-100,-100),(48,48))#(312,93)
empty_rect_4 = pygame.Rect((-100,-100),(48,48))#(456,93)
empty_rect_5 = pygame.Rect((-100,-100),(48,48))#(600,93)
empty_rect_list = [pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48))]


empty_pos = (0,0)

# endgame
end_game_rect = pygame.Rect((0,0),(WIDTH,HEIGHT))


# rects dos obstaculos e das plataformas
obs_rect_rlist = []
faster_obs_list = []
turtle_list = []
obs_rect_llist = []
wood_list = []

# rect dos objetivos
obj_list = [obj_rect_1,obj_rect_2,obj_rect_3,obj_rect_4,obj_rect_5]

# timers
ms=1000
seconds = pygame.USEREVENT
pygame.time.set_timer(seconds,ms)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)
large_wood_timer = pygame.USEREVENT + 7
pygame.time.set_timer(large_wood_timer,1500)
turtle_timer = pygame.USEREVENT + 2
pygame.time.set_timer(turtle_timer,3000)
snake_anim_timer = pygame.USEREVENT + 3
pygame.time.set_timer(snake_anim_timer,250)
turtle_anim_timer = pygame.USEREVENT + 4
pygame.time.set_timer(turtle_anim_timer,350)
text_timer = pygame.USEREVENT + 5
pygame.time.set_timer(text_timer,1000)
sapo_anim_timer = pygame.USEREVENT + 6
pygame.time.set_timer(sapo_anim_timer,60)

# main loop
while True:
    # atualiza os txts assim que inicia
    hi_score = f.get_high_score()
    store_time = f.get_cur_time()
    final_score = f.get_cur_score()

    # event loop
    for event in pygame.event.get():
        #quitar do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ativo:
            #movimento
            if event.type == pygame.KEYDOWN:            
                if event.key in [pygame.K_UP,pygame.K_w] and move_auth:
                    fw=True
                    jump_sound.play()
                    sapo_rect.y-=48
                    score+=10
                    
                    #and (618>=sapo_rect.x>18)
                elif event.key in [pygame.K_LEFT,pygame.K_a] and lmove_auth:
                    left=True
                    jump_sound.play()
                    sapo_rect.x-=50
                    score+=10
                    
                    #and (618>sapo_rect.x>=18) 
                elif event.key in [pygame.K_RIGHT,pygame.K_d] and rmove_auth:
                    right=True
                    jump_sound.play()
                    sapo_rect.x+=50
                    score+=10
                    
            
            if event.type == seconds:
                start_time-=1
                if start_time==20:
                    time_ending.play()
            
            if event.type == obstacle_timer:
                #vindo da direita
                obs_rect_rlist.append(car1_surf.get_rect(center = (randint(700,850),648)))
                faster_obs_list.append(smallcar_surf.get_rect(center = (randint(700,850),545)))
                faster_obs_list.append((truck_surf.get_rect(center = (randint(700,950),449))))
                #vindo da esquerda
                obs_rect_llist.append(car2_surf.get_rect(center = (-(randint(30,180)),596)))
                obs_rect_llist.append(car3_surf.get_rect(center = (-(randint(30,180)),503)))
                wood_list.append(wood_surf.get_rect(midleft = (-130,356)))
                wood_list.append(wood_m_surf.get_rect(midleft = (-180,260)))
                #reaproveitando o timer para usar no objetivo
                obj_frame_index+=1
                if obj_frame_index>1:
                    obj_frame_index=0
                obj_surf = obj_frames[obj_frame_index]

            if event.type == large_wood_timer:
                wood_list.append(wood_l_surf.get_rect(midleft = (-285,165)))
                

            if event.type == turtle_timer:
                turtle_list.append(turtle_surf.get_rect(center = (850,308)))
                turtle_list.append(turtle_surf.get_rect(center = (1025,215)))

            if event.type == snake_anim_timer:
                snake_frame_index+=1
                if snake_frame_index>2:
                    snake_frame_index=0
                snake_surf = snake_frames[snake_frame_index]

            if event.type == turtle_anim_timer:
                turtle_frame_index+=1
                if turtle_frame_index>2:
                    turtle_frame_index=0
                turtle_surf = turtle_frames[turtle_frame_index]
            
            if event.type == sapo_anim_timer:
                if fw:
                    sapo_index +=1
                    if sapo_index>2:
                        sapo_index=0
                        fw=False
                    sapo_surf = sapo_fw[sapo_index]
                elif left:
                    sapo_index +=1
                    if sapo_index>2:
                        sapo_index=0
                        left=False
                    sapo_surf = sapo_left[sapo_index]
                elif right:
                    sapo_index +=1
                    if sapo_index>2:
                        sapo_index=0
                        right=False
                    sapo_surf = sapo_right[sapo_index]
                if dead:
                    
                    death_index+=1
                    if death_index>3:
                        death_index=0
                        dead=False
                    death_surf = death_frame_list[death_index]
                    

        else:
            if event.type == text_timer:
                
                if text_counter==0:
                    press2p = "APERTE ESPAÇO PARA JOGAR"
                    text_counter=1
                else:
                    press2p = ""
                    text_counter=0
                    
                    
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    ativo=True
                    end_game=False
                    start_time=90              
                    
    if ativo:
            #desenhando na tela
        #movimento da cobra
        snake_rect.x+=5
        if snake_rect.x>=700:
            snake_rect.x=-800
        
        #background
        tela.blit(bg_surf,bg_rect)
        
        #score
        cur_score = score
        f.text("SCORE",100,35,"#ffffff",fonte,tela)
        f.text(f"{cur_score:05}",100,65,"#ffffff",fonte,tela)
        if cur_score>hi_score:
            f.save_high_score(cur_score)
              
        #obstaculos que vem da direita
        obs_rect_rlist = f.obstacle_rmove(obs_rect_rlist,tela,car1_surf)
        faster_obs_list = f.faster_obs_rmove(faster_obs_list,tela,smallcar_surf,truck_surf) 
        turtle_list = f.turtle_move(turtle_list,tela,turtle_surf)       
        #obstaculos que vem da esquerda
        obs_rect_llist = f.obstacle_lmove(obs_rect_llist,tela,car2_surf,car3_surf)
        wood_list = f.wood_move(wood_list,tela,wood_surf,wood_m_surf,wood_l_surf)

        #desenhando cobra e sapo por cima de tudo
        tela.blit(snake_surf,snake_rect)
        tela.blit(sapo_surf,sapo_rect)
        if dead:
            tela.blit(death_surf,death_rect)  
        #cronometro
        f.text("TEMPO:",510,760,"#ffff00",fonte,tela)
        f.text(f"{start_time}",620,760,"#ffff00",fonte,tela)

        #checando colisão com plataformas
        wood_cll = f.moving_collision(sapo_rect,wood_list)
        turtle_cll = f.moving_collision(sapo_rect,turtle_list)
        
        #vidas/morte
        if f.death_onRiver(wood_cll,turtle_cll,sapo_rect,rio_rect,death_rect)==1:
            vidas-=f.death_onRiver(wood_cll,turtle_cll,sapo_rect,rio_rect,death_rect)
            dead=True
            water_death.play()
        f.text("VIDAS:",10,760,"#ffffff",fonte,tela)
        f.text(f"x{vidas}",115,760,"#ffffff",fonte,tela)
        if vidas==0:
            ativo=False
            f.save_cur_score(cur_score)
            f.save_cur_time(start_time)
            end_game=True
        
        #colisão com bordas da tela
        if f.oneobs_collision(sapo_rect,rect_direita)==False:
            sapo_rect.x=636
            rmove_auth=False
        else:
            rmove_auth=True
        if f.oneobs_collision(sapo_rect,rect_esquerda)==False:
            sapo_rect.x=0
            lmove_auth=False
        else:
            lmove_auth=True
        if f.oneobs_collision(sapo_rect,rect_cima)==False:
            sapo_rect.y=90
            move_auth=False

        #colisão com grama perto dos objetivos
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_1.x) in range(0,19):
            move_auth=False
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_2.x) in range(-20,61):
            move_auth=False
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_3.x) in range(-20,61):
            move_auth=False
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_4.x) in range(-20,61):
            move_auth=False
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_5.x) in range(-20,61):
            move_auth=False
        elif (sapo_rect.y-48)<=y_max and (sapo_rect.x-rect_fim_6.x)==-15:
            move_auth=False
        else:
            move_auth=True
        
        #colisao com objetivo
        if f.obj_resetOnTouch(sapo_rect,obj_list,tela,obj_surf,empty_rect_list):
            start_time+=10
            score+=50
        
        if f.empty_rect_cll(sapo_rect,empty_rect_list):
            vidas-=1
            death_rect.x=sapo_rect.x
            death_rect.y=sapo_rect.y
            dead=True
            water_death.play()

        if obj_list==[]:
            end_game=True

        #time-reset/return to menu
        if start_time==0:
            ms=0
            
        #colisao com carros
        if f.obs_collision(sapo_rect,obs_rect_rlist)==False:
            vidas-=1
            death_rect.x=sapo_rect.x
            death_rect.y=sapo_rect.y
            dead=True
            car_death.play()
            f.sapo_default_pos(sapo_rect)
            
            
            
        elif f.obs_collision(sapo_rect,obs_rect_llist)==False:
            vidas-=1
            death_rect.x=sapo_rect.x
            death_rect.y=sapo_rect.y
            dead=True
            car_death.play()
            f.sapo_default_pos(sapo_rect)
            
            
        elif f.obs_collision(sapo_rect,faster_obs_list)==False:
            vidas-=1
            death_rect.x=sapo_rect.x
            death_rect.y=sapo_rect.y
            dead=True
            car_death.play()
            f.sapo_default_pos(sapo_rect)
            
            
        elif f.oneobs_collision(sapo_rect,snake_rect)==False:
            vidas-=1
            death_rect.x=sapo_rect.x
            death_rect.y=sapo_rect.y
            dead=True
            car_death.play()
            f.sapo_default_pos(sapo_rect)

         
                
    
    else:
            #player pos reset, titlescreen, highscore
        #timer reset
        ms=1000
        #reset da lista de objetivos e da lista dos rects pós colisão
        f.obj_listReset(obj_list,obj_rect_1,obj_rect_2,obj_rect_3,obj_rect_4,obj_rect_5)
        empty_rect_list = [pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48)),pygame.Rect((-100,-100),(48,48))]
        #score,vida e posição
        score=0
        vidas=10
        dead=False
        f.sapo_default_pos(sapo_rect)
        #tela dividida do menu e o titulo
        pygame.draw.rect(tela,"#000047",pygame.Rect((0,0),(WIDTH,HEIGHT//2)))
        pygame.draw.rect(tela,"#000000",pygame.Rect((0,384),(WIDTH,HEIGHT//2)))
        tela.blit(title_surf,title_rect)
        #textos do menu
        f.text(point_table,223,300,"#ffffff",fonte,tela)
        f.text(instrucaop1,50,HEIGHT//2,"#ffffff",fonte,tela)
        f.text(instrucaop2,50,430,"#ffffff",fonte,tela)
        f.text(instrucaop3,50,476,"#ffffff",fonte,tela)
        f.text(instrucaop4,50,510,"#ff0000",fonte,tela)
        f.text(press2p,120,700,"#ffffff",fonte,tela)
        f.text("TOME CUIDADO COM A ÁGUA",135,600,"#ff0000",fonte,tela)
        f.text("USE AS SETINHAS OU WASD PARA MOVER",50,545,"#ffffff",fonte,tela)
        f.text("HI-SCORE",250,35,"#ffffff",fonte,tela)
        f.text(f"{hi_score:05}",280,65,"#ffffff",fonte,tela)

        #calculo do plus bonus
        if end_game:
            move_auth=False
            rmove_auth=False
            lmove_auth=False
            final_score+=(store_time*10)
            f.text("SCORE",100,35,"#ffffff",fonte,tela)
            f.text(f"{final_score:05}",100,65,"#ffffff",fonte,tela)
            if final_score>hi_score:
                f.save_high_score(final_score)

    pygame.display.update()
    clock.tick(60)

#TODO -> idk test i guess
