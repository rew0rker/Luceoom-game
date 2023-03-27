# Luceoom
**3д-игра написанная на python(v3.8.6) с помощью pygame(v2.0.0).**

Вдохновившись культовой игрой DOOM, было принято решение написать собственную игру наподобии DOOM, только уже на python с помощью библиотеки pygame.

## Описание
В игре представлено 3 уровня, ваша задача пройти каждый и убить главного босса в конце. У вас изначально 100 единиц здоровья и 2 оружия на выбор, перемещаясь по уровням вы можете находить аптечки, которые восстанавливают ваше здоровье. Помните, следущий уровень не откроется, пока вы не убьете всех противноков на текущем.

## Как играть?
Запустите файл main.py или exe. В главном меню выберете уровень сложности и режим отображения трупов мобов.
  
## Персонажи:  
  * Обьюма - большая черная обезьяна. ХП: 3, ближний бой.  
  * Солдат - солдат с пушкой, мгновенно стреляет. ХП: 1, дальний бой.  
  * Пинки - розовый черт ХП: 5, ближний бой.  
  * Стас -  Очень опасный враг. ХП: 10, ближний бой.  
  * Сосадемон - Босс. Очень быстрый и убивает с одного удара. ХП: 30, ближний бой.  
   
## Пушки:  
  * Дробовик - медленное, но мощное оружие, наносит 1,5 единицы урона.  
  * Автомат - быстрое оружие, наносит 0.35 единиц урона.  
  
## Управление:  
  * W,A,S,D - передвижение персонажа  
  * 1, 2, колесико мыши - смена оружия  
  * ЛКМ - стрельба  
  
+ Также в игре присутсвуют аптечки, который восстанавливают 35 ХП
  
+ Игром может открыть дверь в следующую комнату, только в случае убийства всех мобов в данной комнате  

## Описание кода
Ниже представлено подробное описание каждого файла  
### main.py
 Данный файл отвечает за запуск программы. Инициализируются основные функции, запускается отрисовка и бесконечный цикл, который и является программой.
  
### sprites.py 
  Данный файл отвечает за конфигурация каждого моба и параметра в игре
```python
Class Sprites:
   def init - здесь мы задаем списки с объектами и их координатами(двери и мобы для 3х уровней)

   def sprite_shot - возвращает ближайший объект к игроку, по которому идет стрельба

   def b_doors - возвращает словарь всех закрытых дверей

   def delete_objects - очищает карту от трупов мобов и открытых дверей

Class AllSprites:
    def init - здесь инициализируются все параметры для каждого спрайта чтобы в дальнейшем работать над ним
    def is_on_fire - проверяем, находиться ли спрайт на линии огня

    def pos - возвращает текущую позицию на карте

    def object_locate - определение расстояния до спрайта

    def s_animation - отображения анимации атаки если моб нас видит и мы находимся на расстоянии при котором он нас видит(self.animation_dist)

    def show_sprite - отображаем спрайты(чтобы игрок их видел)

    def dead_animation - отображение анимации смерти мобов и объектов

    def s_action - отображение моба с разных углов(если на большом растоянии его обходить он выглядит по-разному)

    def d_open - открывает указаннуб дверь

Далее идут классы каждого спрайта(в них хранятся параметры для каждого спрайта, которые потом будут инициализированы при спавне их на карте)

Параметры:

    way - список с базовыми изображениями спрайта с разных углов

    viewing_angles - параметр, определяющий как выглядит спрайт с разных углов (False - одинаково, True - по-разному)

    shift - высота спрайта относительно пола

    scale - масштабирование спрайта(очень удобно для редактирования размера спрайта прямо в коде)

    side - размер спрайта

    animation - анимация атаки

    animation_dist - расстояние, при котором спрайт видит игрока

    animation_speed - скорость смены каждой картинки анимации

    dead - флаг(сначала True) изменится на False, когда спрайт будет убит

    dead_shift - положение трупа относительно пола

    dead_anim - список анимаций смерти

    tp - тип объекта(бочка,огонь, моб,аптечка)

    blocked - можно ли ходить сквозь спрайт(True - нельзя)

    npc_hp - количество хп моба
```
  
