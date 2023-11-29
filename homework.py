def salary(*args):
    mean= 0
    i=0
    for salary in args:
        mean= salary
        i= 1
    avg= mean/i
    if avg>10000:
        print(f'rich')
    else:
        print(f'poor')
        
salary(100000,100100,11100,10001)

def salary(*args):
    sum= 0
    for item in args:
        sum= sum+item
    mean= sum/len(args)
    return mean
sal= salary(100000,100100,11100,10001)
if sal >= 10000:
    print(f'rich')
else:
    print(f'poor')
        


def name(firstname, lastname):
    print(f'{firstname.capitalize()}{lastname.capitalize()}')
    
name("shreejal", "khanal")

def vowel_st(vowels, string):
    str= f'[{vowels}]'
    return str

vowels = "aeiouAEIOU"
string= "we are peace lover, say no to war"
print(vowel_st(vowels, string))

class Dog:
    def __init__(self, n, b, w):
        self.name = n
        self.breed = b
        self.weight = w
        
p = Dog('Pit_Bull','Pit_bull','25')
print(f'The name of the dog is {p.name}')
print(f'The breed of the dog is {p.breed}')
print(f'The weight of the dog is {p.weight}')

class student:
    principal_name = 'Prof. Dr. Shreejal'
    school_address = 'Kathmandu'
    phone_no = 4878797
    
    def __init__(self, fn, ln, h, w,):
        self.first_name = fn
        self.last_name = ln
        self.height = h 
        self.weight = w
        
a = student('Hari', 'Prasad', '126cm', '76Kg')
print(student.principal_name)
print(student.school_address)
print(student.phone_no)
print(a.first_name)
print(a.last_name)
print(a.height)
print(a.weight)

class student:
    first_name = 'Shreejal'
    last_name = 'Khanal'
    Age = 17
    school_name = 'Deerwalk'
    school_address = 'Sifal'
    
    @classmethod
    def get_student_info(self):
        print(student.first_name) 
        print(student.last_name)
        print(student.Age)
        
    @classmethod
    def get_school_name(cls):
        print(cls.school_name)
        print(cls.school_address)

student.get_student_info()
student.get_school_name()