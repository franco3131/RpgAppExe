'''
Created on Sep 16, 2020

@author: davidfranco
'''



import pygame


class StaticText:
    def __init__(self,screen):  
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Verdana', 25)
        self.screen=screen
        self.showMessages=False
        self.checkCount=0

        
    
    def displayStatsMenu(self,hp,maxHp,atk,hit,defense,evasion,monstersDefeated,level,experience,maxExperience):
        BLUE=(0,100,128)
        self.screen.fill(BLUE)
        self.fire= self.myfont.render('Magic: Fire', False, (255,255,255))
        if monstersDefeated>=1:
            self.fire= self.myfont.render('Magic: Fire2', False, (255,255,255))
        if monstersDefeated<12:
            self.fire2= self.myfont.render('XP Needed for Fire 2: ' +str(monstersDefeated) +'/12', False, (255,255,255))
            self.screen.blit(self.fire2,(10,130))
        if monstersDefeated>=12 and monstersDefeated<=34:
            self.fire2= self.myfont.render('XP Needed for Fire 3: ' +str(monstersDefeated) +'/35', False, (255,255,255))
            self.screen.blit(self.fire2,(10,130))
        if monstersDefeated>=35:
            self.fire= self.myfont.render('Magic: Fire3', False, (255,255,255))
        self.experience= self.myfont.render('Until next Level Up ' +str(experience) +'/'+str(maxExperience), False, (255,255,255))
        self.screen.blit(self.experience,(10,160))
            
        self.name= self.myfont.render('Exilok', False, (255,255,255))
        self.Atk= self.myfont.render('Attack '+str(atk), False, (255,255,255))
        self.hit= self.myfont.render('Hit '+str(hit), False, (255,255,255))
        self.defense= self.myfont.render('Defense '+str(defense), False, (255,255,255))
        self.level= self.myfont.render('Level '+str(level), False, (255,255,255))
#         self.evasion= self.myfont.render('Evasion '+str(evasion), False, (255,255,255))
        result='HP '+str(hp)+'/'+str(maxHp)
        self.hp=self.myfont.render(result, False, (255,255,255))
        self.screen.blit(self.hp,(400,240))
        self.screen.blit(self.Atk,(400,280))       
        self.screen.blit(self.hit,(400,320))
        self.screen.blit(self.defense,(400,360))
        self.screen.blit(self.level,(400,400))       
        self.screen.blit(self.fire,(10,100))
#         self.screen.blit(self.evasion,(400,400))
#         self.screen.blit(self.items,(100,40))
#         self.screen.blit(self.Equipment,(100,100))
#         self.screen.blit(self.magic,(100,160))
#         self.screen.blit(self.status,(100,220))
        self.screen.blit(self.name,(420,13))
#         pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(10, 20, 250, 260), 10)
        
    def displayBattleMenu(self):
        BLUE=(0,100,128)

        pygame.draw.rect(self.screen,BLUE,(380,330,680,360))
        self.attack= self.myfont.render('Attack', False, (255,255,255))

        self.screen.blit(self.attack,(570,330))
        
        self.item= self.myfont.render('Cure', False, (255,255,255))

        self.screen.blit(self.item,(570,360))
        
        self.defend= self.myfont.render('Fire', False, (255,255,255))
        
        self.screen.blit(self.defend,(570,390))
        
        self.defend=self.myfont.render('Defend', False, (255,255,255))
         
        self.screen.blit(self.defend,(570,420))
        
        self.escape= self.myfont.render('Escape', False, (255,255,255))
         
        self.screen.blit(self.escape,(570,450))
        
        
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(380,330,320,160), 6)
        
        
    def displayBattleMessage(self,message):
        BLUE=(0,100,128)
        pygame.draw.rect(self.screen,BLUE,(0,0,700,50))
        self.attack= self.myfont.render(message, False, (255,255,255))
        self.screen.blit(self.attack,(300,18))
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,0,700,50), 6)
    
    def showMessageWhenButtonPressed(self,message):
        keys = pygame.key.get_pressed() 
        
        if keys[pygame.K_a] and self.showMessages==True:
            self.showMessages=False
#             time.sleep(0.3)
        elif keys[pygame.K_a] and self.showMessages==False:
            self.showMessages=True
            self.checkCount=self.checkCount+1
#             time.sleep(0.3)       
        if self.showMessages==True:
                    
            BLUE=(0,100,128)
            pygame.draw.rect(self.screen,BLUE,(0,0,700,50))
            self.attack= self.myfont.render(message, False, (255,255,255))
            self.screen.blit(self.attack,(5,18))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,0,700,50), 4)
            pygame.display.update()
            
    def showMessage(self,message):  
        BLUE=(0,100,128)
        pygame.draw.rect(self.screen,BLUE,(0,0,700,50))
        self.attack= self.myfont.render(message, False, (255,255,255))
        self.screen.blit(self.attack,(5,18))
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,0,700,50), 4)

    

                
    
        
    
    def showMonsterDamage(self,hp):
        self.damage= self.myfont.render(hp, False, (255,255,255))
        self.screen.blit(self.damage,(400,100))
    def showEduardDamage(self,hp):
        self.damage= self.myfont.render(hp, False, (255,255,255))
        self.screen.blit(self.damage,(300,340))
        
    def showEduardoHP(self,hp):
        self.magic= self.myfont.render('HP', False, (255,255,255))
        self.screen.blit(self.magic,(400,340))
        self.Hp= self.myfont.render(hp, False, (255,255,255))
        self.screen.blit(self.Hp,(400,370))
        
    def showCureHp(self,hp):
        self.damage= self.myfont.render(hp, False, (0,255,0))
        self.screen.blit(self.damage,(300,330))
        
        
    def displayCureCount(self,cureCount):
        
        self.cure= self.myfont.render(cureCount, False, (255,255,255))
    
        self.screen.blit(self.cure,(640,360))
        

        
    def displayFireCount(self,fireCount):
        
        self.fire= self.myfont.render(fireCount, False, (255,255,255))
        
        self.screen.blit(self.fire,(640,390))        
        
    
    def displayEscapeCount(self,escapeCount):
        
        self.escape= self.myfont.render(escapeCount, False, (255,255,255))
        
        self.screen.blit(self.escape,(670,450))    
        
        
    
    def displayDefenseCount(self,defenseCount):
        
        self.defense= self.myfont.render(defenseCount, False, (255,255,255))
        
        self.screen.blit(self.defense,(670,420))        
        

        

    