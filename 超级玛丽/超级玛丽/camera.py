from basetypes import Vector2
import config

class Camera():
    def __init__(self, pos, w, h):
        self.pos = pos
        self.w = w
        self.h = h

    def update(self, mario):
        '''摄像头跟着马里奥跑'''
        if self.pos.x < config.MAXIMUM_CAMERA_SCROLL:
            if self.get_camera_to_other(mario).x > config.MAX_DIS_CAMERA_TO_MARIO and config.mario.vel.x>0:
                self.pos.x += config.mario.vel.x * config.delta_time

    def get_camera_to_other(self,other):
        #返回物体与摄像头的相对位置
        return (other.pos - self.pos )
