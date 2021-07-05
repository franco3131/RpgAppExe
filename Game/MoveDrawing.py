
'''
Created on Sep 16, 2020

@author: davidfranco
'''



import json
import os
import random 
import time

from pygame import mixer
import pygame

from Game.BattleEnvironment import BattleEnvironment
from Game.BattleLogic import BattleLogic
from Game.Environment import Environment
from Game.MonsterStats import MonsterStats
from  Game.StaticText import StaticText


class MoveDrawing:
    def __init__(self,screen,eduardoStats):
        pygame.font.init()
        mixer.init() 
        self.x=0
        self.y=170
        self.handCursorX=30
        self.handCursorY=40
        self.character = pygame.image.load("benDown11.png")
        self.screen =screen
        self.screen.blit(self.character,(self.x,self.y))
        self.isMenuRunning=False
        self.running=True
        self.clock = pygame.time.Clock()
        self.numberOfSteps=0
        self.battleRunning=False
        self.battleEnvironment=BattleEnvironment(self.screen)
        self.randomEncounter='';
        self.environment=Environment(self.screen)
        self.battle='';
        self.monsterStats=MonsterStats()
        self.isCharacterStatsInitiated=True
        self.eduardoStats=eduardoStats
        self.textMenu=StaticText(self.screen)
        self.timer=0
        self.messageTime=0
        self.isTimer=False
        self.boss2Initialize=False
        self.matrix='';
        self.message1=False
        self.message2=False
        self.message3=False
        self.dictKeys={}
        self.dictKeys['room1']='null'
        self.dictKeys['straightRoom']='null'
        self.dictKeys['mazeRoom']='null'
        self.dictKeys['straightRoom2']='null'
        self.dictKeys['neonRoom']='null'
        self.dictKeys['outside']='null'
        self.loadLRoom=False
        self.storedLRoomState=False
        self.storedMazeRoomState=False 
        self.storedNeonRoomState=False
        self.crystalShimers=False
        self.boss1Running=False
        self.storedKey=False
        self.unlockedDoor1=False
        self.isLRoomOpenAfterSave=False
        self.isLRoomOpen=False
        self.backgroundTimer=0
        self.dictStats={}
        self.isSaved=False
        self.isEndGame=False
        self.showPathWay=False
        self.boss1EnableSpecial=False
        self.playDeathMusic=False
        self.secretCounter=0
        self.isMainCharacterDefeated=False
        self.isFFOn=False
        self.timerFFMessage=0
        self.ffButtonPressed=False
        self.boss1Initialize=False
        
       
        
        
    def initializeMatrix(self):
        self.matrix=self.battleEnvironment.createFieldMatrix()
        
            
    def lRoomMatrix(self):
        self.matrix=self.battleEnvironment.createFieldMatrixLRoom()
        
    def setMonsterStats(self):
        if self.dictKeys['room1']=='open':
            monsters = ['dragon', 'monster1', 'monster2','monster3','monster4']
    # random item from list
            randomMonster=random.choice(monsters)
            return self.monsterStats.setMonsterStats(randomMonster)

        else:
            monsters = ['dragon', 'monster1', 'monster2','monster3','monster4']
    # random item from list
            randomMonster=random.choice(monsters)
            return self.monsterStats.setMonsterStats2(randomMonster)

    
    def moveMenuHand(self):

        if self.getIsBattleRunning()==False:
            keys = pygame.key.get_pressed()
    #         self.clock.tick(60)
            if keys[pygame.K_z] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:
               
                self.setIsMenuRunning(True)
                
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Cursor Move.wav'), maxtime=600)

#                 time.sleep(1)
     

#           
            elif keys[pygame.K_x] and self.getIsBattleRunning()==False and self.getIsMenuRunning()==True:
                self.setIsMenuRunning(False)
                effect = pygame.mixer.Sound('cursorBack.wav')           
                effect.play()
                self.setIsMenuRunning(False)
            if self.getIsMenuRunning()==True:
                hp=self.eduardoStats.getMyHp()
                maxHp=self.eduardoStats.getMaxHp()
                attack=self.eduardoStats.getAttack()
                hit=self.eduardoStats.getHit()
                defense=self.eduardoStats.getMyDefense()
                evasion=self.eduardoStats.getEvasion()
                monstersDefeated=self.eduardoStats.getMonstersDefeated()
                level=self.eduardoStats.getLevel()
                experience=self.eduardoStats.getExperience()
                maxExperience=self.eduardoStats.getMaxExperience()
                self.textMenu.displayStatsMenu(hp,maxHp,attack,hit,defense,evasion,monstersDefeated,level,experience,maxExperience)
