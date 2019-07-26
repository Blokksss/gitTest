class new:
    
    def __init__(self, name):
        self.name = name

    def showName(self):
        print("his name is {}".format(self.name))

    def getPersonCome(self):
        result_str = ''
        start_word = self.name[0]
        list_upper = ['A', 'B', 'C', 'D','E', 'F','G', 'H', 'I', 'J', 'K', 'L' ,'M' ,'N' ,'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k' ,'l', 'm' , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if start_word in list_upper:
            result_str = "{} is upper man!".format(self.name)
        elif start_word in list_lower:
            result_str = "{} is lower man".format(self.name)
        else:
            result_str = "{} is a supperman".format(self.name)
        return result_str


if __name__ == '__main__':
    p = new('6Blokks')
    p.showName()
    print(p.getPersonCome())
