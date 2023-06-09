#  в этом файле описан класс игрока

import sys
import pygame
import math
from map import collision_walls
from parameters import *


# функция закрытия игры
def terminate():
    pygame.quit()
    sys.exit()


class Gamer:
    def __init__(self, sprites):
        self.x, self.y = gamer_pos  # координаты
        self.angle = gamer_angle  # угол
        self.sensitivity = 0.002  # чувствительность
        self.sprites = sprites    # спрайты для коллизици
        # флаги для трех комнат
        self.first_room = True
        self.second_room = False
        self.third_room = False
        self.flag = ''
        self.hp = 100  # здоровье
        self.weapon_now = 'shotgun'
        #  Параметры игрока для того, чтобы не ходить сквозь стены
        self.side = 50
        self.rect = pygame.Rect(*gamer_pos, self.side, self.side)
        #  прямоугольник для миникарты
        self.minirect = pygame.Rect(gamer_pos[0] // MAP_SCALE, gamer_pos[1] // MAP_SCALE,
                                    self.side // MAP_SCALE,
                                    self.side // MAP_SCALE)
        self.shot = False  # флаг стрельбы
        self.alive = True  # проверка на жизни

# используем встроенный декоратор (делаем функцию атрибутом), чтобы постоянно обновлять координаты
    @property
    def pos(self):
        # print(self.x, self.y)
        return (self.x, self.y)

    @property  # декоратор для определения того, через что ходить нельзя
    def collision_list(self):
        return collision_walls \
               + [pygame.Rect(*obj.pos, obj.side, obj.side)
                  for obj in self.sprites.list_of_sprites if obj.blocked] \
               + [pygame.Rect(*obj.pos, obj.side, obj.side)
                  for obj in self.sprites.list_of_sprites_2 if obj.blocked] \
               + [pygame.Rect(*obj.pos, obj.side, obj.side)
                  for obj in self.sprites.list_of_sprites_3 if obj.blocked] \
               + [pygame.Rect(*obj.pos, obj.side, obj.side)
                  for obj in self.sprites.list_of_sprites_doors if obj.blocked]

    # функция для текущего определения коллизии через прямоугольники
    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0
        self.x += dx
        self.y += dy

    #  функция для определения нажатых клавиш для перемещения/стрельбы
    def keys_check(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()  # берем словарь нажатых кнопок
        if keys[pygame.K_ESCAPE]:
            terminate()  # при нажатии на экскейп закрываем приложение
        # классическое WASD
        if keys[pygame.K_w]:
            dx = gamer_speed * cos_a
            dy = gamer_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -gamer_speed * cos_a
            dy = -gamer_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = gamer_speed * sin_a
            dy = -gamer_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -gamer_speed * sin_a
            dy = gamer_speed * cos_a
            self.detect_collision(dx, dy)
        #  крутимся при помощи стрелок
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        #  переключаемся на разные оружия цифрами
        if keys[pygame.K_1]:
            # подрубаем звук перезарядки и меняем флаг
            if self.flag == 'autorifle':
                pygame.mixer.Sound('data/sound/reload.wav').play()
            self.flag = 'shotgun'
        if keys[pygame.K_2]:
            # подрубаем звук перезарядки и меняем флаг
            if self.flag == 'shotgun':
                pygame.mixer.Sound('data/sound/reload.wav').play()
            self.flag = 'autorifle'
        for event in pygame.event.get():
            if pygame.event == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # активируем флаг выстрела
                if event.button == 1 and not self.shot:
                    self.shot = True
                # подключаем колесико мыши для смены оружия
                if event.button == 4 or event.button == 5 and not self.shot:
                    if self.flag == 'shotgun':
                        self.flag = 'autorifle'
                    else:
                        self.flag = 'shotgun'
                    # звук перезарядки
                    pygame.mixer.Sound('data/sound/reload.wav').play()

    # общая функция для движения
    def movement(self):
        self.keys_check()
        self.mouse_verific()
        # перемещаем прямоугольник
        self.rect.center = self.x, self.y
        self.minirect.center = self.x // MAP_SCALE, self.y // MAP_SCALE
        self.angle %= ZWEI_PI  # корректировка угла

    def return_flag(self):
        return self.flag

    def mouse_verific(self):
        #  движение мышкой
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - H_WIDTH
            pygame.mouse.set_pos((H_WIDTH, H_HEIGHT))  # устанавливаем позицию мыши по центру
            self.angle += diff * self.sensitivity  # меняем угол поворота

    # функция проверки на смерть, меняющая флаг
    def is_dead(self):
        if self.hp <= 0:
            self.alive = False
            