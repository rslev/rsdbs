import os
os.chdir('C:\Users\Owner\DBS\Big Data\CA')


# To define mulitable calculations fuctions with two user inputs (a and b)

def calculation(a,b,choice):
# Choice 1 is addtion calculation
    if choice == 1:
        add = a + b
        return 'Calculation of %.2f + %.2f = %.2f'% (a,b,add)  # returns a string output
# Choice 2 is substraction calculation        
    elif choice == 2:
        sub = a - b
        return 'Calculation of %.2f - %.2f = %.2f'% (a,b,sub)  # returns a string output
# Choice 3 is multiphy calculation
    elif choice == 3:
        multi = a*b
        return 'Calculation of %.2f * %.2f = %.2f'% (a,b,multi)  # returns a string output
# Choice 4 is division calculation
    elif choice == 4:
        div = a / float(b)
        return 'Calculation of %.2f / %.2f = %.2f'% (a,b,div)  # returns a string output
# Choice 5 is exponetiate calculation
    elif choice == 5:
        power = a ** b
        return 'Calculation of %.2f by power of %.2f = %.2f'% (a,b,power)  # returns a string output
# Choice 6 is root calculation
    elif choice == 6:
        if b >= 0:
            root = b ** (1 / float(a))
        else:
            if b < 0:
                root = (-(-b) ** (1 / float(a)))
        return 'Calculation of %.2f root of %.2f = %.2f'% (a,b,root)  # returns a string output
# Choice 7 is combination calculation
    elif choice == 7:
        combination = (factorial(a) / (factorial (b) * factorial (a-b)))
        return 'Combination of %d choose %d = %.2f'% (a,b,combination)  # returns a string output
# Choice 8 is permutation calculation
    elif choice == 8:
        premutation = factorial(a) / factorial (a-b) 
        return 'Permutation of %d choose %d = %.2f'% (a,b,premutation)  # returns a string output

# To define multible calculations function with one user input (c)
      
def operation(c,choice):
# Choice 9 is factorial operation      
    if choice == 9:   
        factor = factorial(c)
        return 'Factorial %d! = %d'% (c,factor)  # returns a string output
# Choice 8 is summation operation
    elif choice == 10:   
        sums = summation(c)
        return 'Summation of %d = %d'% (c,sums)  # returns a string output
# Choice 8 is sine operation
    elif choice == 11:   
        sinx = sine(c)
        return '\nSine of %d degrees = %.3f' % (c,sinx)  # returns a string output
# Choice 8 is cosine operation
    elif choice == 12:         
        cosx = cosine(c)
        return '\nCosine of %d degrees = %.3f'% (c,cosx)  # returns a string output
# Choice 8 is tan operation
    elif choice == 13:
        tan = sine(c)/cosine(c)
        return '\nTan of %d degrees = %.3f' % (c,(tan))  # returns a string output

# To define an factorial function using a recursive formula
   
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

# To define an summation function using a while loop

def summation(s):
   the_sum = 0
   i = 1
   while i <= s:
        the_sum = the_sum + i
        i = i + 1
   return the_sum

# To define sine function

def sine(n):
    # Converting degrees to radians
    x = n * 0.0174532925
    # Using Taylor series
    sin = x - (x**3)/factorial(3) + (x**5)/factorial(5) - (x**7)/factorial(7) + (x**9)/factorial(9) - (x**11)/factorial(11) + (x**13)/factorial(13) - (x**15)/factorial(15) + (x**17)/factorial(17) - (x**19)/factorial(19)
    return sin
 
# To define cosine function
      
def cosine(n):
    # Converting degrees to radians
    x = n * 0.0174532925
    # Using Taylor series    
    cos = 1 - (x**2)/factorial(2) + (x**4)/factorial(4) - (x**6)/factorial(6) + (x**8)/factorial(8) - (x**10)/factorial(10) + (x**12)/factorial(12) - (x**14)/factorial(14) + (x**16)/factorial(16) - (x**18)/factorial(18)
    return cos        
    

