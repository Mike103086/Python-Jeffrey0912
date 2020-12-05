# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 15:09:48 2020

@author: user
"""

import pygame
from pygame.locals import *
from sys import exit
import time
import random

# 建立子彈類，把子彈的圖片轉化為影象物件，設定固定的移動速度
class Bullet():
    def __init__(self,bulletfilename,bulletpos):
        self.bulletimg = pygame.image.load(bulletfilename)
        self.bullet_rect = self.bulletimg.get_rect()
        self.bullet_image = self.bulletimg.subsurface(self.bullet_rect)
        self.bullet_rect.midbottom = bulletpos
        self.speed = 2
    def move(self):
        self.bullet_rect.top -= self.speed

# 建立玩家飛機類，用面向物件的思想來對待
class play_plane_fly():
    def __init__(self,play_image_filename,play_pos):
        self.image = pygame.image.load(play_image_filename)
        self.plane_rect = self.image.get_rect()
        self.play_image = self.image.subsurface(self.plane_rect)
        self.plane_rect.midtop = play_pos
        self.speed = 2
        # 子彈是由玩家飛機發射的，所以建立列表，儲存子彈物件，使該列表變為該類的屬性
        self.bullets = []
        self.is_hitted = False

    # 生成函式，完成發射子彈動作，同時將每個子彈物件存在列表中
    def shoot(self,bullet_filename):
        bulletobj = Bullet(bullet_filename,self.plane_rect.midtop)
        self.bullets.append(bulletobj)

    # 向上移動，當飛機移動到邊框位置時，無法移動
    def moveup(self):
        if self.plane_rect.top <= 0:
            self.plane_rect.top = 0
        else:
            self.plane_rect.top -= self.speed

    # 向下移動，當飛機移動到邊框位置時，無法移動
    def movedown(self):
        if self.plane_rect.top >= 950 - self.plane_rect.height:
            self.plane_rect.top = 950 - self.plane_rect.height
        else:
            self.plane_rect.top += self.speed

    # 向右移動，當飛機移動到邊框位置時，無法移動
    def moveleft(self):
        if self.plane_rect.left <= -40:
            self.plane_rect.left = -40
        else:
            self.plane_rect.left -= self.speed

    # 向左移動，當飛機移動到邊框位置時，無法移動
    def moveright(self):
        if self.plane_rect.left >= 700 - self.plane_rect.width:
            self.plane_rect.left = 700 - self.plane_rect.width
        else:
            self.plane_rect.left += self.speed

# 生成敵機類，設定固定的移動速度
class Enemy():
    def __init__(self,enemyfilename,enemypos):

        self.img = pygame.image.load(enemyfilename)
        self.enemy_rect = self.img.get_rect()
        self.enemy_image = self.img.subsurface(self.enemy_rect)
        self.enemy_rect.midbottom = enemypos
        self.speed = 1

    def move(self):
        self.enemy_rect.bottom += self.speed

clock = pygame.time.Clock()
def main():
    # 初始化文字螢幕
    pygame.font.init()
    # 初始化影象螢幕
    pygame.init()
    # 設定遊戲幀
    clock.tick(50)
    # 設定遊戲螢幕大小
    screen = pygame.display.set_mode((660,950))
    # 設定遊戲名稱
    pygame.display.set_caption('飛機大戰')
    # 載入背景圖片，生成影象物件
    background = pygame.image.load('image/background.png').convert()
    backgroundsurface = pygame.transform.scale(background, (660, 950))
    # 載入遊戲結束圖片，生成影象物件
    gameover = pygame.image.load('image/gameover.png').convert()
    gameoversurface = pygame.transform.scale(gameover,(660, 950))
    playplanefilename = 'image/myself.png'
    planepos = [330,600]
    player = play_plane_fly(playplanefilename,planepos)
    bulletfilename = 'image/bullet.png'
    # 按頻率生成子彈，初始化數字為0
    bullet_frequency = 0
    enemyfilename = 'image/airplane.png'
    # 按頻率生成敵機，初始化數字為0
    enemy_frequency = 0
    enemys = []
    myfont = pygame.font.SysFont("arial", 40)
    textImage = myfont.render("Score ", True, (0,0,0))
    # 初始化得分為0
    Score = 0
    # 敵機被子彈擊中時的動畫，將每張圖片的影象物件存在列表中
    enenys_down = []
    enemy0_down = pygame.image.load('image/airplane_ember0.png')
    enemy0_down_rect = enemy0_down.get_rect()
    enemydown0 = enemy0_down.subsurface(enemy0_down_rect)
    enenys_down.append(enemydown0)
    enemy1_down = pygame.image.load('image/airplane_ember1.png')
    enemy1_down_rect = enemy1_down.get_rect()
    enemydown1 = enemy1_down.subsurface(enemy1_down_rect)
    enenys_down.append(enemydown1)
    enemy2_down = pygame.image.load('image/airplane_ember2.png')
    enemy2_down_rect = enemy2_down.get_rect()
    enemydown2 = enemy2_down.subsurface(enemy2_down_rect)
    enenys_down.append(enemydown2)
    enemy3_down = pygame.image.load('image/airplane_ember3.png')
    enemy3_down_rect = enemy3_down.get_rect()
    enemydown3 = enemy3_down.subsurface(enemy3_down_rect)
    enenys_down.append(enemydown3)


    while True:
        # 動態顯示得分
        score = str(Score)
        myscore = pygame.font.SysFont("arial", 40)
        scoreImage = myscore.render(score, True, (0, 0, 0))
        # 判斷事件，防止卡頓或者意外退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP] or key_pressed[K_w]:
            player.moveup()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            player.movedown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            player.moveleft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            player.moveright()

        screen.blit(backgroundsurface, (0, 0))

        if not player.is_hitted:
            # 按頻率生成子彈
            if bullet_frequency % 30 == 0:
                player.shoot(bulletfilename)
            bullet_frequency += 1
            if bullet_frequency >= 30:
                bullet_frequency = 0
            # 讓子彈動起來
            for i in player.bullets:
                i.move()
                screen.blit(i.bullet_image,i.bullet_rect)
                # 當子彈飛出螢幕，刪除子彈物件
                if i.bullet_rect.bottom <= 0:
                    player.bullets.remove(i)
            # 按頻率生成敵機
            if enemy_frequency % 100 == 0:
                enemypos = [random.randint(30, 630), 0]
                enemyplane = Enemy(enemyfilename, enemypos)
                #將敵機物件新增到列表中
                enemys.append(enemyplane)
            enemy_frequency += 1
            if enemy_frequency >= 100:
                enemy_frequency = 0
            # 讓敵機動起來
            for i in enemys:
                i.move()
                screen.blit(i.enemy_image,i.enemy_rect)
                # 當敵機飛出螢幕，刪除敵機物件
                if i.enemy_rect.bottom >= 950:
                    enemys.remove(i)
                # 遍歷子彈物件，判斷子彈是否擊中敵機
                for j in player.bullets:
                    # 如果擊中，分數增加，同時移除該子彈和敵機物件
                    if pygame.Rect.colliderect(j.bullet_rect,i.enemy_rect):
                        Score += 100
                        enemys.remove(i)
                        player.bullets.remove(j)
                        for k in enenys_down:
                            screen.blit(k,i.enemy_rect)
                # 遍歷敵機物件，判斷玩家是否和敵機相撞
                if pygame.Rect.colliderect(player.plane_rect,i.enemy_rect):
                    # 修改is_hitted的值，跳出該層迴圈
                    player.is_hitted = True
                    break


            screen.blit(player.play_image,player.plane_rect)
            screen.blit(textImage, (0,0))
            screen.blit(scoreImage, (110, 0))
            pygame.display.update()
        # 玩家退出時顯示分數和遊戲結束
        else:
            screen.blit(gameoversurface,(0,0))
            screen.blit(textImage, (0, 0))
            screen.blit(scoreImage, (110, 0))
            pygame.display.update()
            time.sleep(2)
            break

main()