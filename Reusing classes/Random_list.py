import random
class Role: 
    def __init__(self,role) -> None:
         self.role = role
    def bip(self):
        if self.role == "nhacai":
            xuc_xac = [1,2,4,5,6,2,3,4,5,6,4,5,6]
            return xuc_xac
        else:
            xuc_xac = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
            return xuc_xac

class RandomList:
    def __init__(self,xuc_xac) -> None:
        self.list = xuc_xac

    def get_random_element(self,times):
        x = 0
        for i in range(times):
            i = random.choice(self.list)
            x = x + i
            print(i)
           
            self.list.remove(i)
        print("Tong",x)
        if x > 10:
            print("Tai")
        else:
            print("Xiu")
    
Tung = Role("nhacai")
Duy = Role("nguoi choi")

A = RandomList(Tung.bip())
A.get_random_element(3)


