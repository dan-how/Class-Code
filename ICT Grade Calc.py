john = { "name":"John Smith", 
         "assessment" : [90], 
         "homework" : [75], 
         "final" : [90.20] 
       } 
         
dan = { "name" : "Dan How", 
        "assessment" : [56], 
        "homework" : [56], 
        "final" : [40.6] 
      } 
   
def get_average(marks): 
    total_sum = sum(marks) 
    total_sum = float(total_sum) 
    return total_sum / len(marks) 
  
def calculate_total_average(students): 
    assessment = get_average(students["assessment"]) 
    homework = get_average(students["homework"]) 
    final = get_average(students["final"]) 

    return (0.35 * assessment +
            0.4 * final + 0.25 * homework) 
  
  
# Calculate letter grade of each student 
def letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    elif score >= 50: return "E"
    else : return "F"
  
students = [john, dan] 
  
for i in students : 
    print(i["name"])
    print("------------")                    
    print("Letter Grade", letter_grade(calculate_total_average(i)))
    print("Average marks" , calculate_total_average(i))
    print() 
  
