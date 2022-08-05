# coding=UTF-8
import pyglet
from pyglet.window import mouse
#https://pyglet.readthedocs.io/en/latest/programming_guide/media.html
pyglet.options['search_local_libs'] = True

from card import Card
from card_manger import Card_manger
from process_bar import ProcessBar

#游戏的音效
#https://mixkit.co/free-sound-effects/game/
#Explainer video game alert sweep 我先用一个这个音效试试
sweep_sound = pyglet.media.load('sound/mixkit-explainer-video-game-alert-sweep-236.wav')
#sweep_sound.play() 这样就可以开始播放了，倒是很简单

# https://api.arcade.academy/en/latest/tutorials/card_game/index.html

window = pyglet.window.Window(width=640, height=480,caption= u"Card Game")

#例子给得东西，留着这里做参照物
label = pyglet.text.Label('Card Game',
                          font_name='Times New Roman',
                          font_size=72,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


#框架的logger，很好用，一直开着吧
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

batch = pyglet.graphics.Batch()

#square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))
card1 = Card(x=200, y=200, width=60, height=80, color=(255, 55, 255),batch=batch,name=u"Bomb")
card2 = Card(x=300, y=300, width=60, height=80, color=(55, 55, 255),batch=batch,name=u"U-235")


#初始化管理器
cardManger = Card_manger(batch)
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
        # print(card1)
        # print(card2)
        # print(DragObj)
        window.set_mouse_cursor(cursor_hand)
        DragObj.move(dx,dy)
        #让manger不停的检查是否可以成组
        cardManger.can_be_stack()
    return True

#on_mouse_release(x=160, y=67, button='LEFT', modifiers=)
@window.event
def on_mouse_release(x, y, button, modifiers):
    #如果在释放鼠标的那一刻，发现活动卡片有了卡组
    if cardManger.activeCard:
        if cardManger.activeCard.getCardGroup():
            cardManger.activeCard.uiAttchToGroup()
            
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

#传入给do_action的回调函数
def update_processBar(cardgroup):
    #如果有processBar，那就调用更新方法
    if cardgroup.getProcessBar():
        print("它有进度条？？？")
        pb = cardgroup.getProcessBar()
        pb.width += 9
        if pb.width > 60:
            pb.width=5
            c = Card(x=20, y=20, width=110, height=80, color=(255, 55, 75),batch=batch,name=u"Nuclar Bomb")
            cardManger.reg_obj(c)
            
    else:
    #如果这家伙没有，那就好说了，新建一个进度条，并且附加到卡组上面去
        color=(0, 0, 0)
        pb=ProcessBar(0,0,0,0,color,batch,"text")
        cardgroup.uiAttchProcessBar(pb)

#每秒钟会有一次调用
def update(dt):
    print("interval trigger")
    cardManger.do_action(update_processBar)
    pass


pyglet.clock.schedule_interval(update, 1)

pyglet.app.run()