
class Dog:
    def __init__(self):
        self.flag_bark = True
        
    def cutSungdae(self):
        self.flag_bark = False
class Bird:
    def __init__(self):
        self.idx_fly = 0
    def training(self):
        self.idx_fly += 1
    def traing_hard(self,power):
        self.idx_fly += power

class GaeSae(Dog,Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        self.flag_kill = True
    
    def usekill(self):
        self.flag_kill = False
        
    
if __name__ == '__main__':
    gs = GaeSae()
    print(gs.flag_bark)
    print(gs.idx_fly)
    print(gs.flag_kill)
    
    gs.cutSungdae()
    gs.traing_hard(5)
    gs.usekill()
    
    print(gs.flag_bark)
    print(gs.idx_fly)
    print(gs.flag_kill)
    