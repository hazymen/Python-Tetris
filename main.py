import tkinter as t,random as r
class Tetris:
    def __init__(s):
        s.w=t.Tk();w,h=350,600;sw,sh=s.w.winfo_screenwidth(),s.w.winfo_screenheight()
        s.w.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}");s.w.resizable(0,0)
        s.wd,s.ht,s.sz=10,20,25; s.bd=[[0 for _ in range(s.wd)]for _ in range(s.ht)]
        s.cv=t.Canvas(s.w,width=250,height=500,bg="black"); s.cv.pack(pady=20)
        s.sh=[[[[1,1,1,1]]],[[[1,1],[1,1]]],[[[0,1,0],[1,1,1]]],[[[1,0,0],[1,1,1]]],[[[0,0,1],[1,1,1]]],[[[0,1,1],[1,1,0]]],[[[1,1,0],[0,1,1]]]]; s.c='gray'
        s.p,s.x,s.y,s.k,s.rt=None,0,0,0,0; s.sc=0; s.go=0
        s.scl=t.Label(s.w,text=f"スコア: {s.sc}",font=("Arial",16)); s.scl.pack()
        s.w.bind("<KeyPress>",s.on_key_press); s.w.focus_set(); s.spawn_piece(); s.game_loop()
    def spawn_piece(s):s.k,s.rt=r.randint(0,6),0; s.p=s.sh[s.k][s.rt]; s.x=s.wd//2-len(s.p[0])//2; s.y=0; s.go=s.check_collision(s.x,s.y,s.p) or 0
    def check_collision(s,x,y,p):
        for py,rw in enumerate(p):
            for px,c in enumerate(rw):
                if c:
                    nx,ny=x+px,y+py
                    if nx<0 or nx>=s.wd or ny>=s.ht:return 1
                    if ny>=0 and s.bd[ny][nx]:return 1
        return 0
    def place_piece(s):[s.bd.__setitem__(s.y+py,[s.bd[s.y+py][i] if not(c and i==s.x+px) else s.k+1 for i in range(s.wd)]) for py,rw in enumerate(s.p) for px,c in enumerate(rw) if c and s.y+py>=0]; s.clear_lines();s.spawn_piece()
    def clear_lines(s):
        lc=0;y=s.ht-1
        while y>=0:
            if all(s.bd[y]):del s.bd[y];s.bd.insert(0,[0 for _ in range(s.wd)]);lc+=1
            else:y-=1
        if lc>0:s.sc+=lc*100; s.scl.config(text=f"スコア: {s.sc}")
    def rotate_piece(s):
        if s.k==1:return
        p=s.p;rot=[[p[j][len(p[0])-1-i]for j in range(len(p))]for i in range(len(p[0]))]
        if not s.check_collision(s.x,s.y,rot):s.p=rot
    def move_piece(s,dx,dy):nx,ny=s.x+dx,s.y+dy;return not s.check_collision(nx,ny,s.p) and not (setattr(s,'x',nx) or setattr(s,'y',ny)) or 0
    def on_key_press(s,e):
        if s.go:return
        if e.keysym=="Left":s.move_piece(-1,0)
        elif e.keysym=="Right":s.move_piece(1,0)
        elif e.keysym=="Down":not s.move_piece(0,1) and s.place_piece()
        elif e.keysym=="Up":s.rotate_piece()
        s.draw()
    def draw(s):s.cv.delete("all");[s.cv.create_rectangle(x*s.sz,y*s.sz,(x+1)*s.sz,(y+1)*s.sz,fill=s.c,outline="white") for y in range(s.ht) for x in range(s.wd) if s.bd[y][x]];[s.cv.create_rectangle((s.x+px)*s.sz,(s.y+py)*s.sz,(s.x+px+1)*s.sz,(s.y+py+1)*s.sz,fill=s.c,outline="white") for py,rw in enumerate(s.p) for px,cell in enumerate(rw) if cell and not s.go and s.y+py>=0];s.go and s.cv.create_text(s.wd*s.sz//2,s.ht*s.sz//2,text="GAME OVER",fill="red",font=("Arial",20))
    def game_loop(s):not s.go and (not s.move_piece(0,1) and s.place_piece(),s.draw(),s.w.after(800,s.game_loop))
    def run(s):s.draw();s.w.mainloop()
    def run(s):
        s.draw();s.w.mainloop()
if __name__=="__main__":Tetris().run()