#                 hand=pygame.image.load("../Images/hand3.png")
                benjamin=pygame.image.load("benHead2.png")
#                 self.screen.blit(hand,(self.handCursorX,self.handCursorY))
                self.screen.blit(benjamin,(400,40))
                pygame.display.flip()
                pygame.display.update()
            else:
                self.setIsMenuRunning(False)
    
                
    def MoveBenjamin(self):
        self.backgroundTimer=self.backgroundTimer+1
        if self.dictKeys['room1']=='open':
            self.environment.renderEnvironment("LRoom",self.backgroundTimer)
        elif self.dictKeys['straightRoom']=='open':
            self.environment.renderEnvironment("straightRoom",self.backgroundTimer)
        elif self.dictKeys['mazeRoom']=='open':
            self.environment.renderEnvironment("maze",self.backgroundTimer)
        elif self.dictKeys['straightRoom2']=='open':
            self.environment.renderEnvironment("straightRoom",self.backgroundTimer)
        elif self.dictKeys['neonRoom']=='open':
            self.environment.renderEnvironment("neonRoom",self.backgroundTimer)

        else:
            self.environment.renderEnvironment("blueCrystalArea",self.backgroundTimer)
        if self.showPathWay==True:
            self.bg = pygame.image.load("floorArea.png")
            self.screen.blit(self.bg, (311,1))
    

        if self.getIsBattleRunning()==False:
            self.screen.blit(self.character,(self.x,self.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed() 
        if self.getIsBattleRunning()==False and self.getIsMenuRunning()==False: # checking pressed keys
            if keys[pygame.K_RIGHT] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:  # If 'right' - MOVE RIGHT
                    
                    
                if self.x>=647:
                    self.x=647
                elif self.matrix[self.x+3][self.y]==0:
                
                
                    self.x=self.x+3  
                    
                    self.incrementNumberOfSteps()
    
                    if (self.x%20>10):
             
                        self.character=pygame.image.load("benRight31.png")
                    else:
                        self.character=pygame.image.load("benRight12.png")
        
            elif keys[pygame.K_DOWN] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:
               

                if self.y>410:
                    self.y=407
                elif self.matrix[self.x][self.y+3]==0: 
                
                    self.y=self.y+3
                    self.incrementNumberOfSteps()
                    if (self.y%20>10):
          
                        self.character=pygame.image.load("benDown12.png")
                    else:
                        self.character=pygame.image.load("benDown11.png")
            elif keys[pygame.K_LEFT] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False: # If 'right' - MOVE RIGHT
                if self.x<3:
                    self.x=3
                elif self.matrix[self.x-3][self.y]==0:
                
                    self.x=self.x-3
                    self.incrementNumberOfSteps()
                    if (self.x%20>10):
        
                        self.character=pygame.image.load("benLeft31.png")
                    else:
                        self.character=pygame.image.load("benLeft12.png")
            elif keys[pygame.K_UP] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:
                
                if self.y<0:
                    self.y=0
                elif self.matrix[self.x][self.y-3]==0: 
                    self.y=self.y-3
                    self.incrementNumberOfSteps()
                    if (self.y%20>10):
                     
                        self.character=pygame.image.load("upRightFoot.png")
                    else:
                        self.character=pygame.image.load("leftFoot22.png")
            elif keys[pygame.K_a] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:

                print("hi")          
            elif keys[pygame.K_u] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:
                self.secretCounter=self.secretCounter+1
                if self.secretCounter==3:
                    self.setIsBattleRunning(True)
                    self.incrementNumberOfSteps() 
                    monsterArray=[]
    
                    monsterArray=['ben']
       
                    self.battle=BattleLogic(self.screen,self.eduardoStats,self.textMenu,monsterArray)
                    self.randomEncounter=random.randint(50,380) 
                    effect = pygame.mixer.Sound('EnterBattle.wav')
                    effect.play()
                    
                    time.sleep(1) 
            elif keys[pygame.K_p] and self.getIsMenuRunning()==False and self.getIsBattleRunning()==False:
                self.timerFFMessage=0
                self.ffButtonPressed=True
                if self.getIsFFOn()==True:
                    time.sleep(1)
                    self.setIsFFOn(False)
                else:
                    time.sleep(1)
                    self.setIsFFOn(True)
                    
            elif keys[pygame.K_s] and (self.x>=465 and self.x<=519) and (self.y>=344 and self.y<=401) and self.getIsBattleRunning()==False and self.dictKeys['room1']=='null':
#             elif keys[pygame.K_s] and self.dictKeys['room1']==null:
                print(self.eduardoStats.getMaxHp())

                self.eduardoStats.setMyHp(self.eduardoStats.getMaxHp())
                if self.isLRoomOpen==True:
                    self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                    'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                    ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':True,'loadMazeRoom':False,'loadNeonRoom':False,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}
                else:
                    self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                    'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                    ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':False,'loadMazeRoom':False,'loadNeonRoom':False,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}

                jsonData = json.dumps(self.dictStats)

                home=os.getenv("HOME")
                f = open(home+'/'+'stats.json',"w")
                f.write(jsonData)
                f.close()
                time.sleep(3)
                self.isSaved=True
            elif keys[pygame.K_s] and (self.x>=419 and self.x<=455) and (self.y>=196 and self.y<=262) and self.getIsBattleRunning()==False and self.dictKeys['mazeRoom']=='open':

                print(self.eduardoStats.getMaxHp())
                self.eduardoStats.setMyHp(self.eduardoStats.getMaxHp())
                self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                        'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                        ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':False,'loadMazeRoom':True,'loadNeonRoom':False,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}
                
                jsonData = json.dumps(self.dictStats)

                home=os.getenv("HOME")
                f = open(home+'/'+'stats.json',"w")
                f.write(jsonData)
                f.close()
                time.sleep(3)
                self.isSaved=True
            elif keys[pygame.K_s] and (self.x>=419 and self.x<=455) and (self.y>=196 and self.y<=262) and self.getIsBattleRunning()==False and self.dictKeys['neonRoom']=='open':

                print(self.eduardoStats.getMaxHp())
                self.eduardoStats.setMyHp(self.eduardoStats.getMaxHp())
                self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                        'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                        ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':False,'loadMazeRoom':False,'loadNeonRoom':True,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}
                
                jsonData = json.dumps(self.dictStats)

                home=os.getenv("HOME")
                f = open(home+'/'+'stats.json',"w")
                f.write(jsonData)
                f.close()
                time.sleep(3)
                self.isSaved=True  
            elif keys[pygame.K_s] and (self.x>=305 and self.x<=320) and (self.y>=1 and self.y<=5) and self.getIsBattleRunning()==False and self.dictKeys['outside']=='open':

                print(self.eduardoStats.getMaxHp())
                self.eduardoStats.setMyHp(self.eduardoStats.getMaxHp())
                self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                        'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                        ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':False,'loadMazeRoom':False,'loadNeonRoom':True,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}
                
                
                jsonData = json.dumps(self.dictStats)
  

                home=os.getenv("HOME")
                f = open(home+'/'+'stats.json',"w")
                f.write(jsonData)
                f.close()
                time.sleep(3)
                
