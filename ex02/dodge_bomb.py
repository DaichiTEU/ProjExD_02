import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    rb_img = pg.Surface((20, 20))
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
        screen.blit(kk_img, [900, 400])
        rb_rct.move_ip((vx,vy))
        screen.blit(rb_img, [rb_rct.centerx,rb_rct.centery])
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()