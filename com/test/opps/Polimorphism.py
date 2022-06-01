class Bird:
    def intro(self):
        print("There are many type of birds")

    def flight(self):
        print("Most of the bird can fly but some can't")

class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def flight(self):
        print("Ostrich can't fly")


obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.flight()
print("..........")
obj_sparrow.intro()
obj_sparrow.flight()
print("-----------")
obj_ostrich.intro()
obj_ostrich.flight()
