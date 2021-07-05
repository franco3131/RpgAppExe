
import time

from pygame import mixer

import pygame

from Game.MoveDrawing import MoveDrawing
from Game.Stats import Stats

import os


class gameRpg:
    def __init__(self):


        pygame.mixer.quit()
        mixer.init() 
        pygame.init()
#frequency, size, channels, buffersize
#         pygame.init()
#         pygame.mixer.pre_init(44100, 16, 2, 4096) 
#         waterWorld = pygame.mixer.Sound("Waterworld - Map.mp3")
        mixer.music.load("Waterworld - Map.mp3")
        mixer.music.play(-1)  
        pygame.font.init()
        self.screen = pygame.display.set_mode((700,480))
        self.screen.fill([255, 255, 255])
        
        self.eduardoStats='null';
#         self.font = pygame.font.Font(pygame.font.get_default_font(),25)

        self.font = pygame.font.SysFont('Verdana', 25)
#         mixer.music.load("Music/Waterworld - Map.mp3") 
#         mixer.music.set_volume(2.0) 
#         mixer.music.play(-1)   
        self.bg = pygame.image.load("bricks.png")
        self.screen.blit(self.bg, (0,0))


    def runGame(self):
        #instantiate the objects and move them

        continueLoop=True
        LoadGame=False
  
        while continueLoop:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Cursor Move.wav'), maxtime=600)
                time.sleep(1)
                effect = pygame.mixer.Sound('Cursor Move.wav')
                effect.play()

                continueLoop=False  
                self.screen.fill((0,0,0))
            
            if keys[pygame.K_l]:



                effect = pygame.mixer.Sound('load.wav')
                effect.play()
                continueLoop=False  
                self.screen.fill((0,0,0))
                
                LoadGame=True
                time.sleep(1)



            else:

                BLUE=(8, 143, 143)
                pygame.draw.rect(self.screen,BLUE,(0,0,700,50))
#                 text = self.font.render('Press Return', True, (255,255,255))
                self.attack= self.font.render('Press Return', False, (255,255,255))
                self.screen.blit(self.attack,(4,20))
                pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,0,700,50), 8)

                try:

                    home=os.getenv("HOME")
                    print(home)
                    f = open(home+'/'+'stats.json',)
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,50,700,50), 8)   
                    pygame.draw.rect(self.screen,BLUE,(0,50,700,50))
                    self.save= self.font.render('Press l for load game', False, (255,255,255))
                    self.screen.blit(self.save,(4,70))
                except:
                    print("not found")
            
                
                pygame.display.update()
                pygame.event.pump()
                
        loops=0
        
        while loops<30:
            self.screen.fill((0,0,0))  
            loops=loops+1  
  
            pygame.display.update()
            pygame.event.pump()
 
    
                 
        mixer.quit()
 
        self.eduardoStats=Stats(155,5,3,3,8,0)
        game=MoveDrawing(self.screen,self.eduardoStats)    
        if LoadGame==True:
            game.setSavedStats()           
            
        game.initializeMatrix()
        
        self.initializeLRoom=False
        mixer.init() 
#         pygame.mixer.pre_init(44100, 16, 2, 4096) 
        mixer.music.load("Fate In Haze.mp3")
        mixer.music.play(-1)  

#         mixer.music.load("Music/Fate In Haze.mp3") 
#         mixer.music.set_volume(2.0) 
#         mixer.music.play(-1)  
        while game.getIsGameRunning():

            game.MoveBenjamin()
            game.showMessageByLocation()
            game.moveMenuHand()
            game.moveBattleCursor()
            pygame.display.flip()
            pygame.display.update()
            if game.getIsFFOn()==False:
                time.sleep(0.025)
            else:
                print("nothing")
                time.sleep(0.0)

            if game.dictKeys['room1']=='open':
                if self.initializeLRoom==False:
                    game.lRoomMatrix()
                    self.initializeLRoom=True


  
                
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
# 
#     return os.path.join(base_path, relative_path)
# 
# 
# 
# img1 = resource_path("angel.png")
# img2 = resource_path("attackedLeftFoot.png")
# img3 = resource_path("attackedRightFoot.png")
# img4 = resource_path("benDown11.png")
# img5 = resource_path("benDown11.png")
# img6 = resource_path("benDown12.png")
# img7 = resource_path("benHead2.png")
# img8 = resource_path("benLeft12.png")
# img9 = resource_path("benLeft31.png")
# img10 = resource_path("benRight12.png")
# img11= resource_path("benRight31.png")
# img12 = resource_path("blueCrystal.png")
# img13 = resource_path("blueFireBall.png")
# img14= resource_path("blueWoman.png")
# img14 = resource_path("boss1.png")
# img15 = resource_path("bricks.png")
# img16 = resource_path("brownDoor.png")
# img17 = resource_path("brownDoor4.png")
# img18 = resource_path("crystal.png")
# img19 = resource_path("door.png")
# img20= resource_path("dragon.png")
# img21= resource_path("dragon2.png")
# img22= resource_path("ff1.png")
# img23= resource_path("ff2.png")
# img24 = resource_path("ff25.png")
# img25 = resource_path("ff3.png")
# img26 = resource_path("ff4.png")
# img27 = resource_path("fire1.pngg")
# img28 = resource_path("fire2.png")
# img29 = resource_path("fireball.png")
# img30= resource_path("fireball2.png")
# img31= resource_path("fireball3.png")
# img32= resource_path("floorArea.png")
# img33 = resource_path("greenDragon.png")
# img34 = resource_path("hand3.png")
# img35 = resource_path("leftFoot22.png")
# img36 = resource_path("mazeRoom.png")
# img37 = resource_path("monster1.png")
# img38 = resource_path("monster2.png")
# img39 = resource_path("neon2.png")
# img40 = resource_path("neon3.png")
# img41 = resource_path("neon4.png")
# img42 = resource_path("neon5.png")
# img43 = resource_path("straightRoom.png")
# img44 = resource_path("sword1.png")
# img45 = resource_path("sword2.png")
# img46 = resource_path("sword3.png")
# img47 = resource_path("upRightFoot.png")
# img48 = resource_path("wizard.png")







                    
            
  


              
