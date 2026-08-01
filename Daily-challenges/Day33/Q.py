class Bird:
    def fly(self):
        return "Some birds fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

def make_it_fly(bird_obj):
    print(bird_obj.fly())

make_it_fly(Penguin())
