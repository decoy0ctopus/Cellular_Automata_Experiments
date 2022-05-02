GRID_W = 41
GRID_H = 41
generation = 0
from random import choice

def setup():
    global cellList, SZ
    size(600,600)
    SZ = width // GRID_W+1 
    cellList = createCellList()

def draw():
    global generation, cellList
    frameRate(10)
    cellList = update_list(cellList)
    for row in cellList:
        for cell in row:
            cell.state = cell.update_state()
            cell.display()
    generation += 1
    if generation == 300:
        generation = 0
        cellList = createCellList()
            
            
class Cell:
    def __init__(self, c, r, state=0):
        '''How to initialize a cell'''
        self.c = c
        self.r = r
        self.state = state

    def display(self):
        noStroke()
        if self.state == 1:
            fill(0) #white
        else:
            fill(255) #black
        rect(SZ*self.r,SZ*self.c,SZ,SZ)
        
    def update_state(self):
        neighbs = 0
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            try:
                if cellList[self.r+dr][self.c+dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if self.state ==1:
            if neighbs in [2, 3]:
                return 1
            else:
                return 0
        else:
            if neighbs == 3:
                return 1
            else:
                return 0

        
def update_list(cellList):
    newList = []
    for r,row in enumerate(cellList):
        newList.append([])
        for c,cell in enumerate(row):
            newList[r].append(Cell( c, r, cell.update_state()))
    return newList[::]
        
            
            
        
def createCellList():
    '''Creates a big list of off cells with
    one on Cell in the center'''
    newList=[]#empty list for cells
    #populate the initial cell list
    for j in range(GRID_H):
        newList.append([]) #add empty row
        for i in range(GRID_W):
            newList[j].append(Cell(i,j, choice([0, 1]))) #add off Cells or zeroes
    #center cell is set to on
    newList [GRID_H//2][GRID_W//2].state = 1
    return newList
