'''
Created on Sep 18, 2020

@author: davidfranco
'''
class MonsterStats:
    def __init__(self):
        self.room1=True    
        self.room2=False    
        
    def setMonsterStats(self,monster):
        monsterData=[]

        if monster=="dragon":
            print("monster3")
            hp=80
            monsterData.append(hp)
            defense=5
            monsterData.append(defense)
            hit=3
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=10
            monsterData.append(attack)
            experience=5
            monsterData.append(experience)
            return monsterData
        elif monster=="monster1":
            print("monster3")
            hp=50
            monsterData.append(hp)
            defense=7
            monsterData.append(defense)
            hit=5
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=13
            monsterData.append(attack)
            experience=10
            monsterData.append(experience)
            return monsterData
        elif monster=="monster2":
           # hp,defense,hit,evasion,attack
            hp=10
            monsterData.append(hp)
            defense=6
            monsterData.append(defense)
            hit=8
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=15
            monsterData.append(attack)
            experience=10
            monsterData.append(experience)
            return monsterData
        elif monster=="monster4":
            print("monster3")
            hp=200
            monsterData.append(hp)
            defense=2
            monsterData.append(defense)
            hit=8
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=15
            monsterData.append(attack)
            experience=15
            monsterData.append(experience)
            return monsterData
        elif monster=="monster3":
           # hp,defense,hit,evasion,attack
            print("monster3")
            hp=100

            monsterData.append(hp)
            defense=6
            monsterData.append(defense) 
            hit=9
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=19
            monsterData.append(attack)
            experience=10
            monsterData.append(experience)
            return monsterData
        elif monster=="easyMonster":

            hp=40

            monsterData.append(hp)
            defense=6
            monsterData.append(defense) 
            hit=9
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=16
            monsterData.append(attack)
            experience=10
            monsterData.append(experience)
            return monsterData
        elif monster=="boss1":
            hp=1300
#             hp=10
            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=10
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=16
            monsterData.append(attack)
            experience=100
            monsterData.append(experience)
            return monsterData
        elif monster=="wizard":
            hp=900

            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=15
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=23
            monsterData.append(attack)
            experience=100
            monsterData.append(experience)
            return monsterData
        elif monster=="greenDragon":
            hp=700

            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=20
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=20
            monsterData.append(attack)
            experience=50
            monsterData.append(experience)
            return monsterData
        elif monster=="blueWoman":
            hp=500

            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=10
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=15
            monsterData.append(attack)
            experience=50
            monsterData.append(experience)
            return monsterData
        elif monster=="boss2":
            hp=4000
            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=25
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=40
            monsterData.append(attack)
            experience=100
            monsterData.append(experience)
            return monsterData
        elif monster=="easyMonster2":

            hp=100

            monsterData.append(hp)
            defense=6
            monsterData.append(defense) 
            hit=9
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=19
            monsterData.append(attack)
            experience=10
            monsterData.append(experience)
            return monsterData   
        elif monster=="ben":

            hp=8000

            monsterData.append(hp)
            defense=10
            monsterData.append(defense) 
            hit=14
            monsterData.append(hit)
            evasion=4
            monsterData.append(evasion)
            attack=36
            monsterData.append(attack)
            experience=30
            monsterData.append(experience)
            return monsterData             
  