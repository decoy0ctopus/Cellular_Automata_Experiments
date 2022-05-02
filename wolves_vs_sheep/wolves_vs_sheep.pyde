WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)

patchsize = 10
sheepsize = 40
size_wolf = 40
no_sheep = 100
no_wolves = 4
width = 1000
height = 800

def sex_decider():
    if (random(0, 1)) >=  0.5:
        return 'male'
    else:
        return 'female'


def setup():
    size(width, height)
    for i in range(no_sheep):
        sex = sex_decider()
        Sheep_Herd.append(Sheep(random(width), random(height), sheepsize, 10, sex))
    for j in range(0, width, patchsize):
        for k in range(0, height, patchsize):
            Field.append(Grass(j, k, patchsize))
    for i in range(no_wolves):
        sex = sex_decider()
        Wolfpack.append(Wolf(random(width), random(height), size_wolf, 10, sex))

            

def draw():
    background(color(255, 255, 255)) #black
    for grass in Field:
        grass.update()
    for sheep in Sheep_Herd:
        sheep.update()
    for wolf in Wolfpack:
        wolf.update()
    
Sheep_Herd=[] #empty list to put the sheep in

Field=[] # empty list to put grass in

Wolfpack = []

class Sheep:
    def __init__(self,x,y, size_sheep, move_dist, sex):
        '''How to initialize a Sheep'''
        self.xcor = x
        self.ycor = y
        self.size_sheep = size_sheep
        self.move_dist = move_dist
        self.energy = 200
        self.age = 0
        self.sex = sex
        self.sheep_img = loadImage("sheep.png")
        
    def update(self):
        if self.energy > 0:
            self.xcor += random(-self.move_dist, self.move_dist)
            self.ycor += random(-self.move_dist, self.move_dist)
            self.energy -= 1
        else:
            print("Sheep has died of hunger: "+str(len(Sheep_Herd))+" remaining")
            Sheep_Herd.remove(self)
            return
        if self.xcor >= width:
            self.xcor = width-15
        elif self.xcor <= 0:
            self.xcor = 15
        if self.ycor >= height:
            self.ycor = height-15
        elif self.ycor <= 0:
            self.ycor = 15
        grass = Field[int(self.xcor/patchsize) * (height/patchsize) + int(self.ycor/patchsize)]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
            grass.energy = 0
        if (self.age > 20) & (self.energy > 50) & (self.sex == 'female'):
            sex = sex_decider()
            Sheep_Herd.append(Sheep(random(width), random(height), sheepsize, 10, sex))
            print("Sheep has given birth to a: " + sex + " there are now: " + str(len(Sheep_Herd)) + " remaining")
            self.energy -= 30

        if self.age >= random(40, 120):
            print("Sheep has died at age: " + str(self.age) + " there are: " + str(len(Sheep_Herd)) + " remaining")
            Sheep_Herd.remove(self)
            return
        else:
            self.age += 0.1
            
            
        
        stroke(PURPLE)
        fill(WHITE)
        image(self.sheep_img, self.xcor, self.ycor, self.size_sheep, self.size_sheep)
        #ellipse(self.xcor, self.ycor, self.size_sheep, self.size_sheep)
        
class Wolf:
    def __init__(self,x,y, size_wolf, move_dist, sex):
        '''How to initialize a Wolf'''
        self.xcor = x
        self.ycor = y
        self.size_wolf = size_wolf
        self.move_dist = move_dist
        self.energy = 2000
        self.age = 0
        self.sex = sex
        self.wolf_img = loadImage("wolf.png")
        
    def update(self):
        if self.energy > 0:
            self.xcor += random(-self.move_dist, self.move_dist)
            self.ycor += random(-self.move_dist, self.move_dist)
            self.energy -= 10
        else:
            print("Wolf has died of hunger: "+str(len(Wolfpack))+" wolves remaining")
            Wolfpack.remove(self)
            return
        if self.xcor >= width:
            self.xcor = width-15
        elif self.xcor <= 0:
            self.xcor = 15
        if self.ycor >= height:
            self.ycor = height-15
        elif self.ycor <= 0:
            self.ycor = 15
        if (len(Wolfpack)) < (len(Sheep_Herd)*0.1) :
            self.energy += 200
            Sheep_Herd.remove(Sheep_Herd[0])
            print("Sheep has been eaten by wolf, there are: " + str(len(Sheep_Herd)) + " remaining")
        if (self.age > 20) & (self.energy > 500) & (self.sex == 'female') & (random(0, 1) > 0.4):
            sex = sex_decider()
            Wolfpack.append(Wolf(random(width), random(height), size_wolf, 10, sex))
            print("Wolf has given birth to a: " + sex + " there are now: " + str(len(Wolfpack)) + " remaining")
            self.energy -= 400

        if self.age >= random(40, 120):
            print("Wolf has died at age: " + str(self.age) + " there are: " + str(len(Wolfpack)) + " remaining")
            Wolfpack.remove(self)
            return
        else:
            self.age += 0.1
        fill(PURPLE)
        image(self.wolf_img, self.xcor, self.ycor, self.size_wolf, self.size_wolf)
        
class Grass:
    def __init__(self,x,y,patchsize):
        self.x = x
        self.y = y
        self.energy = 3 #energy from eating this patch
        self.eaten = False #hasn't been eaten yet
        self.sz = patchsize

    def update(self):
        if self.energy >= 1.5:
            self.eaten = False
        if self.eaten == False:
            stroke(GREEN)
            fill(GREEN)
        else:
            stroke(BROWN)
            fill(BROWN)
            self.energy += 0.01
        rect(self.x,self.y,self.sz,self.sz)
        
class Wolf:
    def __init__(self,x,y, size_wolf, move_dist, sex):
        '''How to initialize a Wolf'''
        self.xcor = x
        self.ycor = y
        self.size_wolf = size_wolf
        self.move_dist = move_dist
        self.energy = 2000
        self.age = 0
        self.sex = sex
        self.wolf_img = loadImage("wolf.png")
        
    def update(self):
        if self.energy > 0:
            self.xcor += random(-self.move_dist, self.move_dist)
            self.ycor += random(-self.move_dist, self.move_dist)
            self.energy -= 10
        else:
            print("Wolf has died of hunger: "+str(len(Wolfpack))+" wolves remaining")
            Wolfpack.remove(self)
            return
        if self.xcor >= width:
            self.xcor = width-15
        elif self.xcor <= 0:
            self.xcor = 15
        if self.ycor >= height:
            self.ycor = height-15
        elif self.ycor <= 0:
            self.ycor = 15
        if (len(Wolfpack)) < (len(Sheep_Herd)*0.1) :
            self.energy += 200
            Sheep_Herd.remove(Sheep_Herd[0])
            print("Sheep has been eaten by wolf, there are: " + str(len(Sheep_Herd)) + " remaining")
        if (self.age > 20) & (self.energy > 500) & (self.sex == 'female') & (random(0, 1) > 0.4):
            sex = sex_decider()
            Wolfpack.append(Wolf(random(width), random(height), size_wolf, 10, sex))
            print("Wolf has given birth to a: " + sex + " there are now: " + str(len(Wolfpack)) + " remaining")
            self.energy -= 400

        if self.age >= random(40, 120):
            print("Wolf has died at age: " + str(self.age) + " there are: " + str(len(Wolfpack)) + " remaining")
            Wolfpack.remove(self)
            return
        else:
            self.age += 0.1
        fill(PURPLE)
        image(self.wolf_img, self.xcor, self.ycor, self.size_wolf, self.size_wolf)
    
        
