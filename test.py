import pygame as pg, sys
pg.init() #初期化するという意味
screen = pg.display.set_mode((800,600)) #画面を作る設定　横、縦
img1 = pg.image.load("images/car.png")
img1=pg.transform.scale(img1,(50,50))

while True:
    screen.fill(pg.Color("WHITE"))
    screen.blit(img1,(100,100))
    pg.draw.rect(screen, pg.Color("RED"),(100,100,100,150))
    pg.draw.line(screen, pg.Color("BLUE"),(250,100),(350,250),5)
    pg.draw.ellipse(screen, pg.Color("GREEN"),(400,100,150,150),5)
    pg.display.update() #画面を更新し、描画した内容を表示します。
    for event in pg.event.get():   #ユーザーがウィンドウを閉じる操作を行った（QUITイベントが発生した）場合に、Pygameを終了し、プログラムも終了します。
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            