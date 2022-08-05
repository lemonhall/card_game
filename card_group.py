

#思索再三我应该抽象出来一个叫CardGroup的概念，然后整个manger可以管理全部的CardGroup
#一张卡牌，只能属于某一个group
class CardGroup():
    card_list = []
    processBar = None
    batch = None
    """docstring for Card_manger"""
    def __init__(self,batch):
        self.batch=batch
        pass

    #卡牌会使用joinCardGroup(self,cardGroup:CardGroup)来加入某个卡组
    def join(self,card):
        self.card_list.append(card)
        return self

    #从卡组列表当中剔除掉这张卡
    def remove(self,card):
        try:
            self.card_list.remove(card)
        except Exception as e:
            #防御性质的编程
            print("CardGroup->remove ERROR: There is no card in card_list")
            print(e)
            return False
        else:
            return True

    #返回所有的牌
    def getCardsList(self):
        return self.card_list

    #给这个卡组附加上一个头顶的进度条组件
    def uiAttchProcessBar(self,processBar):
        #试图去取卡组的第一张牌
        prime_card = self.card_list[0]
        #如果卡组的第一个元素是存在的
        if prime_card:
            px = prime_card.x
            py = prime_card.y + 80
            pwidth = 5   #初始的宽度，给5个像素吧
            pheight = 10
            #以上四个参数取自于card的大小，这个以后再说
            color=(255, 0, 0)

            processBar.x=px
            processBar.y=py
            processBar.width = pwidth
            processBar.height = pheight
            processBar.color = color

        self.processBar=processBar

    #返回这个卡组的进度条组件
    def getProcessBar(self):
        return self.processBar

    #移除这个卡组的进度条组件
    def removeProcessBar(self):
        self.processBar = None
