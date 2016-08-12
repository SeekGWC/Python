# ========================================================================================================
# ========================================= INSTRUCTIONS =================================================
# ========================================================================================================
# 1. With a partner, comment out each part of the code individually. To comment/uncomment, press ctrl-/ 
# 2. Read the code and try to understand it.
# 3. If you do not understand, raise your hand and ask a teacher or TA. 
# 4. Before you run the code, try to guess what the code will output. 
# 5. Finally, run the code.


# # ========================================================================================================
# # ========================================= PART ONE =====================================================
# # ========================================================================================================

# # this is how you write a function!

# # a parameter is a variable representing your input to the function
# def my_first_function(parameter):
# 	# use an indent to show the code inside of the function

# 	# anything can go in a function!
# 	print("This is my first function!")

# 	# the parameter is a variable that is set when calling the function
# 	print("My parameter is just like any other variable. See: " + parameter)

# 	# the parameter only exists inside the function. once you exit the function, the parameter no longer exists.

# 	# a function is simply a definition - it is defining an action. when you run this code so far, nothing will be printed yet!

# # ========================================================================================================
# # ======================================== PART TWO ======================================================
# # ========================================================================================================

# # you "call" a function to make the code inside of it run.

# # this is how you 'call' a function. you write what you want to input as a parameter between the parentheses.
# my_first_function("hello!") # note: here is where the parameter is set as "hello!"

# # you can call it again with different parameters
# my_first_function("hello again!")

# # but remember that parameters only exist inside of the function!
# # this code creates an error:
# # print(parameter)

# # ========================================================================================================
# # ======================================== PART THREE ======================================================
# # ========================================================================================================

# # functions can also have multiple parameters, or no parameters

# def more_params(parameter_1, parameter_2):
# 	print("Paramter one is " + parameter_1 + ". Parameter two is " + parameter_2)

# def no_params():
# 	print("I have no parameters!")

# # let's call it again
# more_params("duck", "telephone")
# no_params()

# # ========================================================================================================
# # ======================================== PART FOUR ======================================================
# # ========================================================================================================

# # functions can also answer questions by outputting data using the "return" statement.

# # for example, if we wanted to write a function that outputs a value, x, squared...
# def square(x):
# 	# the return keyword outputs, or 'returns', a value
# 	return x*x

# # you can save the output in a variable
# two_squared = square(2)

# # you can also print the output by calling the function within the print statement (which is itself a function!)
# print("Two squared is " + str(square(2))) # remember -- str() here is a function that casts integers to strings!

# # if you call the function without saving it, nothing happens
# print("Nothing prints here.")
# square(2) # this does not save or print out 4. you have to explicitly tell Python to do that!

# # ========================================================================================================
# # ======================================== PART FIVE ======================================================
# # ========================================================================================================

# # IMPORTANT: return is an 'exit button'. that is, return exits you out of the function. no code beyond return is executed!

# def broken_return(some_string):
# 	return some_string
# 	print "Hello! Can anyone hear me?" # this will not print

# # this will only print some_string. It will not print Hello! Can anyone hear me?
# print(broken_return("hello. it's me.")) 

# # ========================================================================================================
# # ======================================== PART SIX ======================================================
# # ========================================================================================================

# # order matters! Python reads top to bottom. just like how you have to make something before you can use it, you have to define a function before you call it.

# # this code will cause an error:
# # ---------------------------------------
# # not_yet_defined() 
# # def not_yet_defined():
# # 	print("hello!") # ERROR!!
# # ---------------------------------------
# # but this will work:

# def not_yet_defined():
# 	print("this is defined now!")

# not_yet_defined() # because you are calling the function after you have defined it.

# # ========================================================================================================
# # ======================================== PART SEVEN ======================================================
# # ========================================================================================================

# # finally, just like conditionals and loops, you can nest functions inside of other functions and call functions within other functions

# # we are going to use the square() function we wrote earlier.

# # this function returns x^3
# def cubed(x):
# 	return x*x*x

# # this function calls square, which we can use because we defined it earlier (order matters!)
# def quadrupuled(x):
# 	return square(x) * square(x) # this does (x^2) * (x^2)

# print("(2^3)^4 is: " + str(((2**3)**4))) # we compute just using arithmetic operators
# print("(2^3)^4 is: " + str(quadrupuled(cubed(2)))) # we compute using our functions

# # ========================================================================================================
# # ========================================================================================================
# # ========================================================================================================
# # ========================================================================================================
# # ========================================================================================================

# # If you have time, work on the following tasks:

# # ========================================================================================================
# # ======================================== TASKS =========================================================
# # ========================================================================================================

# # Create a new file called tasks.py on your Desktop. All functions for these Tasks will go in this file. 
# # Test that each task works before moving on to the next one.

# # Task 1. 
# # rocks(): a zero parameter function
# # Write a function called rocks() that prints "Girls Who Code rocks!" when invoked.
# # This is called a zero parameter function because it has zero parameters. 
# # Remember that, even if you have zero parameters, you still need th double parentheses!

# # Task 2.
# # custom_rocks(x): a single parameter function
# # Write a function called custom_rocks(x) that prints a customized message when invoked.
# # custom_rocks("GWC") ==> this will print, GWC rocks!
# # custom_rocks("hippo") ==> this will print, hippo rocks!

# # Task 3.
# # roll_a_die(): a function that returns something
# #
# # For this function, we will use the library "random" 
# # In order to use this library, type this on the very first line of your file (line 1):
# # import random
# #
# # We will use the random library's randint() function, which uses this syntax:
# # random.randint(a, b) # returns a random integer between a and b
# # An example of this function in use:
# # random.randint(1, 3) # returns a random number between 1 and 3
# # num = random.randint(1, 3)
# # print(num) # prints the random number
# # 
# # Write a function called roll_a_die that uses the random.randint() function to return a random 
# # number between 1 and 6, simulating a die roll.
# # roll_a_die() ==> returns 3 (but prints nothing!)
# # die = roll_a_die() ==> saves the result of roll_a_die, 3, in the die variable
# # print(die) ==> prints 3
# # 