# initialize Loading


                self.isSaved=True    
                self.isEndGame=True    
                
            if self.storedLRoomState==True:
                self.dictKeys['room1']='open'
                self.y=403
                self.x=443
                self.matrix=self.battleEnvironment.createFieldMatrixLRoom()
                self.boss1Initialize=True
#                 self.monsterArray=['wizard','blueWoman','greenDragon']
#                 self.battle=BattleLogic(self.screen,self.eduardoStats,self.textMenu,monsterArray)
                self.loadLRoom=True 
                self.storedLRoomState=False
                self.isLRoomOpen=True
                self.crystalShimers=False
            if self.storedMazeRoomState==True:
                self.dictKeys['straightRoom']='closed'
                self.dictKeys['mazeRoom']='open'
                self.matrix=self.battleEnvironment.createFieldMatrixMazeRoom()
                self.y=256
                self.x=455
                self.boss1Initialize=True
                self.storedMazeRoomState=False
                self.dictKeys['room1']='closed'
                
                self.crystalShimers=False          
#                 This allows for higher level monsters
                self.isLRoomOpen=True
            if self.storedNeonRoomState==True:
                self.dictKeys['straightRoom']='closed'
                self.dictKeys['mazeRoom']='closed'
                self.dictKeys['straightRoom2']='closed'
                self.dictKeys['neonRoom']='open'
                self.matrix=self.battleEnvironment.createFieldMatrixNeonRoom()
                self.y=256
                self.x=455
