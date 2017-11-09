class Mother:
    def message1(self):
        print("Hello from Mother")

class Father:
    def message2(self):
        print("Hello from Father")

class Child(Mother, Father):
    def message3(self):
        print("Hello from Child")
        Mother.message1(self)


Ryan = Child()
Ryan.message3()
