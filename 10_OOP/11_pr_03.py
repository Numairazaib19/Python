# it doesnot change the class attribute
class Sample:
    a = "nemo"
    
obj = Sample()
obj.a = "Lily"      # it set new instance variable
print(Sample.a)
print(obj.a)


# what if we want to change class attribute
class Sample:
    a = "nemo"
    
obj = Sample()
Sample.obj = "Lily"  # it changes the class attribute
print(Sample.obj)
