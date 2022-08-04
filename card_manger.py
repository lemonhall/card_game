#https://api.arcade.academy/en/latest/tutorials/card_game/index.html
#最有参考价值的文章
from card import Card
# Import math Library
import math
from card_group import CardGroup

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

    #扫描整个管理器，计算中心距离
    def can_be_stack(self):
        if self.activeCard ==  None:
            #当前没有拖动的卡片，那就什么事也不干
            pass
        else:
            #https://pyglet.readthedocs.io/en/latest/modules/shapes.html#pyglet.shapes.Rectangle
            #循环外先把拖动目标的中心点x，和中心点y，咱取了
            #大概明白是怎么回事儿了，这个anchor_x，anchor_y
            #其实主要是为了旋转等操作服务的，也就是说其实这玩意是需要自己去计算的，哎
            #所以我加入了，除以2的逻辑来简单表达
            drag_card_anchor_point = [self.activeCard.x/2,self.activeCard.y/2]
            #扫描整个列表
            for card in self.objects_list:
                if card != self.activeCard:
                    temp_point = [card.x/2,card.y/2]
                    distance=self.anchor_distance(drag_card_anchor_point,temp_point)
                    if distance<15:
                        #如果下面的卡片的卡组不为空
                        if card.getCardGroup():
                            #如果活动卡片的卡组为空
                            if self.activeCard.getCardGroup() == None:
                                #当两张卡片的距离小于15，下面的卡片有卡组，活动的卡片卡组指针为空时
                                #将活动卡片加入到下面的距离小于15的卡片的卡组当中去
                                self.activeCard.joinCardGroup(card.getCardGroup())
                                print("#如果活动卡片的卡组为空")
                                self.print_card_group(card.getCardGroup().getCardsList())
                                #一个工具方法，把自己粘附到卡组上面去
                                self.activeCard.uiAttchToGroup()
                                self.activeCard.sweep_sound.play()
                            #如果活动卡片的卡组不为空？那应该是啥事儿都不做的
                            else:
                                pass
                        #如果下面的卡组为空
                        else:
                        #如果待叠加的卡牌，没有组，那就新建一个，然后把卡牌和拖放的卡牌都弄一个组里面去
                            newCardGroup = CardGroup()
                            card.joinCardGroup(newCardGroup)
                            self.activeCard.joinCardGroup(newCardGroup)
                            #这个时候我甚至可以链式调用，然后下面的两个卡片所指向的卡组应该是同一个
                            print("#如果下面的卡组为空")
                            self.print_card_group(card.getCardGroup().getCardsList())
                            self.print_card_group(self.activeCard.getCardGroup().getCardsList())
                            #一个工具方法，把自己粘附到卡组上面去
                            self.activeCard.uiAttchToGroup()
                            self.activeCard.sweep_sound.play()

                    else:
                        #距离大于15，如果活动卡牌有组，就退组
                        #print("距离>15")
                        #print(self.activeCard.getCardGroup())
                        if self.activeCard.getCardGroup():
                            orig_group = self.activeCard.getCardGroup()
                            print("老子退组了老子退组了老子退组了,退组前打印一下：")
                            self.print_card_group(self.activeCard.getCardGroup().getCardsList())
                            self.activeCard.leaveCardGroup()
                            print("退组后再打印一下原来组的情况：")
                            self.print_card_group(orig_group.getCardsList())
                        else:
                            #print("活动卡牌没有组？？")
                            pass

    #debug目的的函数
    def print_card_group(self,cardsList):
        temlist=[]
        for card in cardsList:
            temlist.append(card.name)
        print(temlist)
        return True

    #内部辅助函数，计算两个中心点的距离
    #直接抄的https://www.w3schools.com/python/ref_math_dist.asp#:~:text=The%20math.,be%20of%20the%20same%20dimensions.
    def anchor_distance(self,p,q):
        return math.dist(p, q)

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
        my_card_group = obj.getCardGroup()
        self.objects_list.remove(obj)
        my_card = Card(x=my_x, y=my_y, width=my_width, height=my_height, color=my_color,name=my_name)
        #再次点击的时候，需要完整的clone对象，并且将置顶后的对象再次加入原对象的卡组
        if obj.getCardGroup():
            my_card.joinCardGroup(my_card_group)
            obj.leaveCardGroup()
        #然后忽然发现这里其实是有一个bug的，就是原来的这个obj啊，应该销毁的，但是我没有，所以这里会有内存泄露
        self.objects_list.append(my_card)
        return my_card

    #on_draw的注册点，遍历整个管理器并draw
    def draw(self):
        for o in self.objects_list:
            o.draw()