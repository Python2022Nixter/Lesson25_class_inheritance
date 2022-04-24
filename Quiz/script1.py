from faulthandler import enable


class Person:
    __counter = 0
    
    def __init__(self, email, name, tel):
        self.email = email
        self.name = name
        self.tel = tel
        Person.__counter += 1
        self.id = Person.__counter
    
    def __str__(self) -> str:
        return f"id: {self.id}\nname: {self.name}\nemail: {self.email}\ntel: {self.tel}"
    
    
    def startWorking(self):
        print(f"I'm working, {self.name}")
        

p = Person("n1@gmail.com", "N1", "0123456789")
print(p, p.id)
p.startWorking()
        