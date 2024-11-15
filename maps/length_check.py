
def get_maze(l): # converts maze txt into array
    lister = []
    temp_row=[]
    txt = open(l,'r')
    content = txt.readlines()
    txt.close()
    for row in content:
        for item in row:
            temp_row.append(item)
        temp_row.pop(-1)
        lister.append(temp_row)
        temp_row = []
    
    return lister




red = get_maze("map3.txt")

print(len(red))

print(len(red[0])     )

for row in red:
    print(row)