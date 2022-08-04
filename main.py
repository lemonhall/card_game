# coding=UTF-8
import pyglet
from pyglet.window import mouse
#https://pyglet.readthedocs.io/en/latest/programming_guide/media.html
pyglet.options['search_local_libs'] = True

from card import Card
from card_manger import Card_manger

#游戏的音效
#https://mixkit.co/free-sound-effects/game/
#Explainer video game alert sweep 我先用一个这个音效试试
sweep_sound = pyglet.media.load('sound/mixkit-explainer-video-game-alert-sweep-236.wav')
#sweep_sound.play() 这样就可以开始播放了，倒是很简单

# https://api.arcade.academy/en/latest/tutorials/card_game/index.html

window = pyglet.window.Window(width=1024, height=768,caption= u"Card Game")

#例子给得东西，留着这里做参照物
label = pyglet.text.Label('Card Game',
                          font_name='Times New Roman',
                          font_size=72,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


#框架的logger，很好用，一直开着吧
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)


#square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))
card1 = Card(x=200, y=200, width=60, height=80, color=(255, 55, 255),name=u"第零话")
card2 = Card(x=300, y=300, width=60, height=80, color=(55, 55, 255),name="匪兵乙")


#初始化管理器
cardManger = Card_manger()
#把对象添加给管理器
cardManger.reg_obj(card1)
cardManger.reg_obj(card2)

# @window.event
# def on_mouse_press(x, y, button, modifiers):
#     if button == mouse.LEFT:
#         print('The left mouse button was pressed.')
#         #cardManger.check(x,y)


#https://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html
cursor_default = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)
cursor_hand = window.get_system_mouse_cursor(window.CURSOR_HAND)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    DragObj = cardManger.check(x,y)
    if DragObj:
        window.set_mouse_cursor(cursor_hand)
        DragObj.move(dx,dy)
        cardManger.can_be_stack()
    return True

#on_mouse_release(x=160, y=67, button='LEFT', modifiers=)
@window.event
def on_mouse_release(x, y, button, modifiers):
    cardManger.activeCard = None
    window.set_mouse_cursor(cursor_default)
    #sweep_sound.play()

@window.event
def on_mouse_motion(x, y, dx, dy):
    cardManger.activeCard = None
    window.set_mouse_cursor(cursor_default)

@window.event
def on_draw():
    window.clear()
    label.draw()
    cardManger.draw()

pyglet.app.run()