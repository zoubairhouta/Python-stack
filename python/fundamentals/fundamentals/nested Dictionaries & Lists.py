#1  Update Values in Dictionaries and Lists

#1
x = [ [5,2,3], [10,8,9] ]
students = [
 {'first_name': 'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
 'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

#2
students[0]['last_name']='Bryan'

print(students[0]);

# 3
sports_directory['soccer'][0] = 'Andres'

#4
z[0]['y']=30;

print(z[0]);


Iterate through a list of dictionnaries

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
def iterateDictionary(students):
    for student in students:
        for key, value in student.items():
            print(f"first_name: {key} - last_name: {value}")


iterateDictionary(students)



# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel





def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2("first_name", students)


iterateDictionary2("last_name", students)



#4th assignment

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key}")
        for item in value:
            print(item)
        print()

# Example usage:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
