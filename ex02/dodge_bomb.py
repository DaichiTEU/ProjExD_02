import sys
import pygame as pg
import random

delta = {
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,+5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(+5,0)
}

WIDTH, HEIGHT = 1600, 900

def out_of_range(rct: pg.Rect):
    width = True
    height = True
    if rct.left <0 or WIDTH < rct.right:
        width = False
    if rct.top <0 or HEIGHT < rct.bottom:
        height = False
    
    return width,height

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_right = pg.transform.flip(kk_img,True,False)
    kk_img_rightup = pg.transform.rotozoom(kk_img_right,45,1.0)
    kk_img_up = pg.transform.rotozoom(kk_img_right,90,1.0)
    kk_img_rightdown = pg.transform.rotozoom(kk_img_right,-45,1.0)
    kk_img_down = pg.transform.rotozoom(kk_img_right,-90,1.0)
    kk_img_leftup = pg.transform.rotozoom(kk_img,-45,1.0)
    kk_img_leftdown = pg.transform.rotozoom(kk_img,45,1.0)
    kk_img_gameover = pg.image.load("ex02/fig/8.png")
    kk_img_gameover = pg.transform.rotozoom(kk_img_gameover,0,2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400
    rb_img = pg.Surface((20, 20))
    rb_imgs = ()
    pg.draw.circle(rb_img, (255, 0, 0), (10, 10), 10)
    rb_img.set_colorkey((0, 0, 0))
    rb_rct = rb_img.get_rect()
    rb_rct.centerx = random.randint(0,900)
    rb_rct.centery = random.randint(0,400)
    vx = +5
    vy = +5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0,0]
        for k,tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]

        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        if out_of_range(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])

        if (sum_mv[0]==0)and(sum_mv[1]==-5):
            screen.blit(kk_img_up,kk_rct)
        elif (sum_mv[0]==0)and(sum_mv[1]==5):
            screen.blit(kk_img_down,kk_rct)
        elif (sum_mv[0]==5)and(sum_mv[1]==0):
            screen.blit(kk_img_right,kk_rct)
        elif (sum_mv[0]==-5)and(sum_mv[1]==0):
            screen.blit(kk_img,kk_rct)
        elif (sum_mv[0]==5)and(sum_mv[1]==-5):
            screen.blit(kk_img_rightup,kk_rct)
        elif (sum_mv[0]==5)and(sum_mv[1]==5):
            screen.blit(kk_img_rightdown,kk_rct)
        elif (sum_mv[0]==-5)and(sum_mv[1]==-5):
            screen.blit(kk_img_leftup,kk_rct)
        elif (sum_mv[0]==-5)and(sum_mv[1]==5):
            screen.blit(kk_img_leftdown,kk_rct)
        else:
            screen.blit(kk_img,kk_rct)

        rb_rct.move_ip((vx,vy))

        accs = [a for a in range(1,11)]
        vx,vy = vx*accs[min(tmr//500,9)],vy*accs[min(tmr//500,9)]

        width ,height = out_of_range(rb_rct)
        if not width:
            vx *= -1
        if not height:
            vy *= -1
        screen.blit(rb_img, [rb_rct.centerx,rb_rct.centery])

        if kk_rct.colliderect(rb_rct):

            screen.blit(kk_img_gameover,kk_rct)
            vx = 0
            vy = 0
            

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()