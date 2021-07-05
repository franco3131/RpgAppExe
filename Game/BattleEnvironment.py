'''
Created on Sep 16, 2020

@author: davidfranco
'''

import time

import pygame


class BattleEnvironment:
    def __init__(self,screen):
        self.image=""
        self.screen=screen
        self.isBossRunning=False
        self.matrix=[]
        self.w=650
        self.h=465
        matrix=[] #define empty matrix
        row=[] #Mistake position 
        for i in range(self.w): #total row is 3
            row=[] #Credits for Hassan Tariq for noticing it missing
            for j in range(self.h): #total column is 3
                row.append(0) #adding 0 value for each column for this row
            matrix.append(row)
        self.matrix=matrix
            
       
        
    def renderBattleArena(self,image):
        if(image=="blueCrystalArea"):

            self.bg = pygame.image.load("ff25.png")
            self.screen.blit(self.bg, (0,0))
        elif(image=="LRoom"):
            self.bg = pygame.image.load("LRoom.png")
            self.screen.blit(self.bg, (0,0))   
        elif(image=="straightRoom"):
            self.bg = pygame.image.load("straightRoom.png")
            self.screen.blit(self.bg, (0,0))    
        elif(image=="maze"):
            self.bg = pygame.image.load("mazeRoom.png")
            self.screen.blit(self.bg, (0,0))
        elif(image=="neonRoom"):
            self.bg = pygame.image.load("ff1.png")
            self.screen.blit(self.bg, (0,0))                      


        
    def renderBlackScreen(self):
        BLACK=(0,0,0)
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen,BLACK,(400,450,400,350))
        time.sleep(2)
        
    
    def renderMonster(self,monsterChoice):
        if monsterChoice=="dragon":
            return  pygame.image.load("dragon2.png")
#             self.screen.blit(self.bg, (280,30))
        elif monsterChoice=="monster1":
            return pygame.image.load("monster1.png")
#             self.screen.blit(self.bg, (280,30))
        elif monsterChoice=="monster2":
            return pygame.image.load("monster2.png")
#             self.screen.blit(self.bg, (280,30))
        elif monsterChoice=="monster3":
            return pygame.image.load("monster2.png")
#             self.screen.blit(self.bg, (280,30))
        elif monsterChoice=="monster4":
            return pygame.image.load("dragon2.png")
#             self.screen.blit(self.bg, (280,30))
        elif monsterChoice=="boss1":
            return pygame.image.load("boss1.png")
        elif monsterChoice=="ben":
            return pygame.image.load("benDown11.png")
        elif monsterChoice=="greenDragon":
            return pygame.image.load("greenDragon.png")
        elif monsterChoice=="wizard":
            return pygame.image.load("wizard.png")
        elif monsterChoice=="blueWoman":
            return pygame.image.load("blueWoman.png")    
        elif monsterChoice=="boss2":
            return pygame.image.load("angel.png") 
        elif monsterChoice=="easyMonster":
            return  pygame.image.load("dragon2.png")
        elif monsterChoice=="easyMonster2":
            return  pygame.image.load("dragon2.png")   
        elif monsterChoice=="ben":
            return pygame.image.load("benDown11.png")        


            

    def createFieldMatrix(self):
        print("hiiiii")

        matrix = self.matrix
        print(matrix)
        
        for x in range(0, 36):
            for y in range(278,418):
                matrix[x][y]=1
        for x in range(0,84):
            for y in range (326,368):
                matrix[x][y]=1
        for x in range(0,135):
            for y in range(368,418):
                matrix[x][y]=1
                
                
        for x in range(192,465):
            for y in range(89,152):
                matrix[x][y]=1
        for x in range(348,465):
            for y in range(152,275):
                matrix[x][y]=1
        for x in range(192,326):
            for y in range(152,275):
                matrix[x][y]=1
                
                
        for x in range(0,30):
            for y in range(0,125):
                matrix[x][y]=1
        for x in range(30,117):
            for y in range(0,83):
                matrix[x][y]=1
                
                
        for x in range(549,650):
            for y in range(0,77):
                matrix[x][y]=1
        for x in range(531,597):
            for y in range(374,418):
                matrix[x][y]=1
        for x in range(576,639):
            for y in range(323,418):
                matrix[x][y]=1                 
        for x in range(636,650):
            for y in range(284,418):
                matrix[x][y]=1                            
            
     
        
        
        return matrix
    
    def createFieldMatrixLRoom(self):
        print("hiiiii")
        matrix=self.matrix
        for x in range(0, 350):
            for y in range(127,423):
                matrix[x][y]=1
        for x in range(0,650):
            for y in range (0,0):
                matrix[x][y]=1
        for x in range(521,647):
            for y in range(0,423):
                matrix[x][y]=1
                
                       
            
     
        
        
        return matrix
    
        
    def createFieldMatrixStraightRoom(self):
        print("hiiiii")
        matrix=self.matrix
        for x in range(0, 650):
            for y in range(0,106):
                matrix[x][y]=1
        for x in range(0,650):
            for y in range (229,423):
                matrix[x][y]=1
        return matrix

                
    def createFieldMatrixMazeRoom(self):
        matrix=self.matrix
        for x in range(353, 650):
            for y in range(298,423):
                matrix[x][y]=1
        for x in range(458,545):
            for y in range (25,423):
                matrix[x][y]=1
        for x in range(0,359):
            for y in range (367,423):
                matrix[x][y]=1
        for x in range(323,401):
            for y in range (0,265):
                matrix[x][y]=1
        for x in range(212,287):
            for y in range (34,423):
                matrix[x][y]=1
        for x in range(77,161):
            for y in range (0,315):
                matrix[x][y]=1
        for x in range(0,650):
            for y in range (0,0):
                matrix[x][y]=1
        for x in range(0,35):
            for y in range (85,423):
                matrix[x][y]=1
        return matrix
    def createFieldMatrixNeonRoom(self):
        matrix=self.matrix
        for x in range(461, 650):
            for y in range(0,121):
                matrix[x][y]=1
        for x in range(461, 650):
            for y in range(0,121):
                matrix[x][y]=1
        for x in range(0, 161):
            for y in range(0,423):
                matrix[x][y]=1
        for x in range(368, 458):
            for y in range(0,76):
                matrix[x][y]=1            
        for x in range(0, 650):
            for y in range(0,1):
                matrix[x][y]=1      
        for x in range(0, 149):
            for y in range(0,423):
                matrix[x][y]=1  
        for x in range(0, 650):
            for y in range(370,423):
                matrix[x][y]=1               
        for x in range(578, 650):
            for y in range(301,423):
                matrix[x][y]=1           
        return matrix

    
    def setIsBossRunning(self,isBossRunning):
        self.isBossRunning=isBossRunning
    def getIsBossRunning(self):
        return self.isBossRunning
            
            
        