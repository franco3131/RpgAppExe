

import random 

import time

from pygame import mixer
import pygame

from Game.BattleEnvironment import BattleEnvironment
from Game.MonsterStats import MonsterStats
from Game.Stats import Stats



class BattleLogic():
    firstArenaSet=False
    def __init__(self,screen,eduardoStats,textMenu,monsterArray):
        self.image=""
        pygame.font.init()
    
        self.myfont = pygame.font.SysFont('Comic Sans MS', 24)
        self.screen=screen

        pygame.mixer.quit()
#         pygame.mixer.pre_init(44100, 16, 2, 4096) 
        mixer.init() 
        mixer.music.load("battle2.mp3")
        mixer.music.play(-1)  


        
#         mixer.music.load("battle2.mp3") 
#         mixer.music.set_volume(4.1) 
#         mixer.music.play(-1)
      
        self.attack=False
        #hp,defense,hit,evasion,attack
        monsterData=[]
        self.battleEnvironment=BattleEnvironment(self.screen)
        self.character = pygame.image.load("benDown11.png")
        self.counter=0
        self.eduardoStats=eduardoStats
        self.textMenu=textMenu
        self.battleHandCursorX=510
        self.battleHandCursorY=330
        self.myAttack=0
        self.swordCounter=0
        self.isMonsterDefeated=False
        self.monsterAtk=False
        self.monsterAttackCounter=0
        self.showDefendMessageCount=0
        self.showDefendMessage=False
        monster=MonsterStats()
        monsters = monsterArray
# random item from list
        self.endSwordSound=False
        randomMonster=random.choice(monsters)
        print(randomMonster)
        monsterData=monster.setMonsterStats(randomMonster)
        self.dragon=self.battleEnvironment.renderMonster(randomMonster)
        self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
        self.endMonsterSound=False
        self.monsterTurn=False
        self.eduardoTurn=True
        self.damage2=0
        self.clock = pygame.time.Clock()
        self.count=0
        self.dismissedMessage=False
        self.buttonPressedCount=0;
        self.itemMenu=False;
        self.showCure=False;
        self.showCureCount=0
        self.messageTimer=0
        self.isMessageTimer=False
        self.timer=0
        self.monsterTurnCount=0
        self.isMagicOn=False
        self.magicTimer=0
        self.fireInProgress=False
        self.attackInProgress=False
        self.levelUpOn=False
        self.levelUpTimer=0
        self.isLevelUpTrue=False
        self.boss1Running=False
        self.boss2Running=False
        self.stopBoss1=False
        self.stopBoss2=False
        self.key1=False
        self.arena=""
        self.escapeCount=0
        self.runaway=False
        self.setArena('blueCrystalArea')
        self.cureAnimation=0
        self.boss1Key=False
        self.fire2DrawingTimer=400
        self.countDownTurns=random.randint(3,10) 
        self.countDownCount=0
#         self.displayedCountDown=random.randint(3,6) 
        self.displayedCountDown=random.randint(1,2) 
        self.displayBossAttackCountDown=False
        self.showDefendMessageCounter=0
        self.bossMessage=0
        self.defense=False
        self.powerfulMoveAnimation=0
        self.firePowerfulMoveAnimation=0
        self.powerfulMoveFinished=False
        



        

    
    def renderEnvironmentAndCharacters(self,isBattleRunning):
        if self.firstArenaSet==False:
            self.setArena('blueCrystalArea')
            self.firstArenaSet=True
        
        if(isBattleRunning==True):

          
            self.screen.blit(self.character,(260,400))
            self.screen.blit(self.dragon,(200,40))

            
            
            if (self.counter%30>15):
       
                self.counter=self.counter+1
                self.character=pygame.image.load("upRightFoot.png")
            else:
         
                self.counter=self.counter+1
                self.character=pygame.image.load("leftFoot22.png")
            



                    
                    
    def moveBattleMenu(self):

        keys = pygame.key.get_pressed()
        self.textMenu.displayBattleMenu()
        self.textMenu.displayFireCount(str(self.eduardoStats.getFire()))
        self.textMenu.displayCureCount(str(self.eduardoStats.getCure()))     
        self.textMenu.displayEscapeCount(str(self.eduardoStats.getEscape())) 
        self.textMenu.displayDefenseCount(str(self.eduardoStats.getDefense()))
              
        if self.getIsBoss1Running()==True and self.stopBoss1==False:
            mixer.stop()
            time.sleep(1)
            pygame.mixer.quit()
            mixer.init() 
            music= pygame.mixer.Sound("boss2.mp3")
            music.play()
#             mixer.music.load("boss2.mp3") 
#             mixer.music.set_volume(3.4) 
#             mixer.music.play(-1)
            self.setMessageTimerOn(True)
            monster=MonsterStats()
            monsterData=monster.setMonsterStats('boss1')
            self.dragon=self.battleEnvironment.renderMonster('boss1')
            self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
            self.setBoss1Key(True)
            self.stopBoss1=True   
            
        if self.getIsBoss2Running()==True and self.stopBoss2==False:
            mixer.stop()
            time.sleep(1)
            pygame.mixer.quit()
            mixer.init() 
            music= pygame.mixer.Sound("boss2.mp3")
            music.play()
