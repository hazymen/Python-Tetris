
import tkinter as tk,copy,random as rd
grid_list_1=[[0 for a in range(10)]for b in range(20)]
grid_list_2,grid_list_3 = copy.deepcopy(grid_list_1),copy.deepcopy(grid_list_1)
block_list=["1aba0b3bab2ba","1abababa","1aba0ba3bax","1aba0b3bba2ba","3aba0b1bba2ba"]
keyevent_list=[["Up","Left","Right"],[0,1,1],[1,-1,1]]
key = [0,0]
block_rotation = 0
block_y = 0
block_x = 0
land = False
out = False
point = 0
block_number = rd.randint(0,len(block_list)-1)
def draw(l,y,x,n):
    global block_rotation,grid_list_1,grid_list_2,block_y,block_x,key,land,out,block_number
    l_ = copy.deepcopy(l)
    x1 = x
    y1 = y
    out = False
    land = False
    v = [[1,0],[0,1],[-1,0],[0,-1]]
    v1 = [1,0]
    for i in block_list[n]:
        if i=="a":
            if x1>=10 or x1 < 0 or l_[y1][x1]==2:
                out=True
                break
            if y1>=19 or (l_[y1 + 1][x1] == 2)and not out:
                land=True
            l_[y1][x1]=1
        elif i=="b":
            y1-=v1[0]
            x1+=v1[1]
        elif "x" in block_list[n]and i != "x":
            v1=v[int(i)]
        elif i != "x":
            v1=v[(int(i)+block_rotation)%4]
    if out:
        block_y-=1
        block_x+=key[1]*-1
        return grid_list_2
    if land:
        block_y = 0
        block_x = 5
        grid_list_1 = [[2 if x==1 else x for x in row] for row in l_]
        block_rotation = 0
        block_number = rd.randint(0,len(block_list)-1)
    grid_list_2=copy.deepcopy(l_)
    return grid_list_2
def print_grid_list_1(l):
    return "\n".join(" ".join("□" if x==0 else "■" if x in (1,2) else str(x) for x in row) for row in l) + "\n"
def key_press(event):
    if event.keysym in keyevent_list[0]:
        x=keyevent_list[0].index(event.keysym)
        key[keyevent_list[1][x]]=keyevent_list[2][x]
def grid_list_3loop():
    global block_y,block_x,key,block_rotation,grid_list_1,point,grid_list_3
    block_rotation+=key[0]
    block_x+=key[1]
    block_y+=1
    grid_list_3=draw(grid_list_1,block_y,block_x,block_number)
    key[0]=0
    key[1]=0
    lb1["text"]=print_grid_list_1(grid_list_3)
    for i in range(20):
        l=[i for i in grid_list_3]
        if l[i]==[2 for _ in range(10)]:
            point += 1
            grid_list_1.pop(i)
            grid_list_1.insert(0,[0 for _ in range(10)])        
    lb2["text"]=str(point)
    root.after(400, grid_list_3loop)
root=tk.Tk()
root.geometry("200x400")
root.bind("<KeyPress>",key_press)
root.after(800, grid_list_3loop)
lb1=tk.Label(root,width=20,height=22)
lb1.pack()
lb2=tk.Label(root,width=5,height=5)
lb2.pack()
root.mainloop()