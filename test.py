
import tkinter as tk,copy
l1=[[0 for a in range(10)]for b in range(20)]
l2,l3 = copy.deepcopy(l1),copy.deepcopy(l1)
#a=ブロック,b=1マス進む,（数字は向き（度））1=90,2=180,3=270
block=["1aba0b3bab2ba"]
key = [0,0,0]
rot = 0
blY = 0
blX = 5
blX2 = 0
land = False
out = False
point = 0
def draw(l,y,x,n):
    global rot,l1,l2,blY,blX,key,land,out
    l_ = copy.deepcopy(l)
    b = block[n]
    x1=x
    y1=y
    out = False
    land = False
    v = [[1,0],[0,1],[-1,0],[0,-1]]
    v1 = [1,0]
    for i in b:
        if i == "a":
            if x1 >= 10:
                blX -= 1
                out = True
                break
            if x1 < 0:
                blX += 1
                out = True
                break
            if y1 + 1 >= 20 or (l_[y1 + 1][x1] == 2)and not out:
                land = True
            l_[y1][x1]=1
        elif i == "b":
            y1 -= v1[0]
            x1 += v1[1]
        else:v1=v[(int(i)+rot)%4]
    if out:
        blY -= 1
        return l2
    if land:
        blY = 0;blX=5;l1 = [[2 if x == 1 else x for x in row] for row in l_]
    l2 = copy.deepcopy(l_)
    return l_
def print_l1(l,a):
    l1 = [["■" if x == 1 or x == 2 else x for x in row] for row in l]
    l1 = [["□" if x == 0 else x for x in row] for row in l1]
    for i in l1:
        l2 = " ".join(i)
        print(l2,blY,sum(i.count(1) for i in l1),blX,point,a)
def key_press(event):
    if event.keysym=="Up":key[0] = 1
    elif event.keysym=="Left":key[1] = -1
    elif event.keysym=="Right":key[1] = 1
    elif event.keysym=="Down"and blY != 18:key[2] = 1
def l3loop():
    global blY,blX,key,rot,l1,point,l3
    rot += key[0];key[0]=0
    blX += key[1];key[1]=0
    blY += 1+key[2];key[2]=0
    l3 = draw(l1,blY,blX,0)
    print_l1(l3,len(l3))
    for i in range(20):
        l = [i for i in l3]
        if l[i] == [2 for _ in range(10)]:
            point += 1
            l1.pop(i)
            l1.insert(0,[0 for _ in range(10)])        
    root.after(400, l3loop)
root = tk.Tk()
root.bind("<KeyPress>",key_press)
root.after(800, l3loop)
root.mainloop()
