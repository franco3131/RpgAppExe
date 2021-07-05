'''
Created on Sep 16, 2020

@author: davidfranco
'''

import pygame


class Environment:
    def __init__(self,screen):
        self.image=""
        pygame.font.init()
        self.screen=screen
        self.temp=0
        self.image1=True
        self.image2=False
        self.image3=False
        self.image4=False
        self.count=0
       
        
    def renderEnvironment(self,image,timer):
        if(image=="blueCrystalArea"):
            self.bg = pygame.image.load("ff25.png")
            self.screen.blit(self.bg, (0,0))
                        
            door = pygame.image.load("brownDoor4.png")
            self.screen.blit(door,(330,-30))
            
            door = pygame.image.load("blueCrystal.png")
            self.screen.blit(door,(500,400))
            
            
            
        elif(image=="LRoom"):
            self.bg = pygame.image.load("LRoom.png")
            self.screen.blit(self.bg, (0,0))
        elif(image=="straightRoom"):
            self.bg = pygame.image.load("straightRoom.png")
            self.screen.blit(self.bg, (0,0))
        elif(image=="maze"):
            self.bg = pygame.image.load("mazeRoom.png")
            self.screen.blit(self.bg, (0,0))
                        
            door = pygame.image.load("blueCrystal.png")
            self.screen.blit(door,(455,256))
            
        elif(image=="straightroom2"):
            self.bg = pygame.image.load("mazeRoom.png")
            self.screen.blit(self.bg, (0,0))
        elif(image=="neonRoom"):

            if self.image1==True:
                self.bg = pygame.image.load("neon2.png")
                self.screen.blit(self.bg, (0,0))
                if self.count<=20:
                    print(self.count)
                    self.image2=True 
                    self.image1=False 
                
            elif self.image2==True:
                self.bg = pygame.image.load("neon3.png")
                self.screen.blit(self.bg, (0,0))  
                if self.count<40 and self.count>20:
                    self.image2=False
                    self.image3=True
                              
            elif self.image3==True:
                self.bg = pygame.image.load("neon4.png")
                self.screen.blit(self.bg, (0,0)) 
                if self.count<60 and self.count>=40:
                    self.image3=False 
                    self.image4=True
            elif self.image4==True:
                self.bg = pygame.image.load("neon5.png")
                self.screen.blit(self.bg, (0,0)) 
                if self.count<80 and self.count>=60:
                    self.image1=True 
                    self.image4=False
                    self.count=0                  
            self.count=self.count+1
            door = pygame.image.load("blueCrystal.png")
            self.screen.blit(door,(455,256))
            
            
    
                                

            
