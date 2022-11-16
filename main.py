import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Frogger/graphics/sapo/sapo_stand.png").convert_alpha()
        self.rect = self.image.get_rect(center = (336,694))
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and move_auth:
            self.rect.y-=24
    
    def update(self):
        self.player_input()
        

def sapo_default_pos():
    sapo_rect.x = 318
    sapo_rect.y = 678

def obstacle_rmove(obs_list):
    if obs_list:
        for rect in obs_list:
            rect.x -= 5
            tela.blit(car1_surf,rect)#627
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -100]
        return obs_list
    else:
        return []

def faster_obs_rmove(obs_list):
    if obs_list:
        for rect in obs_list:
            rect.x -= 10
            if rect.y==530:
                tela.blit(smallcar_surf,rect)#530
            else:
                tela.blit(truck_surf,rect)
            
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -100]
        return obs_list
    else:
        return []

def turtle_move(obs_list):
    if obs_list:
        for rect in obs_list:
            rect.x -= 2
            tela.blit(turtle_surf,rect)
            
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -150]
        return obs_list
    else:
        return []

def obstacle_lmove(obs_list):
    if obs_list:
        for rect in obs_list:
            rect.x += 5
            if rect.y>500:
                tela.blit(car2_surf,rect)
            elif 500>=rect.y>450:
                tela.blit(car3_surf,rect)
            
            
                
        obs_list = [obstacle for obstacle in obs_list if obstacle.x < 772]
        return obs_list
    else:
        return []

def wood_move(obs_list):
    if obs_list:
        for rect in obs_list:
            rect.x += 5
            if rect.y==341:
                tela.blit(wood_surf,rect)#(sapo_rect.y-rect.y)=49
            elif rect.y==245:
                tela.blit(wood_m_surf,rect)#49
            else:
                tela.blit(wood_l_surf,rect)#48
                
        obs_list = [obstacle for obstacle in obs_list if obstacle.x < 772]
        return obs_list
    else:
        return []

def obs_collision(player,obstacle_list):
    #multiobs
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player.colliderect(obstacle_rect) and obstacle_rect.y not in [341,245,150]:
                return False
    return True

