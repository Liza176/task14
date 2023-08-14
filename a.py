# class Crafts:
#     pass
# class Easy(Crafts):
#     def time_fast(self):
#         print('Вы сделали очень быстро')
# class Hard(Crafts):
#     def time_long(self):
#         print('Вы делали очень долго')
# class Beads(Hard):
#     def amigurumi(self):
#         print('Вы набрали 100 подпищиков в тт ')
# class Plastilin(Hard):
#     def drakon(self):
#         print('Вы получили 10 балов по художке ')
# class Paper(Easy):
#     def origami(self):
#         print('У вас получился красивый дракон ')
# class Nitki(Easy):
#     def shapka(self):
#         print('У вас новая игрушка на елку ')

# me = Plastilin()
# me.drakon()
    
# class Person:
#     def __init__(self,name) :
#         self.name = name
#     def skishi(self):
#         print('Пр')
#     def say(self):
#         print('Привет')    

# liza = Person('Лиза')

# class About:
#     def say(self,nam,fraz):
#         print(nam,fraz)
# name = input('Ваше имя ')
# fraza = input('Ваша фраза ')
# res = About()
# res.say(name,fraza)


class Math:
    otv1 = 9 - 14
    otv2 = 6 * 6
    otv3 = 586 - 7
    def __init__(self,res1,res2,res3) :
        self.res1 = res1
        self.res2 = res2
        self.res3 = res3
        
    def yes(self):
        print('Верно, Молодец')
    def no(self):
        print('Не верно, Иди учись') 

you = Math 
vopros = int(input('9 - 14 ')) 



you = Math(vopros)
if you.res1 == you.otv1:
        print(1)
        you.yes()
else:
        print(2)
        you.no()



