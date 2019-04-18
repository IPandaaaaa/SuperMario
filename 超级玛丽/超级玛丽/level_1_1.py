import tiles
from sprites import level_1_img
from basetypes import Vector2, StaticCollision
import config

#不会动的碰撞体
static_colliders = []

#会动的碰撞体
dynamic_colliders = []

coins = []
super_mushrooms = []
enemies = []

#砖头碎了 碎片掉到这
brick_fragments = []

#分割的地板开始和结束的砖头的位置
start_tile = None
end_tile = None

for y in range(0, level_1_img.size[1]):
    for x in range(0, level_1_img.size[0]):

        color = level_1_img.getpixel((x, y))
        pos = Vector2(x * config.TILE_SIZE, y * config.TILE_SIZE + 24)

        # 黑色的都是地板
        if color == config.BLACK:
            if start_tile == None:
                start_tile = pos
            if end_tile == None:
                if x + 1 > level_1_img.size[0]:
                    end_tile = pos
                if level_1_img.getpixel((x + 1, y)) != config.BLACK:
                    end_tile = pos
            if end_tile != None and start_tile != None:
                w = end_tile.x - start_tile.x + config.TILE_SIZE
                h = config.TILE_SIZE
                static_colliders.append(StaticCollision(start_tile, w, h))
                end_tile = None
                start_tile = None

        # 红色的是管道
        elif color == config.RED:
            h = config.SCREEN_SIZE.y - pos.y
            w = 2 * config.TILE_SIZE
            static_colliders.append(StaticCollision(pos, w, h))

        # 灰色的是可以撞碎的砖头
        elif color == config.GRAY:
            dynamic_colliders.append(tiles.Brick(pos, config.TILE_SIZE, config.TILE_SIZE))

         # 黄色的是有金币的问号砖头
        elif color == config.YELLOW:
            dynamic_colliders.append(tiles.QuestionTile(pos, config.TILE_SIZE, config.TILE_SIZE, 'coin'))

        #绿色的是有mushroom的问号砖头
        elif color == config.GREEN:
            dynamic_colliders.append(tiles.QuestionTile(pos, config.TILE_SIZE, config.TILE_SIZE, 'mushroom'))

        #棕色是goomba
        elif color == config.BROWN:
            dynamic_colliders.append(tiles.Goomba(pos, config.TILE_SIZE, config.TILE_SIZE, 0))

        #紫色的是乌龟
        elif color == config.PURPLE:
            dynamic_colliders.append(tiles.Turtle(pos, config.TILE_SIZE, config.TILE_SIZE, 0))