#                 This allows for higher level monsters
                self.isLRoomOpen=True
                self.storedNeonRoomState=False
                self.crystalShimers=False
                self.dictKeys['room1']='closed'
                self.boss1Initialize=True
            if self.getIsFFOn()==True and self.ffButtonPressed==True:
                self.timerFFMessage=self.timerFFMessage+1
                if self.timerFFMessage<=80:
                
                    self.textMenu.showMessage("fast forward On")
                else:
                    self.ffButtonPressed=False
            elif self.ffButtonPressed==True:
                self.timerFFMessage=self.timerFFMessage+1
                if self.timerFFMessage<=40:
                    
                    self.textMenu.showMessage("fast forward Off")   
                else:
                    self.ffButtonPressed=False                
                  
                
            
#              
        print("************************")
        print("x")           
        print(self.x)       
        print("y")
        print(self.y)
        print("**************************")
#          
                
                
                
    def moveBattleCursor(self):
        if self.isMainCharacterDefeated==True:
            self.textMenu.displayBattleMessage('annihilated')
        
        if self.isTimer==True and self.isMainCharacterDefeated==False:

            print(self.battle.getIsRunAway())
            if self.battle.getLevelUpTrue()==True:
                self.textMenu.displayBattleMessage('Level Up !!')
   
            else:
                self.textMenu.displayBattleMessage('End Of Battle')

            self.timer=self.timer+1
            if self.timer==25:
                
                self.timer=0
                self.isTimer=False
                self.battle.setLevelUpTrue(False)



        if(self.getNumberOfSteps()==self.randomEncounter and self.getIsBattleRunning()==False and self.message2==True and self.isMainCharacterDefeated==False):
            time.sleep(1)
            self.setIsBattleRunning(True)
            self.incrementNumberOfSteps() 
            monsterArray=[]
            if self.isLRoomOpen==True:
                monsterArray=['greenDragon','blueWoman','wizard','easyMonster2']
            else:
                
                monsterArray=['dragon', 'monster1', 'monster2','monster3','monster4','easyMonster']
            self.battle=BattleLogic(self.screen,self.eduardoStats,self.textMenu,monsterArray)
            self.randomEncounter=random.randint(50,380) 
            effect = pygame.mixer.Sound('EnterBattle.wav')
            effect.play()
            
            time.sleep(1)
        elif(self.getIsBattleRunning()==True and self.isMainCharacterDefeated==False):

            if self.dictKeys['room1']=='open':
                self.environment.renderEnvironment("LRoom",0)
            elif self.dictKeys['straightRoom']=='open':
                self.environment.renderEnvironment("straightRoom",0)
            elif self.dictKeys['mazeRoom']=='open':
                self.environment.renderEnvironment("maze",0)
            elif self.dictKeys['straightRoom2']=='open':
                self.environment.renderEnvironment("straightRoom",0)
            elif self.dictKeys['neonRoom']=='open':
                self.environment.renderEnvironment("neonRoom",0)
            else:
                self.environment.renderEnvironment("blueCrystalArea",0)
