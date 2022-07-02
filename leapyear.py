def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0: 
        year = leap
        
    #elif (year // 100 == 0 ) and (year // 4 == 0):
        #return leap

year = int(input())
print(is_leap(year))