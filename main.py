
# coding=UTF-8
import pyglet
from pyglet.window import mouse
from pyglet import shapes
from pyglet.shapes import Rectangle
import glooey

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

#https://pyglet.readthedocs.io/en/latest/modules/shapes.html
#Card对象，直接继承于Rectangle类
#id，type这些估计以后都需要的
class Card(Rectangle):
    name = ""
    """docstring for Card_manger"""
    def __init__(self,x,y,width,height,color,name):
        super().__init__(x,y,width,height,color)
        self.name  = name

    #ui交互用的方法，检查鼠标指针是否是在本对象范围内
    def check(self,mouse_x,mouse_y):
        if (mouse_x > self.x and mouse_x < self.x+self.width) and (mouse_y > self.y and mouse_y < self.y+self.height):
            return True
        else:
            return False

    #低级方法，移动卡牌
    def move(self,dx,dy):
        #self.opacity=40
        #这里鼠标的x肯定是在mouse_x > self.x and mouse_x < self.x+self.width里面的
        self.x = self.x+dx
        self.y = self.y+dy
        self.draw()

    #我还得加上一些文字啥的
    def draw(self):
        super().draw()
        my_lbl = pyglet.text.Label(self.name,
                          font_name='黑体',
                          font_size=16,
                          x=self.x+10, y=self.y+10)
        my_lbl.draw()


#看了一下可能只能这么调用了
# class Parent:        # 定义父类
#    def myMethod(self):
#       print('调用父类方法')

# class Child(Parent): # 定义子类
#    def myMethod(self):
#       super().myMethod()
#       print('调用子类方法')

# c = Child()          # 子类实例
# c.myMethod()         # 子类调用重写方法

#https://api.arcade.academy/en/latest/tutorials/card_game/index.html
#最有参考价值的文章

class Card_manger():
    #当前的激活卡片，这个只在拖动情况下是有值的
    activeCard = None
    #对象列表
    objects_list = []

    #堆叠列表
    stacks_list = []
    """docstring for Card_manger"""
    def __init__(self):
        pass

    #将卡牌注册到管理器里去
    def reg_obj(self,obj):
        self.objects_list.append(obj)

    #扫描整个管理器，并激活选中的卡牌(drag才行)
    def check(self,mouse_x,mouse_y):
        if self.activeCard ==  None:
            n = 0
            index = -1
            for o in self.objects_list:
                if o.check(mouse_x,mouse_y):
                    print("I am in "+o.name)
                    index = n 
                    #这里从前向后搜索，然后等于是取到最后一个匹配的对象了
                    #card1，card1，这种结构，如果1、2同时满足，那么应该会返回的是card2
                    #index==1的值
                n=n+1
            print("check 结果为："+str(index))
            #扫描完了整个管理器了，如果有结果，则index一定>=0
            if index >= 0:
                tem_obj = self.getObjectFromIdx(index)
                self.activeCard = self.to_top(tem_obj)
            #那么就将拿到的这个card的参数取出，新建一张参数上一模一样的卡牌
            #但是将其append到列表的末尾去，这样下一轮的on_draw会自动帮我们把它置顶,并且返回该卡片
                return self.activeCard
            else:
                #当然了，还有一种情况是用户点击的区域里其实没有任何东西可言
                return None
        else:
            return self.activeCard

    #内部辅助函，外部可以不调用
    def getObjectFromIdx(self,index):
        return self.objects_list[index]

    #内部辅助函，外部可以不调用
    def removeObj(self,obj):
        self.objects_list.remove(obj)

    #复制对象，并将当前对象置顶
    def to_top(self,obj):
        my_x = obj.x
        my_y = obj.y 
        my_width = obj.width
        my_height = obj.height
        my_color = obj.color
        my_name = obj.name
        self.objects_list.remove(obj)
        my_card = Card(x=my_x, y=my_y, width=my_width, height=my_height, color=my_color,name=my_name)
        self.objects_list.append(my_card)
        return my_card

    #on_draw的注册点，遍历整个管理器并draw
    def draw(self):
        for o in self.objects_list:
            o.draw()
            


#square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))
card1 = Card(x=200, y=200, width=60, height=90, color=(255, 55, 255),name=u"第零话")
card2 = Card(x=300, y=300, width=60, height=80, color=(55, 55, 255),name="匪兵乙")


#初始化管理器
cardManger = Card_manger()
#把对象添加给管理器
cardManger.reg_obj(card1)
cardManger.reg_obj(card2)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
        #cardManger.check(x,y)


#https://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html
cursor_default = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)
cursor_hand = window.get_system_mouse_cursor(window.CURSOR_HAND)

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    DragObj = cardManger.check(x,y)
    if DragObj:
        window.set_mouse_cursor(cursor_hand)
        DragObj.move(dx,dy)
    return True

#on_mouse_release(x=160, y=67, button='LEFT', modifiers=)
@window.event
def on_mouse_release(x, y, button, modifiers):
    cardManger.activeCard = None
    window.set_mouse_cursor(cursor_default)

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