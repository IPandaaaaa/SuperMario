import pygame

import config
import basetypes
import sprites

class Mario(basetypes.DynamicCollision):
    '''马里奥'''
    #马里奥的pos是相对于背景图片的绝对位置，但是在绘图时，应该绘制和camera的相对位置
    def __init__(self, pos, w, h, vel):
        super().__init__(pos, w, h, vel)
        self.acc = 0  # 水平加速度
        self.vertacc = 0  # 垂直方向的加速度
        self.dx = 0
        self.dy = 0
        self.issupported = True#默认收到支持力
        self.pressed_right = False
        self.pressed_left = False
        self.pressed_down = False
        self.pressed_space = False
        self.model = sprites.SMALL_MARIO_IDLE#用的哪张素材
        self.count = 0#计数器
        self.action_state_machine = basetypes.State_Machine('idle_state')
        self.jump_state_machine = basetypes.State_Machine('nojump_state')
        self.mario_state_machine = basetypes.State_Machine('small_mario')

    def responce_to_keyboard(self, level):
        '''响应键盘输入'''
        '''根据键盘输入与现在的状态机，产生相应的加速度并改变状态机，但不执行运动，
           具体的移动在movement中执行'''
        #左右键
        if config.KEYS[pygame.K_RIGHT] and not config.KEYS[pygame.K_LEFT]:
            self.pressed_right = True
        elif config.KEYS[pygame.K_LEFT] and not config.KEYS[pygame.K_RIGHT]:
            self.pressed_left = True
        if not config.KEYS[pygame.K_RIGHT]:
            self.pressed_right = False
        if not config.KEYS[pygame.K_LEFT]:
            self.pressed_left = False

        if(self.pressed_right and not self.pressed_left):
            '''按了右键没按左键,判断物体的状态机
                如果是move_state，且速度向左，则改为'brake_state',产生向右刹车加速度
                其他情况，产生向右的加速度,并改为'move_state’
            '''
            if self.action_state_machine.get_state()=='move_state' and self.vel.x < 0:
                self.acc = config.BRAKE_FRICTION * config.MARIO_ACCELERATION
                self.action_state_machine.change_state('brake_state')
            else:
                self.acc = config.MARIO_ACCELERATION
                self.action_state_machine.change_state('move_state')
        elif(self.pressed_left and not self.pressed_right):
            '''按了左键没按右键，类似上述条件'''
            if self.action_state_machine.get_state()=='move_state' and self.vel.x > 0:
                self.acc = - config.BRAKE_FRICTION * config.MARIO_ACCELERATION
                self.action_state_machine.change_state('brake_state')
            else:
                self.acc = -config.MARIO_ACCELERATION
                self.action_state_machine.change_state('move_state')
        else:
            '''左右键都没按 或者 左右键都按了 要判断物体的状态机
                如果物体是idle_state,加速度为0
                如果物体是move_state，则摩擦减速，并改变物体状态机
            '''
            if self.action_state_machine.get_state()=='idle_state':
                acc = 0
            elif self.action_state_machine.get_state()=='move_state':
                if self.vel.x > 0:
                    self.acc = - config.FRICTION * config.MARIO_ACCELERATION
                else:
                    self.acc = config.FRICTION * config.MARIO_ACCELERATION
                self.action_state_machine.change_state('frict_state')
            pass

        #空格键
        #先判断左右，在判断垂直，因为垂直优先级比较高
        if config.KEYS[pygame.K_SPACE] and not self.pressed_space:
            self.pressed_space = True
        if not config.KEYS[pygame.K_SPACE]:
            self.pressed_space = False
        if self.pressed_space:
            '''按了空格的响应事件，判断状态机
                如果是nojump_state，基于较大的初始加速度（负数），并修改状态
                如果是jump_state，且没有达到最大上升速度，给予较小的持续加速度（负数）
                已经达到最大速度，和下落状态按空格，则和没按空格一样处理
             '''
            if self.jump_state_machine.get_state() == 'nojump_state':
                self.vertacc = - config.MARIO_JUMP_START_ACCELERATION
                self.jump_state_machine.change_state('jump_state')
            elif self.jump_state_machine.get_state() == 'jump_state' and abs(self.vel.y) < config.MAX_MARIO_JUMP_VEL:
                self.vertacc = - config.MARIO_JUMP_ACCELERATION
            else:
                #这里同下面的没按空格状态
                if self.jump_state_machine.get_state() == 'jump_state':
                    self.vertacc = config.GRAVITYACCELERATION
                    self.jump_state_machine.change_state('fall_state')
                elif self.jump_state_machine.get_state() == 'nojump_state':
                    if self.issupported:
                        self.vertacc = 0
                    else:
                        self.vertacc = config.GRAVITYACCELERATION
                        self.jump_state_machine.change_state('fall_state')

        else:
            '''没按空格，判断状态机
                如果是jump_state，则加速度修改为重力加速度（正的），并改变状态为'fall_state'（在后面通过碰撞检测来决定是否改为nojump）
                如果是nojump_state且受到支持力，则加速度为0
                如果是nojump_state且不受到支持力，则加速度修改为重力加速度（正的），并改变状态为'fall_state'
            '''
            if self.jump_state_machine.get_state() == 'jump_state':
                self.vertacc = config.GRAVITYACCELERATION
                self.jump_state_machine.change_state('fall_state')
            elif self.jump_state_machine.get_state() == 'nojump_state' :
                if self.issupported:
                    self.vertacc = 0
                else:
                    self.vertacc = config.GRAVITYACCELERATION
                    self.jump_state_machine.change_state('fall_state')

        self.movement(level)

    def reset_idle(self):#水平方向速度重置
        self.acc=0
        self.vel.x=0
        self.dx = 0
        self.action_state_machine.change_state('idle_state')

    def reset_idle_vert(self):#垂直方向速度重置
        self.vertacc = 0
        self.vel.y=0
        self.dy = 0
        self.jump_state_machine.change_state('nojump_state')

    def movement(self, level):
        '''移动'''
        '''根据加速度改变速度，判断有没有碰撞，并改变马里奥的状态机'''
        if abs(self.vel.x) <= config.MAX_MARIO_SPEED:
            self.vel.x += self.acc * config.delta_time
        elif self.vel.x > 0:
            self.vel.x = config.MAX_MARIO_SPEED
        else:
            self.vel.x = - config.MAX_MARIO_SPEED

        self.vel.y += self.vertacc * config.delta_time

        self.dx,self.dy = self.vel.x * config.delta_time,self.vel.y * config.delta_time

        self.issupported = False#判断有没有碰撞前，默认不受支持力
        #这里判断有无碰撞,并根据碰撞方向，执行相应操作
        for collider in level.static_colliders + level.dynamic_colliders:
            if self.iscollided(collider,self.dx,self.dy):#判断有没有碰撞，返回撞到的碰撞体
                #如果有碰撞，判断方向，执行相应操作
                pro = self.iscollidedbywhichdir(collider)
                if pro =='left':
                    self.reset_idle()
                    self.pos.x = collider.pos.x - self.w
                elif pro =='right':
                    self.reset_idle()
                    self.pos.x = collider.pos.x + collider.w
                elif pro == 'up':
                    self.reset_idle_vert()
                    self.issupported = True #收到支持力
                    self.pos.y = collider.pos.y - self.h
                elif pro == 'down':
                    self.reset_idle_vert()
                    self.pos.y = collider.pos.y + collider.h

        #根据判断后的dx,dy 来转变物体运动状态
        #刹车或者摩擦减速状态时，速度小于0.02时，将水平速度和加速度置为0，并改变状态机
        if self.action_state_machine.get_state() in ['brake_state','frict_state'] and abs(self.vel.x)<0.02:
            self.reset_idle()

        #马里奥不可以往回走
        if self.pos.x + self.dx <= config.camera.pos.x:
            self.reset_idle()
            self.pos.x = config.camera.pos.x

        self.pos.x += self.dx
        self.pos.y += self.dy

    def blitme(self,screen):# 画马里奥
        config.screen.blit(sprites.tile_set,
                            (config.camera.get_camera_to_other(config.mario).x, config.camera.get_camera_to_other(config.mario).y),
                            self.model)



