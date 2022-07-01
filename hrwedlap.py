#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#The first line contains an integer, , the number of students.
#The  subsequent lines describe each student over  lines.
#The first line contains a student's name.
#The second line contains their grade.

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
     
#students_grades.insert({['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]})


    list = [37.21, 37.21, 37.2, 41, 39]
    max = list[0]
    second_last = list[0]
    for x in list[1:]:
        if x > max:
            second_last = max
            max = x
        elif x < max and x > second_last:
            second_last = x
    print(second_last)
        