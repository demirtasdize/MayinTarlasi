import random
mine = random.randint(5,30)

grid = [[0 for x in range(9)] for y in range(9)]
for i in range(mine):
    minesrow = random.randint(0,8)
    minescol = random.randint(0,8)
    grid[minesrow][minescol] = 1

print(grid)

def count(row,col):
    offsets = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    count = 0
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        if((offset_row>=0 and offset_row<=8) and (offset_col>=0 and offset_col<=8)):
            if grid[offset_row][offset_col] == 1:
                count += 1
    return count
    
    
def click(row, col):
    if grid[row][col] == 1:
        print("BOOM!")
    else :
        print(count(row,col))

deger = False
toplam = 0
while deger == False:
    sutun = int(input("sütun giriniz: "))
    satir = int(input("satir giriniz: "))
    if grid[satir][sutun] == 0:
        toplam = toplam+1
        print(toplam)
    else:
        print("oyun bitti")
        print(toplam)
        deger=True

