class User:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if value < 0:
            raise ValueError("Age manfiy bo'lishi mumkin emas")
        self._age = value


user = User(20)

print(user.get_age())
user.set_age(25)
print(user.get_age)