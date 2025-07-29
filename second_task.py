with open('cats_info.txt', 'w+', encoding = 'utf-8') as file:
    file.write('60b90c1c13067a15887e1ae1,Tayson,3\n'
'60b90c2413067a15887e1ae2,Vika,1\n'
'60b90c2e13067a15887e1ae3,Barsik,2\n'
'60b90c3b13067a15887e1ae4,Simon,12\n'
'60b90c4613067a15887e1ae5,Tessi,5\n')

'''
function which reads a text  file and returns a list of dictionaries with information about each cat

input: path(str) - path to text file
output: list(dict) - list of dictionaries with information about each cat
'''
def get_cats_info(path:str)->list:
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            lines =[el.strip() for el in file.readlines()]
            list_of_cats = []
            cats = {}
            for line in lines:
                part = line.split(',')
                list_of_cats.append({'id': part[0], 'name': part[1], 'age': part[2]})
        return list_of_cats
    except FileNotFoundError:
        print('File not found.')


cats_info = (get_cats_info('/Users/hanna/Desktop/PROJECTS/goit-algo-hw-04/cats_info.txt'))
print(cats_info)