# 
            self.battle.renderEnvironmentAndCharacters(self.getIsBattleRunning())   
         
                  
            self.battle.moveBattleMenu()
            if self.battle.getEduardoTurn()==True:
                self.battle.eduardoAttack()
                
            
            else:

                self.battle.monsterAttack()
                      
            
            if self.battle.getIsMonsterDefeated()==True:
                self.isTimer=True
                self.setIsBattleRunning(False)
                self.battle.setIsMonsterDefeated(self.battle.getIsMonsterDefeated())
                self.resetNumberOfSteps()
                
            elif self.battle.getIsRunAway()==True:
                self.isTimer=True
                self.setIsBattleRunning(False)
                self.resetNumberOfSteps()                
                

                
            elif self.battle.eduardoDefeated()==True:
                self.isMainCharacterDefeated=True
                if self.playDeathMusic==False:
                    self.eduardoStats.setCure(0)
                    self.eduardoStats.setEscape(0)
                    self.eduardoStats.setFire(0)
                    time.sleep(1.2)
                    mixer.stop()
                    mixer.init() 
                    
#                     pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
#                     FarAway= pygame.mixer.Sound("Faraway Promise.mp3")

#                     pygame.mixer.pre_init(44100, 16, 2, 4096) 
                    mixer.music.load("Faraway Promise.mp3")
                    mixer.music.play(-1)  
#                     mixer.music.load("Music/Faraway Promise.mp3") 
#                     mixer.music.set_volume(3.4) 
#                     mixer.music.play(-1)
                    self.playDeathMusic=True


                self.eduardoStats.setMyHp(0)
                time.sleep(0.01)
                self.textMenu.displayBattleMessage('annihilated')
                self.messageTime=self.messageTime+1
                if self.messageTime==180:
                    exit()


            
    def showMessageByLocation(self):


        if ((self.x>=325 and self.x<=345) and (self.y>=147 and self.y<=155) and self.storedKey==False and self.getIsBattleRunning()==False and self.boss1Initialize==False):
            time.sleep(0.09)
            self.textMenu.showMessageWhenButtonPressed('The crystal shimmers, you unlocked the door...')
            self.crystalShimers=True
        elif ((self.x>=149 and self.x<=164) and (self.y>=358 and self.y<=373) and self.dictKeys['neonRoom']=='open' and self.boss2Initialize==False):
            self.setIsBattleRunning(True)
            self.textMenu.showMessage('You pressed button')
            self.isEndGame=True
            self.showPathWay=True
#             time.sleep(2)
#             self.battle.battleEnvironment.setIsBossRunning(True)
            self.boss2Initialize=True
            monsterArray=['wizard','blueWoman','greenDragon','easyMonster2','easyMonster2']
            self.battle=BattleLogic(self.screen,self.eduardoStats,self.textMenu,monsterArray)
            self.battle.setIsBoss2Running(True)
            self.incrementNumberOfSteps() 
            
        elif ((self.x>=325 and self.x<=347) and (self.y>=162 or self.y<=166) and self.crystalShimers==True and self.getIsMenuRunning()==False):
            self.setIsBattleRunning(True)
            monsterArray=[]
            if self.isLRoomOpen==True:
                monsterArray=['wizard','blueWoman','greenDragon']
            else:
                
                monsterArray=['dragon', 'monster1', 'monster2','monster3','monster4','easyMonster','easyMonster']
            self.battle=BattleLogic(self.screen,self.eduardoStats,self.textMenu,monsterArray)
            self.battle.setIsBoss1Running(True)
            self.loadLRoom=True
            self.battle.battleEnvironment.setIsBossRunning(True)
            self.incrementNumberOfSteps() 
            self.crystalShimers=False
            self.storedKey=True
            self.isLRoomOpen=True
        elif((self.x>=318 and self.x<=347) and (self.y==0 or self.y==-3) and self.storedKey==True):
#         elif((self.x>=318 and self.x<=342) and (self.y==0 or self.y==-3)):
#             self.textMenu.showMessageWhenButtonPressed('unlocked')
            self.dictKeys['room1']='open'
            self.y=403
            self.x=443
            self.matrix=self.battleEnvironment.createFieldMatrixLRoom()
            self.dragon=self.battle.battleEnvironment.renderMonster('boss1')
            self.isLRoomOpen=True
