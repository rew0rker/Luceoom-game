# Luceoom
**3D-game written in python(v3.8.6) using pygame(v2.0.0).**

Inspired by the cult game DOOM, it was decided to write my own game like DOOM, only in python using the pygame library.
## Video demo: https://youtu.be/z_KfFhgwGvI
# Description
The game has 3 levels, your task is to go through each and kill the main boss at the end. You initially have 100 health units and 2 weapons to choose from, moving through the levels you can find first-aid kits that restore your health. Remember, the next level will not open until you kill all the opponents on the current one.

## How to play?
Run the main.py or exe file. In the main menu, select the difficulty level and the mode for displaying the corpses of mobs.
  
## Mobs:
* Obyuma is a big black monkey. HP: 3, melee.  
* Soldier - a soldier with a cannon, instantly shoots. HP: 1, ranged.  
* Pinky - pink devil HP: 5, melee.  
* Stas - A very dangerous enemy. HP: 10, melee.  
* Sosademon - Boss. Very fast and kills with one hit. HP: 30, melee.
   
## Gun:
 * Shotgun - slow but powerful weapon, deals 1.5 damage.  
 * Automatic - fast weapon, deals 0.35 damage. 
  
## Management:  
* W, A, S, D - character movement  
* 1, 2, mouse wheel - change weapon  
* LMB - shooting
  
+ Also in the game there are first-aid kits, which restore 35 HP  
  
+ Igrom can open the door to the next room, only if all the mobs in this room are killed

## Code Description  
Below is a detailed description of each file.  
### main.py  
This file is responsible for starting the program. The main functions are initialized, drawing starts and an endless loop, which is the program.
  

### sprites.py 
This file is responsible for the configuration of each mob and parameter in the game
```python
Class Sprites:
   def init # here we set lists with objects and their coordinates (doors and mobs for 3 levels)

   def sprite_shot # returns the closest object to the player being fired upon

   def b_doors # returns a dictionary of all closed doors

   def delete_objects # clears the map of mob corpses and open doors

Class AllSprites:
    def init # here all parameters for each sprite are initialized in order to further work on it
    def is_on_fire # check if the sprite is in the line of fire

    def pos # returns the current position on the map

    def object_locate # determining the distance to a sprite

    def s_animation # display attack animation if the mob sees us and we are at a distance at which he sees us (self.animation_dist)

    def show_sprite # display sprites (so the player can see them)

    def dead_animation # display animation of the death of mobs and objects

    def s_action # displaying a mob from different angles (if you bypass it at a large distance, it looks different)

    def d_open # открывает указаннуб дверь
```
Next come the classes of each sprite (they store the parameters for each sprite,
which will then be initialized when they spawn on the map)
```
Parameters:
    way - list with base sprite images from different angles

    viewing_angles - a parameter that determines how the sprite looks from different angles (False - the same, True - different)

    shift - sprite height relative to the floor

    scale - sprite scaling (very handy for editing sprite size directly in code)

    side - sprite size

    animation - sprite size

    animation_dist - the distance at which the sprite sees the player

    animation_speed - the speed of changing each animation picture

    dead - the flag (first True) will change to False when the sprite is killed

    dead_shift - position of the body relative to the floor

    dead_anim - список анимаций смерти

    tp - object type (barrel, fire, mob, first aid kit)

    blocked - is it possible to walk through the sprite (True - not possible)

    npc_hp - mob's HP
```
  
### map.py 
This file sets the parameters of the map and minimap, sets the width and length of the world. Also, the desired wall textures are added here.
```python
Class Camera:  
	def __init__:  
		Initializes a class that implements player tracking on the minimap.  
  
	def update:  
		Updates minimap data.  
  
	def apply:  
		Updates the minimap.
```
  
### malen.py 
(from German - drawing) This file draws everything that is in the player's field of view (wall textures, etc.)
  ```python
  class Malen:
	def __init__:
		Here the parameters of the object of the Malen class are set, as well as the parameters of weapons of both types.

	def bg:
		The function draws the sky.

	def world:
		Arranges sprites on the map.

	def fps:
		Draws fps on the screen.

	def hp:
		Draws a health bar on the screen.

	def terminate:
		Allows you to exit the game.

	def mini_map:
		Draws a minimap on the screen.

	def choice_weapon:
		Implements weapon selection.

	def bullet_sfx:
		Draws an explosion from a bullet on a wall or NPC.
	
	def win:
		Displays the victory screen.
	
	def menu:
		Displays the launch menu

	def dead_menu:
		Displays the death screen
```
  
### parameters.py
 This file specifies the basic constants necessary for the productive operation of the program. For example: player position, view angle, width and height of textures.
  
### gamer.py 
В этом файле находится класс игрока, в котором находятся следующие функции
```python
class Gamer:
	def __init__(self, sprites):
		# here we set all the necessary attributes and define flags
		
	def pos(self):
		# we return the current coordinates of the player, but it's more convenient and faster using the built-in decorator to use the function as a class attribute
	def collision_list(self):
		# return a list of all objects that are not transparent to the player and that cannot be walked through. For convenience, we use a decorator

	def detect_collision(self):
		# in this function, we determine whether the player's rectangle (from init) intersects with the rectangle of certain sprites (defined in the class of each sprite)

	def keys_check(self):
		# of this function, we define by the standard method of projections onto different axes horizontal and vertical components of 
        # velocities, we tie them to familiar in shooters control, determine the moments of the shot and switching between weapons

	def is_dead(self):
		# check that the character is alive, otherwise change the flag from init

	def return_flag(self):
		# returns the player's current weapon

	def mouse_verific(self):
		# we have mouse movement only along the x-axis, so we look at the scale  
		# movement, set the mouse to a constant position in the center of the screen and change player angle

	def movement(self):
		# prefab for the above, so we adjust the    angle by putting  
		# it into the standard trigonometry class 10 framework
```
  
### interaction.py 
```python
class Interaction:
	def init:
		# objects of the Gamer, Sprites and Malen classes are initialized here, as well as  
difficulty level flag

	def terminate: 
		# game over

	def interaction_objects:
		# determines the reaction of objects to the player's shooting, depending on their type

	def npc_action:
		# object attack on the player

	def set_difficulty:
		# difficulty level processing

	def npc_move:
		# mob movement towards the player

	def play_music: 
		# trigger music during combat

	def wins: 
		# called when the player killed all the mobs (it calls the victory menu and winning music)

	def deads:
		# (called when the player dies) it calls the death menu and shout
```



