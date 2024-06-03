import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for key,value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self,n):
        rlist=[]
        if n > len(self.contents):
            return self.contents
        for _ in range(n):
            r_i=random.randrange(len(self.contents))
            p_e = self.contents.pop(r_i)
            rlist.append(p_e)
        return rlist
       
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    
    for each in range(num_experiments):
        newdict={}
        for i in expected_balls:
            newdict[i]=0
        newhat=copy.deepcopy(hat)
        checklist=newhat.draw(num_balls_drawn)
        for i in checklist:
            if i in newdict:
                newdict[i]+=1
        flag=False
        for i in expected_balls:
            if newdict[i]>=expected_balls[i]:
                flag=True
            else:
                flag=False
                break
        if flag==True:
            count+=1
    return count/num_experiments
hat = Hat(black=6, red=4, green=3)
print(experiment(hat=hat,
                 expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000))