class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f' this is my value {self._value}')

    # this is getter
    @property
    def ten_value(self):
        return 10*self._value
    #this is setter
    @ten_value.setter
    def ten_values(self,new_values):
        self._value = new_values


obj=MyClass(10)
print(obj.ten_value)
obj.ten_values = 20
print(obj.ten_values,'this is ten values')
obj.show()