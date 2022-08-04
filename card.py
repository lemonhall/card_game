from card_group import CardGroup
from pyglet.shapes import Rectangle
import pyglet

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


#https://pyglet.readthedocs.io/en/latest/modules/shapes.html
#Card对象，直接继承于Rectangle类
#id，type这些估计以后都需要的
class Card(Rectangle):
    name = ""
    card_group = None
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

    #将cardgroup的指针返回给外界
    def getCardGroup(self):
        return self.card_group

    #加入某个卡组
    def joinCardGroup(self,cardGroup:CardGroup):
        #加入某个卡组，处理完一系列的成功或者意外情况之后，需要一定的逻辑
        cardGroup.join(self)
        #将自己card_group指针，和外界传过来的做好链接
        self.card_group = cardGroup
        return True

    #退出当前的卡组
    def leaveCardGroup(self):
        #这里不需要提供参数的原因，很简单，因为自身持有了card_group指针
        if self.card_group == None:
            #对外抛出错误,你不能离开一个空的卡组
            print("You cannot leave a blank card group")
            raise Exception("You cannot leave a blank card group")
        else:
            #调用卡组的remove方法，把自己剔除出卡组
            self.card_group.remove(self)
            #最后一步肯定是断开指针联系
            self.card_group = None
        return True

###END OF CARD CLASS