def moving_collision(player,obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if obstacle_rect.y==341:
                if player.colliderect(obstacle_rect):
                    player.x+=5
                    return True
            elif obstacle_rect.y==292:
                if player.colliderect(obstacle_rect):
                    player.x-=2
                    return True
            elif obstacle_rect.y==245:
                if player.colliderect(obstacle_rect):
                    player.x+=5
                    return True
            elif obstacle_rect.y==199:
                if player.colliderect(obstacle_rect):
                    player.x-=2
                    return True
            elif obstacle_rect.y==150:
                if player.colliderect(obstacle_rect):
                    player.x+=5
                    return True
            else:
                return False

def oneobs_collision(player_rect,enemy_rect):
    if player_rect.colliderect(enemy_rect):
        return False
    return True

def river_collision(wood_cll,turtle_cll):
    if (wood_cll or turtle_cll)==None and sapo_rect.colliderect(rio_rect):
        return True
    else:
        return False
    
def death_onRiver():
    death=0
    if river_collision(wood_cll,turtle_cll):
        death=1
        sapo_default_pos()
    return death

def obj_resetOnTouch(player,obj_list):
    if obj_list:
        for rect in obj_list:
            tela.blit(obj_surf,rect)
            if player.colliderect(rect):
                obj_list.remove(rect)
                sapo_default_pos()
                return True
    return False          

def obj_listReset(obj_list):
    obj_list.clear()
    obj_list.append(obj_rect_1)
    obj_list.append(obj_rect_2)
    obj_list.append(obj_rect_3)
    obj_list.append(obj_rect_4)
    obj_list.append(obj_rect_5)

def text(instrucao,x,y,cor):
    isurf = fonte.render(instrucao,False,cor)
    rect = isurf.get_rect(bottomleft = (x,y))
    return tela.blit(isurf,rect)

def get_high_score():
    high_score = 0
    try:
        high_score_file = open("Frogger/txts/high_score.txt","r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        return 0
    return high_score

def save_high_score(new_high_score):
    high_score_file = open("Frogger/txts/high_score.txt","w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()

def get_cur_score():
    score_cur = 0
    try:
        stored_score_file = open("Frogger/txts/stored_score.txt","r")
        score_cur = int(stored_score_file.read())
        stored_score_file.close()
    except IOError:
        return 0
    return score_cur

def save_cur_score(new_score):
    stored_score_file = open("Frogger/txts/stored_score.txt","w")
    stored_score_file.write(str(new_score))
    stored_score_file.close()

def get_cur_time():
    time = 0
    try:
        stored_time_file = open("Frogger/txts/stored_time.txt","r")
        time = int(stored_time_file.read())
        stored_time_file.close()
    except IOError:
        return 0
    return time

def save_cur_time(new_time):
    stored_time_file = open("Frogger/txts/stored_time.txt","w")
    stored_time_file.write(str(new_time))
    stored_time_file.close()

pygame.init()
WIDTH = 224*3
HEIGHT = 256*3
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()
ativo = False
fonte = pygame.font.Font("Frogger/fonts/Retro Gaming.ttf",25)
start_time = 90
vidas = 10
end_game = False

player = pygame.sprite.GroupSingle()
player.add(Player())

#tela de inicio
title_surf = pygame.image.load("Frogger/graphics/title.png").convert_alpha()
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

#background
bg_surf = pygame.image.load("Frogger/graphics/bg.png").convert_alpha()
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
#sapo
sapo_stand = pygame.image.load("Frogger/graphics/sapo/sapo_stand.png").convert_alpha()
sapo_jump1 = pygame.image.load("Frogger/graphics/sapo/sapo_jump1.png").convert_alpha()
sapo_jump2 = pygame.image.load("Frogger/graphics/sapo/sapo_jump2.png").convert_alpha()
sapo_fw = [sapo_stand,sapo_jump1,sapo_jump2]
sapo_index = 0
sapo_surf = sapo_fw[sapo_index]
sapo_rect = sapo_surf.get_rect(center = (336,699))
fw = False
left = False
right = False

#cobra
snake_frame_1 = pygame.image.load("Frogger/graphics/snake/snake_stand.png").convert_alpha()
snake_frame_2 = pygame.image.load("Frogger/graphics/snake/snake_move1.png").convert_alpha()
snake_frame_3 = pygame.image.load("Frogger/graphics/snake/snake_move2.png").convert_alpha()
snake_frames = [snake_frame_1,snake_frame_2,snake_frame_3]
snake_frame_index = 0
snake_surf = snake_frames[snake_frame_index]
snake_rect = snake_surf.get_rect(center = (-800,405))

#carros
car1_surf = pygame.image.load("Frogger/graphics/carros/car1.png").convert_alpha()
car1_surf = pygame.transform.rotate(car1_surf,180)

car2_surf = pygame.image.load("Frogger/graphics/carros/car2.png").convert_alpha()

car3_surf = pygame.image.load("Frogger/graphics/carros/car3.png").convert_alpha()

smallcar_surf = pygame.image.load("Frogger/graphics/carros/smallcar.png").convert_alpha()

truck_surf = pygame.image.load("Frogger/graphics/carros/truck.png").convert_alpha()

#plataformas
wood_surf = pygame.image.load("Frogger/graphics/river/wood/wood.png").convert_alpha()
wood_m_surf = pygame.image.load("Frogger/graphics/river/wood/wood_m.png").convert_alpha()
wood_l_surf = pygame.image.load("Frogger/graphics/river/wood/wood_l.png").convert_alpha()

turtle_frame_1 = pygame.image.load("Frogger/graphics/river/turtle/turtle_1.png").convert_alpha()
turtle_frame_2 = pygame.image.load("Frogger/graphics/river/turtle/turtle_2.png").convert_alpha()
turtle_frame_3 = pygame.image.load("Frogger/graphics/river/turtle/turtle_3.png").convert_alpha()
turtle_frames = [turtle_frame_1,turtle_frame_2,turtle_frame_3]
turtle_frame_index = 0
turtle_surf = turtle_frames[turtle_frame_index]


wood_cll = False
turtle_cll = False

#objetivo
obj_frame_1 = pygame.image.load("Frogger/graphics/obj/obj_1.png").convert_alpha()
obj_frame_2 = pygame.image.load("Frogger/graphics/obj/obj_2.png").convert_alpha()
obj_frames = [obj_frame_1,obj_frame_2]
obj_frame_index = 0
obj_surf = obj_frames[obj_frame_index]
obj_rect_1 = pygame.Rect((24,93),(48,48))
obj_rect_2 = pygame.Rect((168,93),(48,48))
obj_rect_3 = pygame.Rect((312,93),(48,48))
obj_rect_4 = pygame.Rect((456,93),(48,48))
obj_rect_5 = pygame.Rect((600,93),(48,48))


#endgame
end_game_rect = pygame.Rect((0,0),(WIDTH,HEIGHT))


#rects dos obstaculos
obs_rect_rlist = []
faster_obs_list = []
turtle_list = []
obs_rect_llist = []
wood_list = []

#rect dos objetivos
obj_list = [obj_rect_1,obj_rect_2,obj_rect_3,obj_rect_4,obj_rect_5]

#timers
ms=1000
seconds = pygame.USEREVENT
pygame.time.set_timer(seconds,ms)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)
large_wood_timer = pygame.USEREVENT + 6
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
pygame.time.set_timer(sapo_anim_timer,3000)

#main loop
while True:
    #atualiza o highscore assim que inicia
    hi_score = get_high_score()
    store_time = get_cur_time()
    final_score = get_cur_score()
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if ativo:
            if event.type == pygame.KEYDOWN:            
                if event.key in [pygame.K_UP,pygame.K_w] and move_auth:
                    sapo_rect.y-=48
                    score+=10
                    fw=True
                    #and (618>=sapo_rect.x>18)
                elif event.key in [pygame.K_LEFT,pygame.K_a] and lmove_auth:
                    sapo_rect.x-=50
                    score+=10
                    left=True
                    #and (618>sapo_rect.x>=18) 
                elif event.key in [pygame.K_RIGHT,pygame.K_d] and rmove_auth:
                    sapo_rect.x+=50
                    score+=10
                    right=True

            if event.type == seconds:
                start_time-=1

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
                wood_list.append(wood_l_surf.get_rect(midleft = (-300,165)))
                

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
                    for i in range(3):
                        sapo_index +=1
                        if sapo_index>2:
                            sapo_index=0
                        sapo_surf = sapo_fw[sapo_index]
                    fw=False

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
        
        tela.blit(bg_surf,bg_rect)
        
        #score
        cur_score = score
        text("SCORE",100,35,"#ffffff")
        text(f"{cur_score:05}",100,65,"#ffffff")
        if cur_score>hi_score:
            save_high_score(cur_score)
              
        #obstaculos que vem da direita
        obs_rect_rlist = obstacle_rmove(obs_rect_rlist)
        faster_obs_list = faster_obs_rmove(faster_obs_list) 
        turtle_list = turtle_move(turtle_list)       
        #obstaculos que vem da esquerda
        obs_rect_llist = obstacle_lmove(obs_rect_llist)
        wood_list = wood_move(wood_list)


        tela.blit(snake_surf,snake_rect)
        tela.blit(sapo_surf,sapo_rect)

        player.draw(tela)
        player.update()

        #cronometro
        text("TEMPO:",510,760,"#ffff00")
        text(f"{start_time}",620,760,"#ffff00")

        #checando colisão com cada obstaculo
        wood_cll = moving_collision(sapo_rect,wood_list)
        turtle_cll = moving_collision(sapo_rect,turtle_list)
        #sapo_rect.y-rio_rect.y = 242
        #None = nenhuma plataforma

        #vidas/morte
        vidas-=death_onRiver()
        text("VIDAS:",10,760,"#ffffff")
        text(f"x{vidas}",115,760,"#ffffff")
        if vidas==0:
            ativo=False
            save_cur_score(cur_score)
            save_cur_time(start_time)
            end_game=True

        #colisão com bordas
        if oneobs_collision(sapo_rect,rect_direita)==False:
            sapo_rect.x=636
            rmove_auth=False
        else:
            rmove_auth=True
        if oneobs_collision(sapo_rect,rect_esquerda)==False:
            sapo_rect.x=0
            lmove_auth=False
        else:
            lmove_auth=True
        if oneobs_collision(sapo_rect,rect_cima)==False:
            sapo_rect.y=90
            move_auth=False
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
        if obj_resetOnTouch(sapo_rect,obj_list):
            start_time+=10
            score+=50
        
        if obj_list==[]:
            end_game=True

        #time-reset/return to menu
        if start_time==0:
            ms=0
            
        #colisao carros
        if obs_collision(sapo_rect,obs_rect_rlist)==False:
            vidas-=1
            sapo_default_pos()
            
        elif obs_collision(sapo_rect,obs_rect_llist)==False:
            vidas-=1
            sapo_default_pos()
            
        elif obs_collision(sapo_rect,faster_obs_list)==False:
            vidas-=1
            sapo_default_pos()
            
        elif oneobs_collision(sapo_rect,snake_rect)==False:
            vidas-=1
            sapo_default_pos()
                
    
    else:
        #player pos reset, titlescreen, highscore
        ms=1000
        obj_listReset(obj_list)
        score=0
        vidas=10
        sapo_default_pos()
        pygame.draw.rect(tela,"#000047",pygame.Rect((0,0),(WIDTH,HEIGHT//2)))
        pygame.draw.rect(tela,"#000000",pygame.Rect((0,384),(WIDTH,HEIGHT//2)))
        tela.blit(title_surf,title_rect)
        text(point_table,223,300,"#ffffff")
        text(instrucaop1,50,HEIGHT//2,"#ffffff")
        text(instrucaop2,50,430,"#ffffff")
        text(instrucaop3,50,476,"#ffffff")
        text(instrucaop4,50,510,"#ff0000")
        text(press2p,120,700,"#ffffff")
        text("TOME CUIDADO COM A ÁGUA",135,600,"#ff0000")
        text("USE AS SETINHAS OU WASD PARA MOVER",50,545,"#ffffff")
        text("HI-SCORE",250,35,"#ffffff")
        text(f"{hi_score:05}",280,65,"#ffffff")
        if end_game:
            move_auth=False
            rmove_auth=False
            lmove_auth=False
            final_score+=(store_time*10)
            text("SCORE",100,35,"#ffffff")
            text(f"{final_score:05}",100,65,"#ffffff")
            if final_score>hi_score:
                save_high_score(final_score)



    pygame.display.update()
    clock.tick(60)

#TODO -> animations, check class thing agane, check functions thing later
