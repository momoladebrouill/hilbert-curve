import pygame as pg
from pygame.locals import *
pg.init()
f=pg.display.set_mode((500,500))
B=1
fps=pg.time.Clock()
f.fill(0)
size=50
margin=150
pg.draw.line(f,0xffffff,(margin,margin),(margin,500-margin),size)
pg.draw.line(f,0xffffff,(500-margin,margin),(500-margin,500-margin),size)
pg.draw.line(f,0xffffff,(margin-int(size/2),500-margin),(500-margin+int(size/2),500-margin),size)

pg.display.flip()
fps.tick(1)
s=parts=0
pos=[(0,0),(250,0),(0,250),(250,250)]
j=1
margin/=2
 

while B:
    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            B=0
        elif event.type==pg.KEYUP:
            f=pg.display.get_surface()
            s=f.copy()
            s=pg.transform.scale(s,(250,250))
            parts=list([s.copy() for _ in range(4)])
            f.fill(0)
            for i in range(4):
                if pos[i]==(0,0):
                    parts[i]=pg.transform.rotate(parts[i],90)
                elif pos[i]==(250,0):
                    parts[i]=pg.transform.rotate(parts[i],-90)
                f.blit(parts[i],pos[i])
            thickness=round(size/(j*2))
            pg.draw.line(f,0xffffff,(margin/j,250-margin/j-thickness/2),(margin/j,250+margin/j),thickness)
            pg.draw.line(f,0xffffff,(500-margin/j,250-margin/j-thickness/2),(500-margin/j,250+margin/j),thickness)
            pg.draw.line(f,0xffffff,(250-margin/j-thickness/2,250+margin/j),(250+margin/j+thickness/2,250+margin/j),thickness)
            pg.display.flip()
            j*=2
