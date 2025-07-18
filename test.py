
import tkinter as tk,copy,random as rd;l1=[[0 for a in range(10)]for b in range(20)];l2,l3 = copy.deepcopy(l1),copy.deepcopy(l1)
block,keys=["1aba0b3bab2ba","1abababa","1aba0ba3bax"],[["Up","Left","Right"],[0,1,1],[1,-1,1]]
key,rot,blY,blX,land,out,point,bl = [0,0],0,0,5,False,False,0,rd.randint(0,len(block)-1)
def draw(l,y,x,n):
    global rot,l1,l2,blY,blX,key,land,out,bl;l_,x1,y1,out,land,v,v1=copy.deepcopy(l),x,y,False,False,[[1,0],[0,1],[-1,0],[0,-1]],[1,0]
    for i in block[n]:
        if i=="a":
            if x1>=10:blX-=1;out=True;break
            if x1<0:blX+=1;out=True;break
            if y1>=19 or (l_[y1 + 1][x1] == 2)and not out:land=True
            l_[y1][x1]=1
        elif i=="b":y1-=v1[0];x1+=v1[1]
        elif "x" in block[n]and i != "x":v1=v[int(i)]
        elif i != "x":v1=v[(int(i)+rot)%4]
    if out:blY-=1;return l2
    if land:blY,blX,l1,rot,bl=0,5,[[2 if x==1 else x for x in row] for row in l_],0,rd.randint(0,len(block)-1)
    l2=copy.deepcopy(l_);return l2
def print_l1(l):return "\n".join(" ".join("□" if x==0 else "■" if x in (1,2) else str(x) for x in row) for row in l) + "\n"
def key_press(e):x=keys[0].index(e.keysym);key[keys[1][x]]=keys[2][x]
def l3loop():
    global blY,blX,key,rot,l1,point,l3;rot+=key[0];key[0]=0;blX+=key[1];key[1]=0;blY+=1;l3=draw(l1,blY,blX,bl);label["text"]=print_l1(l3)
    for i in range(20):
        l=[i for i in l3]
        if l[i]==[2 for _ in range(10)]:point += 1;l1.pop(i);l1.insert(0,[0 for _ in range(10)])        
    root.after(400, l3loop)
root = tk.Tk();root.geometry("200x400");root.bind("<KeyPress>",key_press);root.after(800, l3loop)
label = tk.Label(root,width=20,height=40);label.pack();root.mainloop()