from random import choice
class Person:
    def __init__(self, name):
        self.name = name
    
class Football(Person):
    count=0
    def __init__(self, name,random_players):
        super().__init__(name)
        self.random_players=random_players
    def get_random(self):
        while self.name!=[]:
            item=choice(self.name)
            self.name.remove(item)
            self.random_players.append(item)
        return(self.random_players)
    def get_team(self,random_players):
        while Football.count!=22:
            for item in self.random_players:
                if Football.count<11:
                    print(item+':A')
                    Football.count+=1
                else:
                    print(item+':B')
                    Football.count+=1
            
name=['hosein','nima','akbar','maziyar','mehdi','farhad','mohamad','khashayar','mohsen','saman','shahrooz','behrooz','soheil','behzad','ali','reza','pouria','puya','saeed','amin','mostafa','milad']
random_players=[]
output = Football(name,random_players)
a=output.get_random()
output.get_team(a)