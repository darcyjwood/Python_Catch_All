#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#The first line contains an integer, , the number of students.
#The  subsequent lines describe each student over  lines.
#The first line contains a student's name.
#The second line contains their grade.

#if __name__ == '__main__':
    #for _ in range(int(input())):
#name = input()
#score = float(input())
        
#students_grades = ('name' + score)
students_grades = {'Harry' : 37.21, 'Berry' : 37.21, 'Tina' : 37.2, 'Akriti': 41, 'Harsh' : 39}

print(students_grades)
students_grades.keys()
print(sorted(list(students_grades.values())))
x = (sorted(list(students_grades.values())))[1]
print(x)
y = (sorted(list(students_grades.values())))[2]
print(y)

students_grades.sort(key=lambda value: value[2])
print(key)


#print(students_grades.get(37.21))

#for x in students_grades:
#print(list(students_grades.keys [1, 2]))


    #for x, k in students_grades.items():
        #if k == 'x':
        #print(k)


#list(reversed(sorted(my_list)))
#sort('score')
#print(value)
    
    
    
    #second_last = list[0]
    #for x in list[1:]:
        #if x > max:
            #second_last = max
            #max = x
        #elif x < max and x > second_last:
            #second_last = x
    #print(second_last)
        