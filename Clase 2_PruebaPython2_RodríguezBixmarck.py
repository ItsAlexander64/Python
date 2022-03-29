ranini=1
ranfin=100
for i in range (ranini,(ranfin+1)):
    if(i%5==0 and i%3==0) :        
     print(i,"FizzBuzz")  
    elif i%3==0:
            print(i,"Fizz")
    elif i%5==0:
            print(i,"Buzz")
    