#             monster=MonsterStats()
#             monsterData=monster.setMonsterStats('boss1')
#             print(monsterData[0])
#             self.monsterStats=Stats(monsterData[0],monsterData[1],monsterData[2],monsterData[3],monsterData[4],monsterData[5])
        elif ((self.x>=465 and self.x<=519) and (self.y>=344 and self.y<=401) and self.dictKeys['room1']=='null' and self.getIsBattleRunning()==False and self.getIsMenuRunning()==False):
            if self.isSaved==False:
                self.textMenu.showMessage('Press S to save and restore Health')
            else:
                self.textMenu.showMessage('healed and Game is Saved')
            effect = pygame.mixer.Sound('twinkle.wav')
            effect.play()
            time.sleep(0.02)
        elif ((self.x>=419 and self.x<=455) and (self.y>=196 and self.y<=262) and self.dictKeys['mazeRoom']=='open' and self.getIsBattleRunning()==False and self.getIsMenuRunning()==False):
            if self.isSaved==False:
                self.textMenu.showMessage('Press S to save and restore Health')
            else:
                self.textMenu.showMessage('healed and Game is Saved')
            effect = pygame.mixer.Sound('twinkle.wav')
            effect.play()
            time.sleep(0.02)
        elif ((self.x>=419 and self.x<=455) and (self.y>=196 and self.y<=262) and self.dictKeys['neonRoom']=='open' and self.getIsBattleRunning()==False and self.getIsMenuRunning()==False):
            if self.isSaved==False:
                self.textMenu.showMessage('Press S to save and restore Health')
            else:
                self.textMenu.showMessage('healed and Game is Saved')
            effect = pygame.mixer.Sound('twinkle.wav')
            effect.play()
            time.sleep(0.02)
        elif((self.x>=318 and self.x<=342) and (self.y==0 or self.y==-3) and self.crystalShimers==False and self.getIsBattleRunning()==False and self.getIsMenuRunning()==False):
            self.textMenu.showMessageWhenButtonPressed('Locked')
        elif (self.x>=260 and self.x<=365) and (self.y>=1 and self.y<=5) and self.getIsBattleRunning()==False and self.dictKeys['neonRoom']=='open':
            self.dictKeys['outside']='open'

            if self.isEndGame==True:
                self.textMenu.showMessage('END GAME."u" 3 times:secret battle."p":FF')
                self.eduardoStats.setMyHp(self.eduardoStats.getMaxHp())
                self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit(),
                        'defense':self.eduardoStats.getMyDefense(),'fire2':self.eduardoStats.getIsFire2Enabled(),'monstersDefeated':self.eduardoStats.getMonstersDefeated()
                        ,'level':self.eduardoStats.getLevel(),'fire3':self.eduardoStats.getIsFire3Enabled(),'loadLRoom':False,'loadMazeRoom':False,'loadNeonRoom':True,'experience':self.eduardoStats.getExperience(),'maxExperience':self.eduardoStats.getMaxExperience()}
                
                
                jsonData = json.dumps(self.dictStats)


                home=os.getenv("HOME")
                f = open(home+'/'+'stats.json',"w")           
                f.write(jsonData)
                f.close()
                time.sleep(3)
     

        elif(self.x<=0 and self.dictKeys['room1']=='open'):
            self.dictKeys['straightRoom']='open'
            self.dictKeys['room1']='closed'
            self.crystalShimers=False

            self.matrix=self.battleEnvironment.createFieldMatrixStraightRoom()
            self.y=172
            self.x=647
        elif(self.x<=0 and self.dictKeys['straightRoom']=='open'):
            self.dictKeys['straightRoom']='closed'
            self.dictKeys['mazeRoom']='open'
            self.matrix=self.battleEnvironment.createFieldMatrixMazeRoom()
            self.crystalShimers=False

            self.dictKeys['room1']='closed'
            self.y=172
            self.x=647
        elif(self.x<=0 and self.dictKeys['mazeRoom']=='open'):
            self.dictKeys['straightRoom']='closed'
            self.dictKeys['mazeRoom']='closed'
            self.dictKeys['straightRoom2']='open'
            self.crystalShimers=False

            self.dictKeys['room1']='closed'
            self.matrix=self.battleEnvironment.createFieldMatrixStraightRoom()
            self.y=172
            self.x=647
        elif(self.x<=0 and self.dictKeys['straightRoom2']=='open'):
            self.dictKeys['straightRoom']='closed'
            self.dictKeys['mazeRoom']='closed'
            self.dictKeys['straightRoom2']='closed'
            self.dictKeys['neonRoom']='open'
            self.crystalShimers=False
      
            self.dictKeys['room1']='closed'
            self.matrix=self.battleEnvironment.createFieldMatrixNeonRoom()
            self.y=172
            self.x=647
        elif(self.x<=0 and self.dictKeys['neonRoom']=='open'):
            self.dictKeys['straightRoom']='closed'
            self.dictKeys['mazeRoom']='closed'
            self.dictKeys['straightRoom2']='closed'
            self.dictKeys['outside']='open'
            self.crystalShimers=False
            self.dictKeys['room1']='closed'
            self.y=172
            self.x=647  
        else:
            self.isSaved=False    


        
