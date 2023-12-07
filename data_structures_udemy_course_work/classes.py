

class Cookie:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


cookie_one = Cookie('green')
cookie_two = Cookie('red')

print(cookie_one.get_color())
cookie_one.set_color('orange')
print(cookie_one.get_color())


#pointer
list_1 = {
    'value' : 10
}
list_2 = list_1
print(list_1, list_2)
list_2['test'] = 20
print(list_1, list_2)
