class Worker:
    def __init__(self, name, age):
        self.name = name #Public attribute
        self.__age = age #Private attribute using double underscore

    def get_age(self):
            return self.__age  # Method to access the private attribute
     
    def set_age(self, age):
         if age > 0:
              self.__age = age
         else:
              print("Invalid  age")

worker = Worker("Alice", 30)
print(worker.name)  # Accessing public attribute
print(worker.get_age())   # Accessing private attribute through a method
worker.set_age(35)   # Modifying private attribute through a method

                  

