class TestObject(object):
    value1 = 10
    value2 = 20

    def __init__(self, id_, pw_):
        self.id = id_
        self.pw = pw_

    def show_attribute(self):
        print('My ID :', self.id)
        print('My PW :', '*' * len(self.pw))
        print('Val_1 :', self.value1)
        print('Val_2 :', self.value2)
        print()
        
    def __main__(self):
        print(type(self))        

kay = TestObject('onito', '123456')

print('------------ SHOW ATTRIBUTE -')
kay.show_attribute()

print('------------ CHANGE VALUE.01 -')
kay.value1 += 100
kay.show_attribute()

print('------------ CHANGE PW TO 333 -')
kay.pw = '333'
#print(kay.__pw)
#print(kay._TestObject__pw)
#print(help(TestObject))
kay.show_attribute()
