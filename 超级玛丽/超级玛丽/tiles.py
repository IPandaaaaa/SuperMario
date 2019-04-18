from basetypes import  StaticCollision,DynamicCollision
import config
import sprites

class QuestionTile(StaticCollision):#问号砖头
    def __init__(self, pos, w, h, contents):
        super().__init__(pos, w, h)
        self.contents =contents
        self.model = sprites.Q_BLOCK_CLOSED[0]

    def blitme(self, screen):
        pos = config.camera.get_camera_to_other(self)
        screen.blit(sprites.tile_set, (pos.x, pos.y), self.model)

class Brick(StaticCollision):#可以撞碎的砖头
    def __init__(self, pos, w, h):
        super().__init__(pos, w, h)
        self.model = sprites.BRICK
    def blitme(self, screen):
        pos = config.camera.get_camera_to_other(self)
        screen.blit(sprites.tile_set, (pos.x, pos.y), self.model)

class Coin(StaticCollision):#金币
    def __init__(self, pos, w, h):
        super().__init__(pos, w, h)
        self.model = sprites.COIN[0]

    def blitme(self, screen):
        pos = config.camera.get_camera_to_other(self)
        screen.blit(sprites.tile_set, (pos.x, pos.y), self.model)

class Super_Mushroom():
    pass

class Brick_Fragment():
    pass

class Goomba(DynamicCollision):
    def __init__(self, pos, w, h, vel):
        super().__init__(pos, w, h, vel)
        self.model = sprites.GOOMBA_RUN[0]

    def blitme(self, screen):
        pos = config.camera.get_camera_to_other(self)
        screen.blit(sprites.tile_set, (pos.x, pos.y), self.model)

class Turtle(DynamicCollision):
    def __init__(self, pos, w, h, vel):
        super().__init__(pos, w, h, vel)
        self.model = sprites.TURTLE[0]

    def blitme(self, screen):
        pos = config.camera.get_camera_to_other(self)
        screen.blit(sprites.tile_set, (pos.x, pos.y), self.model)