#             mixer.music.load("boss2.mp3") 
#             mixer.music.set_volume(3.4) 
#             mixer.music.play(-1)
            self.setMessageTimerOn(True)
            monster=MonsterStats()
            monsterData=monster.setMonsterStats('boss2')
            self.dragon=self.battleEnvironment.renderMonster('boss2')
            self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
            self.stopBoss2=True   
            self.isEndGame=True
        

        if self.buttonPressedCount%2==0:
            self.monsterTurnCount=self.monsterTurnCount+1;
            if keys[pygame.K_DOWN] and self.attack==False:
                self.battleHandCursorY=self.battleHandCursorY+30
                effect = pygame.mixer.Sound('Cursor Move.wav')
                effect.play()
     
                if(self.battleHandCursorY>450):
                    self.battleHandCursorY=330
          
                    effect = pygame.mixer.Sound('Cursor Move.wav')
                    effect.play()
   
    #              time.sleep(.01)
            elif keys[pygame.K_UP] and self.attack==False:
    
          
                self.battleHandCursorY=self.battleHandCursorY-30
                effect = pygame.mixer.Sound('Cursor Move.wav')
                effect.play()

                if(self.battleHandCursorY<330):
                    self.battleHandCursorY=450
             
                    effect = pygame.mixer.Sound('Cursor Move.wav')

                    effect.play()
  
                 
             
            elif keys[pygame.K_a] and self.getEduardoTurn()==True and self.battleHandCursorY==330 and self.attack==False :
                self.attack=True
                self.eduardoStats.calculateAttack(self.monsterStats.getMyDefense())
                self.myAttack=self.eduardoStats.getDamage()
                self.monsterStats.calculateHpAfterAttack(self.myAttack)
                self.setMonsterTurn(True)
                

          
               
            elif keys[pygame.K_a] and self.getEduardoTurn()==True and self.battleHandCursorY==360:
                if self.eduardoStats.getCure()>0:
                    effect = pygame.mixer.Sound('cure.wav')
                    effect.play()
                    time.sleep(1.3)
                    self.showCure=True
                    cureCount=self.eduardoStats.getCure()
                    cureCount=cureCount-1
                    self.eduardoStats.setCure(cureCount)
                    
                    maxHp=self.eduardoStats.getMaxHp()
                    self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()+120)
                    if maxHp<self.eduardoStats.getMyHp():
                        self.eduardoStats.setMyHp(maxHp)
                    self.setMonsterTurn(True)
    
                   
    
            
                else:
                    effect = pygame.mixer.Sound('Cursor Error.wav')
                    effect.play()                         
            elif keys[pygame.K_a] and self.getEduardoTurn()==True and self.battleHandCursorY==390 and self.fireInProgress==False:
                if self.eduardoStats.getFire()>0:
                    self.fireInProgress=True
                    self.eduardoStats.calculateAttack(self.monsterStats.getMyDefense())
                    if self.eduardoStats.getIsFire2Enabled()==True:
                        self.myAttack=int(self.eduardoStats.getDamage())+int(self.eduardoStats.getDamage()*3.3)
                    elif self.eduardoStats.getIsFire3Enabled()==True:
                        self.myAttack=int(self.eduardoStats.getDamage())+int(self.eduardoStats.getDamage()*4.4)                       
                    else:
                        self.myAttack=int(self.eduardoStats.getDamage())+int(self.eduardoStats.getDamage()*2.2)
                    print("myAttack"+str(self.myAttack))
                    self.monsterStats.calculateHpAfterAttack(self.myAttack)
                    print("monster hp"+str(self.monsterStats.getMyHp()))
                    fireCount=self.eduardoStats.getFire()
                    fireCount=fireCount-1
                    self.eduardoStats.setFire(fireCount)
                    
                    effect = pygame.mixer.Sound('fire.wav')
                    effect.play()
                    
    
                    self.isMagicOn=True
                else:
                    effect = pygame.mixer.Sound('Cursor Error.wav')
                    effect.play()     
                print(self.eduardoStats.getFire())   
           
            
            elif keys[pygame.K_a] and self.getEduardoTurn()==True and self.battleHandCursorY==450 :
                if self.eduardoStats.getEscape()>0 and self.stopBoss1==False and self.stopBoss2==False:
                    self.monsterDefeated()
                    monster=MonsterStats()
                    monsters = ['dragon', 'monster1', 'monster2','monster3','monster4']
            # random item from list
                    randomMonster=random.choice(monsters)
                    print(randomMonster)
                    monsterData=monster.setMonsterStats(randomMonster)
                    self.dragon=self.battleEnvironment.renderMonster(randomMonster)
                    self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
                    self.setIsRunAway(True)
                    self.randomEncounter=random.randint(200,600)
                    escapeCount=self.eduardoStats.getEscape()
                    escape=escapeCount-1
                    self.eduardoStats.setEscape(escape)
                    pygame.mixer.quit()
                    mixer.init() 
