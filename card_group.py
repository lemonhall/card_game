

#思索再三我应该抽象出来一个叫CardGroup的概念，然后整个manger可以管理全部的CardGroup
#一张卡牌，只能属于某一个group
class CardGroup():
    card_list = []
    """docstring for Card_manger"""
    def __init__(self):
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