### map.py 
  В данном файле задаются параметры карты и миникарты, задается ширина и длина мира. Также здесь добавляются нужные текстуры стен.
  ```python
Сlass Camera:
Функция __init__:
	Инициализирует класс, который реализует отслеживание игрока на миникарте.

Функция update:
	Обновляет данные о миникарте.

Функция apply:
	Обновляет миникарту.
```
  
### malen.py 
  (с немецкого - рисование) Данный файл отрисовывает все, что находится в поле зрения игрока (текстуры стен и т.д.)\
  ```python
  class Malen:
	def __init__:
		Здесь задаются параметры объекта класса Malen, а также параметры оружия обоих видов.

	def bg:
		Функция отрисовывает небо.

	def world:
		Расставляет спрайты по карте.

	def fps:
		Отрисовывает fps на экране.

	def hp:
		Отрисовывает полоску здоровья на экране.

	def terminate:
		Позволяет выйти из игры.

	def mini_map:
		Отрисовывает миникарту на экране.

	def choice_weapon:
		Реализует выбор оружия.

	def bullet_sfx:
		Отрисовывает взрыв от пули на стене или нпс.
	
	def win:
		Отображает экран победы.
	
	def menu:
		Отображает меню запуска.

	def dead_menu:
		Отображает экран смерти
  ```
  
### parameters.py
 В данном файле задаются основные константы, необходимые для продуктивной работы программы. Например: позиция игрока, угол обзора, ширина и высота текстур.
  
### gamer.py 
В этом файле находится класс игрока, в котором находятся следующие функции
```python
class Gamer:
	def __init__(self, sprites):
		здесь мы задаем все нужные атрибуты и определяем флаги
		
	def pos(self):
		возвращаем текущие координаты игрока, но это удобнее и быстрее при помощи встроенного декоратора, чтобы использовать функцию как атрибут класса
	def collision_list(self):
		возвращаем список всех объектов, которые не прозрачны для игрока, через которые нельзя ходить. Для удобства используем декоратор

	def detect_collision(self):
		в этой функции определяем, пересекается ли прямоугольника игрока (из инита) с прямоугольником тех или иных спрайтов (определен в классе каждого спрайта)

	def keys_check(self):
		в этой функций мы стандартным методом проекций на разные оси задаем
		горизонтальные и вертикальные составляющие скоростей, привязываем их к
		привычному в шутерах управлению, определяем моменты выстрела и
		переключение между оружием

	def is_dead(self):
		проверка на то, что персонаж жив, иначе меняем флаг из инита

	def return_flag(self):
		возвращает текущее оружие игрока

	def mouse_verific(self):
		движение мышки у нас только по оси икс, поэтому мы смотрим масштабность
		движения, задаем мыши постоянное положение в центре экрана и изменяем
		угол игрока

	def movement(self):
		сборная функция для вышеописанных, так же мы корректируем угол, помещая
		его в стандартные для тригонометрии 10 класса рамки
```
  
### interaction.py 
```python
class Interaction:
	def init:
		здесь инициализируются объекты классов Gamer, Sprites и Malen, а также
		флаг уровня сложности

	def terminate: 
		завершение игры

	def interaction_objects:
		определяет реакцию объектов на стрельбу игрока, в зависимости от их типа

	def npc_action:
		атака объектов на игрока

	def set_difficulty:
		обработка уровня сложности

	def npc_move:
		движение моба к игроку

	def play_music: 
		запуск музыки во время боя

	def wins: 
		вызывается когда игрок убил всех мобов (в ней вызывается меню победы и
		победная музыка)

	def deads:
		(вызывается при смерти игрока) в ней вызывается меню смерти и крик
```
