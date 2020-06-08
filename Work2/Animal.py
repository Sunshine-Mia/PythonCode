import yaml
class Animal():
    def __init__(self, name = 'default', color = 'white', age = 1, gendar = 'male'):
        self.name = name
        self.color = color
        self.age = age
        self.gendar = gendar

    def call(self):
        return f"{self.name} calls."

    def run(self):
        return f"{self.name} runs."


class Cat(Animal):
    def __init__(self, name = 'default', color = 'white', age = 1, gendar = 'male', hair = 'short hair'):
        self.name = name
        self.color = color
        self.age = age
        self.gendar = gendar
        self.hair = hair

    def call(self, call = '喵喵叫'):
        return f"{self.name} calls {call}"

    def catching_mice(self, catched = False):
        if(catched == True):
            return "捉到了老鼠"
        else:
            return "没捉到老鼠"


class Dog(Animal):
    def __init__(self, name='default', color='white', age=1, gendar='male', hair='long hair'):
        self.name = name
        self.color = color
        self.age = age
        self.gendar = gendar
        self.hair = hair

    def call(self, call = "汪汪叫"):
        return f"{self.name} calls {call}"

    def watching_house(self):
        return f"{self.name} 在看家"


if __name__ == '__main__':
    with open("Property.yml") as f:
        p = yaml.safe_load(f)
    tom = Cat(p[0]['cat']['name'], p[0]['cat']['color'], p[0]['cat']['age'], p[0]['cat']['gendar'], p[0]['cat']['hair'])
    print(f"{tom.name} {tom.catching_mice(True)}")
    print(f"{tom.name}, {tom.color}, {tom.age}, {tom.gendar}, {tom.hair}, {tom.catching_mice(True)}")

    puppy = Dog(p[1]['dog']['name'], p[1]['dog']['color'], p[1]['dog']['age'], p[1]['dog']['gendar'], p[1]['dog']['hair'])
    print(puppy.watching_house())
    print(f"{puppy.name}, {puppy.color}, {puppy.age}, {puppy.gendar}, {puppy.hair}")