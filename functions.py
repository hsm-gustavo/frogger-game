def sapo_default_pos(sapo_rect):
    #reseta pos sapo
    sapo_rect.x = 318
    sapo_rect.y = 678

def obstacle_rmove(obs_list,tela,car1_surf):
    #movimento dos obstaculos que vem da direita
    if obs_list:
        for rect in obs_list:
            rect.x -= 5
            tela.blit(car1_surf,rect)#627
        #os rects dos obstaculos ficam na lista até chegarem em x=-100
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -100]
        return obs_list
    else:
        return []

def faster_obs_rmove(obs_list,tela,smallcar_surf,truck_surf):
    #movimento dos obstaculos que vem da direita, mas com uma maior velocidade
    if obs_list:
        for rect in obs_list:
            rect.x -= 10
            if rect.y==530:
                tela.blit(smallcar_surf,rect)#530
            else:
                tela.blit(truck_surf,rect)
        #os rects dos obstaculos ficam na lista até chegarem em x=-100   
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -100]
        return obs_list
    else:
        return []

def turtle_move(obs_list,tela,turtle_surf):
    #movimento das tartarugas
    if obs_list:
        for rect in obs_list:
            rect.x -= 2
            tela.blit(turtle_surf,rect)
        #os rects das tartarugas ficam na lista até chegarem em x=-150 
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -150]
        return obs_list
    else:
        return []

def obstacle_lmove(obs_list,tela,car2_surf,car3_surf):
    #movimento dos obstaculos que vem da esquerda
    if obs_list:
        for rect in obs_list:
            rect.x += 5
            if rect.y>500:
                tela.blit(car2_surf,rect)
            elif 500>=rect.y>450:
                tela.blit(car3_surf,rect)
        #os rects dos obstaculos ficam na lista até chegarem em x=772    
        obs_list = [obstacle for obstacle in obs_list if obstacle.x < 772]
        return obs_list
    else:
        return []

def wood_move(obs_list,tela,wood_surf,wood_m_surf,wood_l_surf):
    if obs_list:
        for rect in obs_list:
            rect.x += 5
            if rect.y==341:
                tela.blit(wood_surf,rect)#(sapo_rect.y-rect.y)=49
            elif rect.y==245:
                tela.blit(wood_m_surf,rect)#49
            else:
                tela.blit(wood_l_surf,rect)#48
        #os rects dos obstaculos ficam na lista até chegarem em x=772 
        obs_list = [obstacle for obstacle in obs_list if obstacle.x < 772]
        return obs_list
    else:
        return []

def obs_collision(player,obstacle_list):
    #checa colisao com obstaculos
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player.colliderect(obstacle_rect) and obstacle_rect.y not in [341,245,150]:
                return False
    return True

def moving_collision(player,obstacle_list):
    #checa colisao com plataformas
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
    #checa colisao com rects unicos, que nao estao em listas
    if player_rect.colliderect(enemy_rect):
        return False
    return True

def river_collision(wood_cll,turtle_cll,sapo_rect,rio_rect):
    #colisao com rio
    if (wood_cll or turtle_cll)==None and sapo_rect.colliderect(rio_rect):
        return True
    else:
        return False
    
def death_onRiver(wood_cll,turtle_cll,sapo_rect,rio_rect,death_rect):
    #continuacao da colisao com rio
    death=0
    if river_collision(wood_cll,turtle_cll,sapo_rect,rio_rect):
        death=1
        death_rect.x=sapo_rect.x
        death_rect.y=sapo_rect.y
        sapo_default_pos(sapo_rect)
    return death

def obj_resetOnTouch(player,obj_list,tela,obj_surf,empty_rect):
    #reseta o player de posicao quando o player colidir com o rect do objetivo
    if obj_list:
        for rect in obj_list:
            tela.blit(obj_surf,rect)
            if player.colliderect(rect):
                empty_rect[obj_list.index(rect)].x = rect.x
                empty_rect[obj_list.index(rect)].y = rect.y
                obj_list.remove(rect)
                sapo_default_pos(player)
                return True
    return False          

def empty_rect_cll(player,empty):
    #adiciona colisão com a agua no lugar do objetivo
    for rect in empty:
        if player.colliderect(rect):
            sapo_default_pos(player)
            return True

def obj_listReset(obj_list,obj_rect_1,obj_rect_2,obj_rect_3,obj_rect_4,obj_rect_5):
    #reseta lista de objetivos quando ativo=False
    obj_list.clear()
    obj_list.append(obj_rect_1)
    obj_list.append(obj_rect_2)
    obj_list.append(obj_rect_3)
    obj_list.append(obj_rect_4)
    obj_list.append(obj_rect_5)

def text(instrucao,x,y,cor,fonte,tela):
    #cria textos
    isurf = fonte.render(instrucao,False,cor)
    rect = isurf.get_rect(bottomleft = (x,y))
    return tela.blit(isurf,rect)

def get_high_score():
    #pega o highscore dentro de um arquivo de texto
    high_score = 0
    try:
        high_score_file = open("txts/high_score.txt","r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        return 0
    return high_score

def save_high_score(new_high_score):
    #salva o highscore em um arquivo de texto
    high_score_file = open("txts/high_score.txt","w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()

def get_cur_score():
    #pega o atual score dentro de um arquivo de texto para calcular o plus bonus (score + (tempo restante * 10))
    score_cur = 0
    try:
        stored_score_file = open("txts/stored_score.txt","r")
        score_cur = int(stored_score_file.read())
        stored_score_file.close()
    except IOError:
        return 0
    return score_cur

def save_cur_score(new_score):
    #salva o atual score em um arquivo de texto
    stored_score_file = open("txts/stored_score.txt","w")
    stored_score_file.write(str(new_score))
    stored_score_file.close()

def get_cur_time():
    #pega o tempo restante dentro de um arquivo de texto para calcular o plus bonus (score + (tempo restante * 10))
    time = 0
    try:
        stored_time_file = open("txts/stored_time.txt","r")
        time = int(stored_time_file.read())
        stored_time_file.close()
    except IOError:
        return 0
    return time

def save_cur_time(new_time):
    #salva o tempo restante em um arquivo de texto
    stored_time_file = open("txts/stored_time.txt","w")
    stored_time_file.write(str(new_time))
    stored_time_file.close()
