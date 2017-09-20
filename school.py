from eit import Eit
from fellow import Fellow


class School:
    def __init__(self):
        self.fellows = []
        self.eits = []
        seek = 0
        try:
            f = open('eits.csv', 'r')
            f.close()
        except:
            with open('eits.csv', 'w') as f:
                f.close()

        with open('eits.csv', 'r') as eits:
            for eit in eits:
                if seek == 0:
                    seek += 1
                    continue
                if len(eit) >= 1:
                    eit = eit.strip('\n').split(',')
                    eit = Eit(name=eit[0], nationality=eit[1])
                    self.eits.append(eit)

    def add_eit(self):
        done = False
        while not done:
            try:
                eit_ = Eit()
                self.eits.append(eit_)
                done = True
            except ValueError:
                print('Invalid nationality. [Ghana, Nigeria, Ivory Coast, Kenya, South Africa]')

    def add_fellow(self):
        fellow_ = Fellow()
        self.fellows.append(fellow_)


