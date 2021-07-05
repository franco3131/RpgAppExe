'''
Created on Sep 18, 2020

@author: davidfranco
'''

import random



class Stats:
    def __init__(self,hp,defense,hit,evasion,attack,monsterExperience):
        self.Hp=hp
        self.Defense=defense
        self.Hit=hit
        self.Evasion=evasion
        self.Attack=attack
        self.maxHp=hp
        self.damage=0
        self.monsterExperience=monsterExperience
        self.maxExperience=30
        self.experience=0
        self.cure=5
        self.fire=5
        self.escape=3
        self.monstersDefeated=0
        self.isFire2Enabled=False
        self.fire3=False
        self.level=1
        self.defense=3
        
        
    
    def setMyHp(self,hp):
        self.Hp=hp
    def getMyHp(self):
        return self.Hp
    def setMyDefense(self,defense):
        self.Defense=defense
    def getMyDefense(self):
        print(self.Defense)
        return self.Defense
    def setHit(self,hit):
        self.Hit=hit
    def getHit(self):
        return self.Hit
    def setEvasion(self,evasion):
        self.Evasion=evasion
    def getEvasion(self):
        return self.Evasion
    def setAttack(self,attack):
        self.Attack=attack
    def getAttack(self):
        return self.Attack
    def getMaxHp(self):
        return self.maxHp
    def setMaxHp(self,maxHp):
        self.maxHp=maxHp
    def setDamage(self,damage):
        self.damage=damage
        
    def getDamage(self):
        return self.damage
    def setCure(self,cure):
        self.cure=cure
    def getCure(self):
        return self.cure
    def setEscape(self,escape):
        self.escape=escape
    def getEscape(self):
        return self.escape
    def setFire(self,fire):
        self.fire=fire
    def getFire(self):
        return self.fire
    def setExperience(self,monsterExperience):
        self.experience=self.experience+monsterExperience
    def getExperience(self):
        return self.experience
    def getMaxExperience(self):
        return self.maxExperience
    def setMaxExperience(self,maxExperience):
        self.maxExperience=maxExperience
    def increaseMaxExperience(self):
        self.maxExperience=self.maxExperience+30
    def getMonsterExperience(self):
        return self.monsterExperience
    def setMonstersDefeated(self,monstersDefeated):
        self.monstersDefeated=monstersDefeated
    def getMonstersDefeated(self):
        return self.monstersDefeated
    def setIsFire2Enabled(self,isFire2Enabled):
        self.isFire2Enabled=isFire2Enabled
    def getIsFire2Enabled(self):
        return self.isFire2Enabled
    def setIsFire3Enabled(self,fire3):
        self.fire3=fire3
    def getIsFire3Enabled(self):
        return self.fire3
    def setLevel(self,level):
        self.level=level 
    def getLevel(self):
        return self.level
    def setDefense(self,defense):
        self.defense=defense
    def getDefense(self):
        return self.defense
    def calculateAttack(self,otherCharacterDefense):
        attack=1+(self.getHit()/10)
        attack=attack*(self.getAttack())
        attack=attack-(otherCharacterDefense/2)
        self.random=random.randint(0, 12)
        attackMultiplier=[1.1,1.1,1.2,1.2,1.2,1.3,1.3,1.3,1.5,1.5,1.7,1.7,2.0,3.0]
        self.setDamage((attack*attackMultiplier[self.random])+attack)

    
    def calculateDamageAfterDefense(self,monsterAttack,monsterHit):
        attack=1+((monsterHit)/10)
        attack=attack*(monsterAttack)
        attack=attack-(self.getMyDefense()/2)
        self.setDamage(attack)
        return attack 
    def calculateHpAfterAttack(self,attack):
        
        self.setMyHp(self.getMyHp()-attack)
        
 
      
     
        
               
        
    def statsIncreaseLevelUp(self):
        data=["HP","Defense","Hit","Evasion","Attack"]
        self.random=random.randint(0, 4)
        attack=self.getAttack()
        attack=attack+3
        if self.getLevel()>3:
            attack=attack+1
        elif self.getLevel()>10:
            attack=attack+2
        elif self.getLevel()>15:
            attack=attack+3
        elif self.getLevel()>25:
            attack=attack+4
        elif self.getLevel()>40:
            attack=attack+6
        elif self.getLevel()>60:
            attack=attack+9
        elif self.getLevel()>90:
            attack=attack+11
        elif self.getLevel()>100:
            attack=attack+15
        self.setAttack(attack)
        self.maxHp=int(self.getMaxHp()*.10)+self.getMaxHp()
        self.setMyHp(self.maxHp)
        hit=self.getHit()
        hit=hit+5
        self.setHit(hit)
        for x in range(2):
#             if(data[x]=="HP"):
#                 self.maxHp=self.maxHp+20
#                 self.setHp(self.maxHp)
            if(data[x]=="Defense"):
                defense=self.getMyDefense()
                defense=defense+1
                self.setMyDefense(defense)
            elif(data[x]=="Hit"):
                hit=self.getHit()
                hit=hit+1
                self.setHit(hit)
            elif(data[x]=="Evasion"):
                evasion=self.getEvasion()
                evasion=evasion+1
                self.setEvasion(evasion)
#             elif(data[x]=="Attack"):
#                 attack=self.getAttack()
#                 attack=attack+1
#                 self.setAttack(attack)



             
                
    
            
            
            
            
    