if __name__ == '__main__':

    # To handle menu function
    def show_menu():
        print '\n'
        print '#########################################'
        print 'Select 1 for an Addtion operation.'
        print 'Select 2 for an Substraction opearation.'
        print 'Select 3 for an Multiplication operation.'
        print 'Select 4 for an Divison operation.'
        print 'Select 5 for an Exponetiate operration.'
        print 'Select 6 for an Root operation.'
        print 'Select 7 for an Combination operation.'
        print 'Select 8 for an Permutation operation.'
        print 'Select 9 for an Factorial operation.'
        print 'Select 10 for an Summation operation.'
        print 'Select 11 for an Sine operation.'
        print 'Select 12 for an Cosine operation.' 
        print 'Select 13 for an Tan operation.'    
        print 'Select Q to quit program.'
        print '#########################################'
    
    # To define an float function from a user input
         
    def strnuminput(str):
    # While loop     
        while True:
            str_input = raw_input(str)
    # To handle the unexpected         
            try:
                fl_value = float(str_input)
            except:
                print '\nInput must be numeric value.'
                continue
            return fl_value
     
    # To define an integer function from a user input
         
    def strintinput(string):
    # While loop    
        while True:
            str_input = raw_input(string)
    # To handle the unexpected 
            try:
                int_value = int(str_input) 
            except:
                print '\nInput must be integer number'
                continue
            return int_value
     
    # While loop
    while True:   
        show_menu()
        str_inp = raw_input('\nPlease enter menu choice: ')
        if str_inp.lower() == 'q':
            break
    # To handle the unexpected  
        try:
            choice = int(str_inp) 
        except:
            print 'Invalid input'
            raw_input("\nPress 'Enter' to return back to main menu: ")
            continue
        
    # To keep user within loop untill they have chosen correctly    
        if choice < 1 or choice > 13:
            print 'Invalid input'
            raw_input("\nPress 'Enter' to return back to main menu: " )  
            continue
        
    # To handle two inputs by user for menu choice 1 to 6      
        if choice >=1 and choice <= 6:   
            num_a = strnuminput('\nEnter your first number: ')
            num_b = strnuminput('\nEnter your second number: ')
            
    # To handle calculation output and some expected errors     
            if choice == 4 and num_b == 0:
                print '\nUnable to perform division calculation as the second value is Zero.'
            elif choice == 6 and (num_b < 0 and num_a % 2 == 0):
                print '\nUnable to perform even root calculation of a negative number.'
            elif choice == 6 and num_b == 0:
                print '\nUnable to perform root calculation as the second value is Zero.' 
            else:
    # To call calculation function and do calaculation from choicen menu
                calc = calculation(num_a,num_b,choice)
    # Prints output from the choicen calculation.
                print calc 
                
    # To allow user to quit or continue program.
            str_inp = raw_input("\nQ to quit\ Press 'Enter' to return to main menu: \n")
            if str_inp.lower() == 'q':
                break  
    
    # To handle two integer inputs by user for menu choice 7 to 8 
        elif choice >= 7 and choice <= 8:   
            num_a = strintinput('\nEnter your first number: ')
            num_b = strintinput('\nEnter your second number: ')
                 
    # To handle calculation output and some expected errors             
            if (choice == 7 and (num_b > num_a)) or (num_a < 0 or num_b < 0):
                print '\nUnable to perform Combination calculation as at least one of the values are unsuitable.'  
            elif (choice == 8 and (num_b > num_a)) or (num_a < 0 or num_b < 0):
                print '\nUnable to perform Permutation calculation as at least one of the values are unsuitable.'
            else:
    # To call calculation function and do calaculation from choicen menu.
                calc = calculation(num_a,num_b,choice)
    # Prints output from the choicen calculation.
                print calc 
                
    # To allow user to quit or continue program.
            str_inp = raw_input("\nQ to quit\ Press 'Enter' to return to main menu: \n")
            if str_inp.lower() == 'q':
                break 
               
    # To handle single integr input by user for menu choice 9 to 10
        elif choice >= 9 and choice <= 10:
            num_a = strintinput('\nEnter your chosen integer number: ')
            
    # To handle calculation output and some expected errors        
            if (choice == 9 and num_a < 0) or (choice == 10 and num_a < 0):
                print '\nUnable to perform factorial calculation as input value is not a postive integer'
            else:
    # To call operation function and do calaculation from choicen menu.            
                calculation = operation(num_a,choice)
    # Prints output from the choicen calculation.            
                print calculation
                
    # To allow user to quit or continue program.            
            str_inp = raw_input("\nQ to quit\ Press 'Enter' to return to main menu: \n")
            if str_inp.lower() == 'q':
                break 
            
    # To handle single input by user for menu choice 11 to 13
        elif choice <=13 and choice >= 11:
            num_a = strnuminput('\nEnter your chosen number: ')
            
    # To handle calculation output and expected errors        
            if (choice == 13 and num_a % 90 == 0 and num_a % 180 !=0):
                print '\nUnable to perform tan of %d degrees' % (num_a)
            else:
    # To call operation function and do calaculation from choicen menu.            
                calculation = operation(num_a,choice)
    # Prints output from the choicen calculation.            
                print calculation
    
    # To allow user to quit or continue program.            
            str_inp = raw_input("\nQ to quit\ Press 'Enter' to return to main menu: \n")
            if str_inp.lower() == 'q':
                break   
    # To inform user that the program has finished.       
    print '\nThis program has finish.\nThank you !'