#  
        if (((self.x>=0 and self.x<=6)) and self.message1==False and self.getIsMenuRunning()==False):
            self.textMenu.showMessage('I need to get out of here...')
        else:
            self.message1=True    
        if ((self.x>=9 and self.x<=69) and self.message3==False and self.getIsMenuRunning()==False):
            self.textMenu.showMessage('Press A to check purple crystal...')
        elif(self.x>=70):
            self.message3=True   
        if ((self.x>=70 and self.x<145) and self.message2==False and self.getIsMenuRunning()==False):
            self.textMenu.showMessage('But Better prepare myself before I approach it...')
        elif self.message2==True:
            print("")
        elif(self.x>=155):
            self.randomEncounter=random.randint(50,380) 
            self.resetNumberOfSteps()
            self.message2=True    

                    

#                 self.dictStats = {'HP' : self.eduardoStats.getMaxHp(), 'attack' :  self.eduardoStats.getAttack(), 'hit' : self.eduardoStats.getHit()(),
#                         'defense':self.eduardoStats.getMyDefense()}
    def setSavedStats(self):
        home=os.getenv("HOME")
        print(home)
        f = open(home+'/'+'stats.json',)

        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        self.x=500
        self.y=400
        self.eduardoStats.setMaxHp(data['HP'])
        self.eduardoStats.setAttack(data['attack'])
        self.eduardoStats.setHit(data['hit'])
        self.eduardoStats.setDefense(data['defense'])     
        self.eduardoStats.setIsFire2Enabled(data['fire2'])
        self.eduardoStats.setIsFire3Enabled(data['fire3'])
        self.eduardoStats.setLevel(data['level'])
        self.eduardoStats.setMonstersDefeated(data['monstersDefeated'])
        self.storedLRoomState=data['loadLRoom']
        self.storedMazeRoomState=data['loadMazeRoom']
        self.storedNeonRoomState=data['loadNeonRoom']
        self.eduardoStats.setExperience(data['experience'])
        self.eduardoStats.setMaxExperience(data['maxExperience'])
        # Closing file
        f.close()

    def setIsFFOn(self,isFFOn):
        self.isFFOn=isFFOn
    def getIsFFOn(self):
        return self.isFFOn

    def setIsBoss1Running(self,boss1Running):
        self.boss1Running=boss1Running
    def getIsBoss1Running(self):
        return self.boss1Running       
        

    def setDoesCrystalShimer(self,crystalShimers):
        self.crystalShimers=crystalShimers;
    def getIsCrystalShimmering(self):
        return self.crystalShimers

            
    def setIsMenuRunning(self,isMenuRunning):
        self.isMenuRunning=isMenuRunning
    def getIsMenuRunning(self):
        return self.isMenuRunning
    def incrementNumberOfSteps(self):
        self.numberOfSteps=self.numberOfSteps+1
    def getNumberOfSteps(self):
        return self.numberOfSteps
    def resetNumberOfSteps(self):
        self.numberOfSteps=0
    
    def setIsGameRunning(self,isGameRunning):
        self.running=isGameRunning
    def getIsGameRunning(self):
        return self.running
    def setIsBattleRunning(self,isBattleRunning):
        self.battleRunning=isBattleRunning
    def getIsBattleRunning(self):
        return self.battleRunning