#                     pygame.mixer.pre_init(44100, 16, 2, 4096) 
                    mixer.music.load("Fate In Haze.mp3")
                    mixer.music.play(-1)  
                    mixer.init() 

#                     mixer.music.load("Fate In Haze.mp3") 
#                     mixer.music.set_volume(2.0) 
#                     mixer.music.play(-1)
#                     time.sleep(0.2)
                else:
                    effect = pygame.mixer.Sound('Cursor Error.wav')
                    effect.play()                  
            elif keys[pygame.K_a] and self.getEduardoTurn()==True and self.battleHandCursorY==420 and self.showDefendMessage==False :
                effect = pygame.mixer.Sound('Cursor Move.wav')
                effect.play()

                self.showDefendMessage=True
                if self.eduardoStats.getDefense()<=0:
                    
                    effect = pygame.mixer.Sound('Cursor Error.wav')
                    effect.play()     
                else:
                    time.sleep(1.3)
                    self.defense=True
                    self.eduardoStats.setDefense(self.eduardoStats.getDefense()-1)
                                

                

                    
        if self.isMagicOn==True:
            if self.eduardoStats.getIsFire2Enabled()==True:
                if self.magicTimer<50:
  
                    self.fire=pygame.image.load("fireball2.png")
                    self.fire2=pygame.image.load("fireball3.png")                
                    self.screen.blit(self.fire,(200,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(240,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(280,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(320,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(130,self.fire2DrawingTimer-30))
                    self.screen.blit(self.fire,(160,self.fire2DrawingTimer-49))
                    self.screen.blit(self.fire,(500,self.fire2DrawingTimer-80))
                    self.screen.blit(self.fire,(450,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(130+self.fire2DrawingTimer,self.fire2DrawingTimer-66))
                    self.screen.blit(self.fire,(160+self.fire2DrawingTimer,self.fire2DrawingTimer-144))
                    self.screen.blit(self.fire,(500-self.fire2DrawingTimer,self.fire2DrawingTimer-288))
                    self.screen.blit(self.fire,(450-self.fire2DrawingTimer,self.fire2DrawingTimer-399))
                    self.screen.blit(self.fire,(33+self.fire2DrawingTimer,self.fire2DrawingTimer-67))
                    self.screen.blit(self.fire,(444+self.fire2DrawingTimer,self.fire2DrawingTimer-77))
                    self.screen.blit(self.fire,(560-self.fire2DrawingTimer,self.fire2DrawingTimer-188))
                    self.screen.blit(self.fire,(422-self.fire2DrawingTimer,self.fire2DrawingTimer-499))
                    self.screen.blit(self.fire,(10+self.fire2DrawingTimer,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(122+self.fire2DrawingTimer,self.fire2DrawingTimer-122))
                    self.screen.blit(self.fire,(300-self.fire2DrawingTimer,self.fire2DrawingTimer-38))
                    self.screen.blit(self.fire,(550-self.fire2DrawingTimer,self.fire2DrawingTimer-39))
                    self.screen.blit(self.fire,(552+self.fire2DrawingTimer,self.fire2DrawingTimer-47))
                    self.screen.blit(self.fire,(133+self.fire2DrawingTimer,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(232-self.fire2DrawingTimer,self.fire2DrawingTimer-41))
                    self.screen.blit(self.fire,(345-self.fire2DrawingTimer,self.fire2DrawingTimer-122))
                    self.screen.blit(self.fire,(602+self.fire2DrawingTimer,self.fire2DrawingTimer-47))
                    self.screen.blit(self.fire,(444+self.fire2DrawingTimer,self.fire2DrawingTimer-32))
                    self.screen.blit(self.fire,(132-self.fire2DrawingTimer,self.fire2DrawingTimer-11))
                    self.screen.blit(self.fire,(3-self.fire2DrawingTimer,self.fire2DrawingTimer-22))
                    self.screen.blit(self.fire2,(102+self.fire2DrawingTimer,self.fire2DrawingTimer-57))
                    self.screen.blit(self.fire2,(344+self.fire2DrawingTimer,self.fire2DrawingTimer-22))
                    self.screen.blit(self.fire2,(532-self.fire2DrawingTimer,self.fire2DrawingTimer-1))
                    self.screen.blit(self.fire2,(31-self.fire2DrawingTimer,self.fire2DrawingTimer-212))
                    self.screen.blit(self.fire2,(112+self.fire2DrawingTimer,self.fire2DrawingTimer-7))
                    self.screen.blit(self.fire2,(134+self.fire2DrawingTimer,self.fire2DrawingTimer-12))
                    self.screen.blit(self.fire2,(532-self.fire2DrawingTimer,self.fire2DrawingTimer-1))
                    self.screen.blit(self.fire2,(31-self.fire2DrawingTimer,self.fire2DrawingTimer-122))                
                    self.magicTimer=self.magicTimer+1
                    self.fire2DrawingTimer=self.fire2DrawingTimer-self.magicTimer-3
                    self.textMenu.showMonsterDamage(str(self.myAttack))
                else:
                    self.isMagicOn=False
                    self.magicTimer=0
                    self.setMonsterTurn(True)
                    self.monsterDefeated()
                    self.setEduardoTurn(False)
                    self.fireInProgress=False
                    self.attack=False
                    self.fire2DrawingTimer=400
            elif self.eduardoStats.getIsFire3Enabled()==True:
                if self.magicTimer<50:

                    self.fire=pygame.image.load("blueFireBall.png")
                    self.fire2=pygame.image.load("fireball3.png")                
                    self.screen.blit(self.fire,(200,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(240,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(280,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(320,self.fire2DrawingTimer))
                    self.screen.blit(self.fire,(130,self.fire2DrawingTimer-30))
                    self.screen.blit(self.fire,(160,self.fire2DrawingTimer-49))
                    self.screen.blit(self.fire,(500,self.fire2DrawingTimer-80))
                    self.screen.blit(self.fire,(450,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(130+self.fire2DrawingTimer,self.fire2DrawingTimer-66))
                    self.screen.blit(self.fire,(160+self.fire2DrawingTimer,self.fire2DrawingTimer-144))
                    self.screen.blit(self.fire,(500-self.fire2DrawingTimer,self.fire2DrawingTimer-288))
                    self.screen.blit(self.fire,(450-self.fire2DrawingTimer,self.fire2DrawingTimer-399))
                    self.screen.blit(self.fire,(33+self.fire2DrawingTimer,self.fire2DrawingTimer-67))
                    self.screen.blit(self.fire,(444+self.fire2DrawingTimer,self.fire2DrawingTimer-77))
                    self.screen.blit(self.fire,(560-self.fire2DrawingTimer,self.fire2DrawingTimer-188))
                    self.screen.blit(self.fire,(422-self.fire2DrawingTimer,self.fire2DrawingTimer-499))
                    self.screen.blit(self.fire,(10+self.fire2DrawingTimer,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(122+self.fire2DrawingTimer,self.fire2DrawingTimer-122))
                    self.screen.blit(self.fire,(300-self.fire2DrawingTimer,self.fire2DrawingTimer-38))
                    self.screen.blit(self.fire,(550-self.fire2DrawingTimer,self.fire2DrawingTimer-39))
                    self.screen.blit(self.fire,(552+self.fire2DrawingTimer,self.fire2DrawingTimer-47))
                    self.screen.blit(self.fire,(133+self.fire2DrawingTimer,self.fire2DrawingTimer-33))
                    self.screen.blit(self.fire,(232-self.fire2DrawingTimer,self.fire2DrawingTimer-41))
                    self.screen.blit(self.fire,(345-self.fire2DrawingTimer,self.fire2DrawingTimer-122))
                    self.screen.blit(self.fire,(602+self.fire2DrawingTimer,self.fire2DrawingTimer-47))
                    self.screen.blit(self.fire,(444+self.fire2DrawingTimer,self.fire2DrawingTimer-32))
                    self.screen.blit(self.fire,(132-self.fire2DrawingTimer,self.fire2DrawingTimer-11))
                    self.screen.blit(self.fire,(3-self.fire2DrawingTimer,self.fire2DrawingTimer-22))
          
                    self.magicTimer=self.magicTimer+1
                    self.fire2DrawingTimer=self.fire2DrawingTimer-self.magicTimer-3
                    self.textMenu.showMonsterDamage(str(self.myAttack))
                else:
                    self.isMagicOn=False
                    self.magicTimer=0
                    self.setMonsterTurn(True)
                    self.monsterDefeated()
                    self.setEduardoTurn(False)
                    self.fireInProgress=False
                    self.attack=False
                    self.fire2DrawingTimer=400
            else:
                if self.magicTimer<20:
                    if self.magicTimer%5<3:
                        self.fire=pygame.image.load("fire1.png")
                        self.screen.blit(self.fire,(200,40))
                    else:
                        self.fire=pygame.image.load("fire2.png")
                        self.screen.blit(self.fire,(200,40))
                    self.magicTimer=self.magicTimer+1
                    self.textMenu.showMonsterDamage(str(self.myAttack))
                else:
                    self.isMagicOn=False
                    self.magicTimer=0
                    self.setMonsterTurn(True)
                    self.monsterDefeated()
                    self.setEduardoTurn(False)
                    self.fireInProgress=False
                    self.attack=False
        

        if self.showCure==True:
            self.showCureCount=self.showCureCount+1;
            count=0

            print(count)
            self.textMenu.showCureHp("120")
            count=count+1

            if(self.showCureCount==10):
                self.showCureCount=0
                self.showCure=False        
        if self.showDefendMessage==True:
            self.textMenu.displayBattleMessage('Barrier for one turn')
            if self.showDefendMessageCounter>=40:

                self.showDefendMessage=False
                self.showDefendMessageCounter=0
            self.showDefendMessageCounter=self.showDefendMessageCounter+1
                
                
                

                
                
        self.buttonPressedCount=self.buttonPressedCount+1;

        

        self.textMenu.showEduardoHP(str(self.eduardoStats.getMyHp())+'/'+str(self.eduardoStats.getMaxHp()))
        hand=pygame.image.load("hand3.png")
        self.screen.blit(hand,(self.battleHandCursorX,self.battleHandCursorY+10))
  
        
#340,370,400,430
    

            
    def eduardoAttack(self):
        if self.attack==True:

            self.swordCounter=self.swordCounter+1
            if (self.swordCounter>=0 and self.swordCounter<=2):
                self.sword1=pygame.image.load("sword1.png")
                self.screen.blit(self.sword1,(350,250))
                if self.endSwordSound==False:
                    effect = pygame.mixer.Sound('swordSound.wav')

                    effect.play()
#                         effect.set_volume(3)
#                     pygame.mixer.Channel(1).play(pygame.mixer.Sound('swordSound.wav'), maxtime=600)

                    self.endSwordSound=True
            elif(self.swordCounter>2 and self.swordCounter<=4):
               
                self.sword2=pygame.image.load("sword2.png")
                self.screen.blit(self.sword2,(250,250))
                time.sleep(.01)
          
            elif(self.swordCounter>4 and self.swordCounter<=10):
           
                self.sword3=pygame.image.load("sword3.png")
                self.screen.blit(self.sword3,(200,250))
                self.damage=int(self.eduardoStats.getDamage())
                self.textMenu.showMonsterDamage(str(self.damage))
                
                time.sleep(.01)
             
                if self.swordCounter==8:
          
                    self.attack=False
                    self.swordCounter=0
                    self.monsterStats.setMyHp(self.monsterStats.getMyHp()-self.damage)
                    print("monster HP"+str(self.monsterStats.getMyHp()))
                    self.setEduardoTurn(False)
                    self.setMonsterTurn(True)
                    self.monsterDefeated()
                    time.sleep(1)
                    self.endSwordSound=False
            

  


                   
            


            
    def monsterAttack(self):
        if self.getMonsterTurn()==True:
            self.monsterAtk=self.monsterStats.calculateAttack(self.eduardoStats.getMyDefense())
            self.damage2=int(self.monsterStats.getDamage()) 
            self.setMonsterTurn(False)
            self.monsterAtk=True

            
        if self.monsterAtk==True:
            if self.getIsBoss1Running()==True:
                self.boss1Attack()
            elif self.getIsBoss2Running()==True:
                self.boss2Attack()

            else:    
                    time.sleep(0.2)
                    self.monsterAttackCounter=self.monsterAttackCounter+1
                    if (self.monsterAttackCounter>=0 and self.monsterAttackCounter<=2):
                        self.sword1=pygame.image.load("attackedLeftFoot.png")
                        self.screen.blit(self.sword1,(260,400))
#                         effect = pygame.mixer.Sound('hit.wav')
#                         effect.play()
#                         effect.set_volume(3)
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('hit.wav'), maxtime=600)

                        time.sleep(.01)
                        self.endMonsterSound=True
                    elif(self.monsterAttackCounter>2 and self.monsterAttackCounter<=4):
                        self.sword2=pygame.image.load("leftFoot22.png")
                        self.screen.blit(self.sword2,(260,400))
                        time.sleep(.01)
                    elif(self.monsterAttackCounter>4 and self.monsterAttackCounter<=10):
                         
                        self.sword3=pygame.image.load("attackedLeftFoot.png")
                        self.screen.blit(self.sword3,(260,400))
                        if self.defense==True:
                            self.textMenu.showEduardDamage(str(int(self.damage2/3)))
                            

                        else:
                            self.textMenu.showEduardDamage(str(self.damage2))


                         
                        time.sleep(.01)
                        if self.monsterAttackCounter==8:
                            self.displayedCountDown=self.displayedCountDown-1

                            self.countDownCount=self.countDownCount+1
                            self.monsterAttackCounter=0
                            self.eduardoDefeated()
                            self.monsterAtk=False
                            self.setEduardoTurn(True)
                            self.endMonsterSound=False
                            if self.defense==True:
                                self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-int(self.damage2/3))  
                                self.defense=False
                            else:
                                self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-self.damage2)  




        hand=pygame.image.load("hand3.png")
        self.screen.blit(hand,(self.battleHandCursorX+10,self.battleHandCursorY+10))
    
    def monsterDefeated(self):


        
        if self.monsterStats.getMyHp()<0:
            self.eduardoStats.setMonstersDefeated(self.eduardoStats.getMonstersDefeated()+1)
            if(self.eduardoStats.getMonstersDefeated()>=12 and self.eduardoStats.getMonstersDefeated()<=34):
#             if(self.eduardoStats.getMonstersDefeated()>=1 and self.eduardoStats.getMonstersDefeated()<3):
                self.eduardoStats.setIsFire2Enabled(True)
            elif (self.eduardoStats.getMonstersDefeated()>=35):
#             elif (self.eduardoStats.getMonstersDefeated()>=3):
                self.eduardoStats.setIsFire2Enabled(False)
                self.eduardoStats.setIsFire3Enabled(True)
            effect = pygame.mixer.Sound('monsterDefeated.wav')
            effect.play()
            time.sleep(2)
            self.randomEncounter=random.randint(5,200)
            self.setMessageTimerOn(True)
            monster=MonsterStats()
            monsters = ['dragon', 'monster1', 'monster2','monster3','monster4']
    # random item from list
            randomMonster=random.choice(monsters)
            print(randomMonster)
            monsterData=monster.setMonsterStats(randomMonster)

            self.dragon=self.battleEnvironment.renderMonster(randomMonster)
            self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
            if self.eduardoStats.getCure()!=5:
                cures=self.eduardoStats.getCure()+1
                self.eduardoStats.setCure(cures)
            if self.eduardoStats.getFire()!=5:
                fires=self.eduardoStats.getFire()+1
                self.eduardoStats.setFire(fires) 
            if self.eduardoStats.getDefense()!=3:
                defense=self.eduardoStats.getDefense()+1
                self.eduardoStats.setDefense(defense)
                
            self.setIsBoss1Running(False)
            self.setIsBoss2Running(False)
            
            if self.escapeCount%10==0 and self.eduardoStats.getEscape()<5:
                self.escapeCount=self.escapeCount+1

            self.boss1EnableSpecial=False
            pygame.mixer.quit()
            mixer.init() 
#             pygame.mixer.pre_init(44100, 16, 2, 4096) 
            mixer.music.load("Fate In Haze.mp3")
            mixer.music.play(-1)  

#             mixer.init() 
#             music= pygame.mixer.Sound("Fate In Haze.mp3")
#             music.play()
#             mixer.music.load("Fate In Haze.mp3") 
#             mixer.music.set_volume(2.0) 
#             mixer.music.play(-1)
            self.hit=random.randint(200, 600)

            time.sleep(1)
        
#             self.eduardoStats.statsIncreaseLevelUp()
            self.setIsMonsterDefeated(True)


            self.eduardoStats.setExperience(self.monsterStats.getMonsterExperience())
            print(self.eduardoStats.getExperience())
            if self.eduardoStats.getExperience()>=self.eduardoStats.getMaxExperience():
                self.eduardoStats.increaseMaxExperience()
                self.eduardoStats.statsIncreaseLevelUp()
                self.eduardoStats.setExperience(0)
                self.levelUpOn=True
                effect = pygame.mixer.Sound('levelUp.wav')
                effect.play()
                self.setLevelUpTrue(True)
                self.eduardoStats.setLevel(self.eduardoStats.getLevel()+1)
                
                
    def boss1Attack(self):
        self.textMenu.displayBattleMessage(str(self.displayedCountDown)+" until major attack")
        self.displayBossAttackCountDown=True
        if  self.displayBossAttackCountDown==True and self.bossMessage<2:
            self.textMenu.displayBattleMessage(str(self.displayedCountDown)+" until major attack")
            self.bossMessage=self.bossMessage+1
        else:
            self.bossMessage=0
            self.displayBossAttackCountDown=False
             
             
             
        if self.displayedCountDown==0:
            self.powerfulMoveAnimation=self.powerfulMoveAnimation+3  
            print(self.displayedCountDown)
            if(self.powerfulMoveAnimation>0 and self.powerfulMoveAnimation<50 and self.powerfulMoveFinished==False):
                self.fire=pygame.image.load("fireball2.png")        
                self.screen.blit(self.fire,(300+self.powerfulMoveAnimation,300))
                self.screen.blit(self.fire,(400-self.powerfulMoveAnimation,300))
            elif((300+self.powerfulMoveAnimation)>=350 and (300+self.powerfulMoveAnimation)<450 and self.powerfulMoveFinished==False):
                self.fire=pygame.image.load("fire1.png")     
                self.fire2=pygame.image.load("fire2.png") 
                effect = pygame.mixer.Sound('fire.wav')
                effect.play()
                           
                self.screen.blit(self.fire,(random.randint(0,650),random.randint(0,500)))
                self.screen.blit(self.fire2,(random.randint(0,650),random.randint(0,500)))
                 
            elif((self.powerfulMoveAnimation+300)>=450 and self.powerfulMoveFinished==False):
                print("HEEEEEEYYYYYY")
                self.powerfulMoveFinished=True
                self.powerfulMoveAnimation=0

              
             
             
            if self.powerfulMoveFinished==True:
                self.monsterAttackCounter=self.monsterAttackCounter+1
                print("INSIDE HERE")
                if (self.monsterAttackCounter>=0 and self.monsterAttackCounter<=2):
                    self.sword1=pygame.image.load("attackedLeftFoot.png")
                    self.screen.blit(self.sword1,(260,400))
                    if self.endMonsterSound==False:
                        effect = pygame.mixer.Sound('hit.wav')
                        effect.play()
#                         effect.set_volume(3)
                        time.sleep(.02)
                        self.endMonsterSound=True
                elif(self.monsterAttackCounter>2 and self.monsterAttackCounter<=4):
                    self.sword2=pygame.image.load("leftFoot22.png")
                    self.screen.blit(self.sword2,(260,400))
                    time.sleep(.02)
                elif(self.monsterAttackCounter>4 and self.monsterAttackCounter<=10):
                     
                    self.sword3=pygame.image.load("attackedLeftFoot.png")
                    self.screen.blit(self.sword3,(260,400))
                    powerAttack=self.damage2+self.damage2*1.1
                    powerAttack=int(powerAttack)
                    if self.defense==True:
#                         powerAttack=int(powerAttack/3)
                        time.sleep(.02)
                        self.textMenu.showEduardDamage(str(int(powerAttack/3)))

                    else:
                        self.textMenu.showEduardDamage(str(powerAttack))
                    time.sleep(.01)
                    if self.monsterAttackCounter==8:
                        self.countDownCount=0

                        self.randomEncounter=random.randint(3,10)
                        self.monsterAttackCounter=0
                        self.eduardoDefeated()
                        self.monsterAtk=False
                        self.setEduardoTurn(True)
                        self.displayedCountDown=random.randint(3,6)
                        self.powerfulMoveFinished=False
                        self.endMonsterSound=False
                        if self.defense==True:
                            self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-int(powerAttack/3))
                            self.defense=False
                        else:

                            self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-powerAttack)
                        
        else:
#             time.sleep(0.2)
            self.monsterAttackCounter=self.monsterAttackCounter+1
            if (self.monsterAttackCounter>=0 and self.monsterAttackCounter<=2):
                self.sword1=pygame.image.load("attackedLeftFoot.png")
                self.screen.blit(self.sword1,(260,400))
                effect = pygame.mixer.Sound('hit.wav')
                effect.play()
#                 effect.set_volume(3)
                time.sleep(.01)
                self.endMonsterSound=True
            elif(self.monsterAttackCounter>2 and self.monsterAttackCounter<=4):
                self.sword2=pygame.image.load("leftFoot22.png")
                self.screen.blit(self.sword2,(260,400))
                time.sleep(.01)
            elif(self.monsterAttackCounter>4 and self.monsterAttackCounter<=10):
                    
                self.sword3=pygame.image.load("attackedLeftFoot.png")
                self.screen.blit(self.sword3,(260,400))
                time.sleep(.05)
                if self.defense==True:
                    self.textMenu.showEduardDamage(str(int(self.damage2/3)))                        
        
                else:
                    self.textMenu.showEduardDamage(str(self.damage2))
                    
#                 time.sleep(.01)
                if self.monsterAttackCounter==8:
                    self.displayedCountDown=self.displayedCountDown-1
                    self.countDownCount=self.countDownCount+1
                    self.monsterAttackCounter=0
                    self.eduardoDefeated()
                    self.monsterAtk=False
  
                    self.setEduardoTurn(True)
                    self.endMonsterSound=False
                    if self.defense==True:
                        self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-int(self.damage2/3))
                        self.defense=False
                    else:
                        self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-self.damage2) 

                        
                        
    def boss2Attack(self):
        self.textMenu.displayBattleMessage(str(self.displayedCountDown)+" until major attack")
        self.displayBossAttackCountDown=True
        if  self.displayBossAttackCountDown==True and self.bossMessage<2:
            self.textMenu.displayBattleMessage(str(self.displayedCountDown)+" until major attack")
            self.bossMessage=self.bossMessage+1
        else:
            self.bossMessage=0
            self.displayBossAttackCountDown=False
             
             
             
        if self.displayedCountDown==0:
            self.powerfulMoveAnimation=self.powerfulMoveAnimation+6  
            print(self.displayedCountDown)
            if(self.powerfulMoveAnimation>0 and self.powerfulMoveAnimation<400 and self.powerfulMoveFinished==False): 
                pygame.draw.rect(self.screen, (255,255,102), pygame.Rect(300,100,10,self.powerfulMoveAnimation), 10)

                effect = pygame.mixer.Sound('Electric Sound Effect.wav')
                effect.play()

                 
            else:
                print("HEEEEEEYYYYYY")
                self.powerfulMoveFinished=True
                self.powerfulMoveAnimation=0

              
             
             
            if self.powerfulMoveFinished==True:
                self.monsterAttackCounter=self.monsterAttackCounter+1
                print("INSIDE HERE")
                if (self.monsterAttackCounter>=0 and self.monsterAttackCounter<=2):
                    self.sword1=pygame.image.load("attackedLeftFoot.png")
                    self.screen.blit(self.sword1,(260,400))
                    if self.endMonsterSound==False:
                        effect = pygame.mixer.Sound('hit.wav')
                        effect.play()
#                         effect.set_volume(3)
                        time.sleep(.01)
                        self.endMonsterSound=True
                elif(self.monsterAttackCounter>2 and self.monsterAttackCounter<=4):
                    self.sword2=pygame.image.load("leftFoot22.png")
                    self.screen.blit(self.sword2,(260,400))
                    time.sleep(.01)
                elif(self.monsterAttackCounter>4 and self.monsterAttackCounter<=10):
                     
                    self.sword3=pygame.image.load("attackedLeftFoot.png")
                    self.screen.blit(self.sword3,(260,400))
                    powerAttack=self.damage2+self.damage2*1.1
                    powerAttack=int(powerAttack)
                    if self.defense==True:
                        self.textMenu.showEduardDamage(str(int(powerAttack/3)))

                    else:
                        self.textMenu.showEduardDamage(str(powerAttack))
                    time.sleep(.01)
                    if self.monsterAttackCounter==8:
                        self.countDownCount=0

                        self.randomEncounter=random.randint(3,10)
                        self.monsterAttackCounter=0
                        self.eduardoDefeated()
                        self.monsterAtk=False
                        self.setEduardoTurn(True)
                        self.displayedCountDown=random.randint(3,6)
                        
                        self.powerfulMoveFinished=False
                        self.endMonsterSound=False
                        if self.defense==True:
                            self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-int(powerAttack/3))
                            self.defense=False
                        else:

                            self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-powerAttack)
        else:
            time.sleep(0.2)
            self.monsterAttackCounter=self.monsterAttackCounter+1
            if (self.monsterAttackCounter>=0 and self.monsterAttackCounter<=2):
                self.sword1=pygame.image.load("attackedLeftFoot.png")
                self.screen.blit(self.sword1,(260,400))
                effect = pygame.mixer.Sound('hit.wav')
                effect.play()
#                 effect.set_volume(3)
                time.sleep(.01)
                self.endMonsterSound=True
            elif(self.monsterAttackCounter>2 and self.monsterAttackCounter<=4):
                self.sword2=pygame.image.load("leftFoot22.png")
                self.screen.blit(self.sword2,(260,400))
                time.sleep(.01)
            elif(self.monsterAttackCounter>4 and self.monsterAttackCounter<=10):
                    
                self.sword3=pygame.image.load("attackedLeftFoot.png")
                self.screen.blit(self.sword3,(260,400))
                if self.defense==True:
                    self.textMenu.showEduardDamage(str(int(self.damage2/3)))                        
        
                else:
                    self.textMenu.showEduardDamage(str(self.damage2))
                    
                time.sleep(.01)
                if self.monsterAttackCounter==8:
                    self.displayedCountDown=self.displayedCountDown-1
                    self.countDownCount=self.countDownCount+1
                    self.monsterAttackCounter=0
                    self.eduardoDefeated()
                    self.monsterAtk=False
                    self.setEduardoTurn(True)
                    self.endMonsterSound=False

                    if self.defense==True:
                        self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-int(self.damage2/3))
                        self.defense=False
                    else:
                        self.eduardoStats.setMyHp(self.eduardoStats.getMyHp()-self.damage2)                    
                
    def setIsBoss1Running(self,boss1Running):
        self.boss1Running=boss1Running
    def getIsBoss1Running(self):
        return self.boss1Running   
    def setIsBoss2Running(self,boss2Running):
        self.boss2Running=boss2Running
    def getIsBoss2Running(self):
        return self.boss2Running       
        
    def setBoss1Key(self,boss1Key):
        self.boss1Key=boss1Key
    def getBoss1Key(self):
        return self.boss1Key

            
    def eduardoDefeated(self):
        if self.eduardoStats.getMyHp()<=0:
            return True
            
    def setIsMonsterDefeated(self,defeated):
        self.isMonsterDefeated=defeated
    def getIsMonsterDefeated(self):
        return self.isMonsterDefeated
    def setIsRunAway(self,runaway):
        self.runaway=runaway
    def getIsRunAway(self):
        return self.runaway
    def setEduardoTurn(self,eduardoTurn):
        self.eduardoTurn=eduardoTurn
    def getEduardoTurn(self):
        return self.eduardoTurn
    def setMonsterTurn(self,monsterTurn):
        self.monsterTurn=monsterTurn
    def getMonsterTurn(self):
        return self.monsterTurn
    def setMessageTimerOn(self,message):
        self.isMessageTimer=message;
    def getMessageTimerOn(self):
        return self.isMessageTimer
    def setLevelUpTrue(self,isLevelUpTrue):
        self.isLevelUpTrue=isLevelUpTrue
    def getLevelUpTrue(self):
        return self.isLevelUpTrue
    def setArena(self,arena):
        self.arena=arena
    def getArena(self):
        return self.arena

            
    

              