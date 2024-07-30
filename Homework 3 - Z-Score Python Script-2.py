def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                

# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	                  #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    Returns the z-score of x
    """
    
    # Participating group member names go in this comment: Samuel Mock, Samantha Simpkins, Will McWain
    
    # Your code goes between this comment and the return
    numerator = x - mu
    denominator = sigma
    return numerator/denominator

#TESTING

min_population1 = min(population1)
min_population2 = min(population2)
min_population3 = min(population3)
max_population1 = max(population1)
max_population2 = max(population2)
max_population3 = max(population3)

#Testing Z score for the minimum value in each data set

print("\n\t\tFor the minimum value of Population 1:")
print("The z-score of",min_population1,"is",(z_score(min_population1,mean(population1),stdev(population1,mean(population1)))))

print("\n\t\tFor the minimum value of Population 2:")
print("The z-score of", min_population2, "is", (z_score(min_population2, mean(population2), stdev(population2, mean(population2)))))

print("\n\t\tFor the minimum value of Population 3:")
print("The z-score of", min_population3, "is", (z_score(min_population3, mean(population3), stdev(population3, mean(population3)))))

#Testing Z score when population is less than mean

filter_values_less_population1 = [x for x in population1 if x < mean(population1) and x > min_population1]
filter_values_less_population2 = [x for x in population2 if x < mean(population2) and x > min_population2]
filter_values_less_population3 = [x for x in population3 if x < mean(population3) and x > min_population3]

import random

ran_less_population1 = random.choice(filter_values_less_population1)
ran_less_population2 = random.choice(filter_values_less_population2)
ran_less_population3 = random.choice(filter_values_less_population3)

print("\n\t\tFor Population 1 value less than the mean:")
print("The z-score of",ran_less_population1,"is",(z_score(ran_less_population1,mean(population1),stdev(population1,mean(population1)))))

print("\n\t\tFor Population 2 value less than the mean:")
print("The z-score of",ran_less_population2,"is",(z_score(ran_less_population2,mean(population2),stdev(population2,mean(population2)))))

print("\n\t\tFor Population 3 value less than the mean:")
print("The z-score of",ran_less_population3,"is",(z_score(ran_less_population3,mean(population3),stdev(population3,mean(population3)))))

#Testing Z score when population item is greater than mean

filter_values_greater_population1 = [x for x in population1 if x > mean(population1) and x < max_population1]
filter_values_greater_population2 = [x for x in population2 if x > mean(population2) and x < max_population2]
filter_values_greater_population3 = [x for x in population3 if x > mean(population3) and x < max_population3]

ran_greater_population1 = random.choice(filter_values_greater_population1)
ran_greater_population2 = random.choice(filter_values_greater_population2)
ran_greater_population3 = random.choice(filter_values_greater_population3)

print("\n\t\tFor Population 1 value greater than the mean:")
print("The z-score of",ran_greater_population1,"is",(z_score(ran_greater_population1,mean(population1),stdev(population1,mean(population1)))))

print("\n\t\tFor Population 2 value greater than the mean:")
print("The z-score of",ran_greater_population2,"is",(z_score(ran_greater_population2,mean(population2),stdev(population2,mean(population2)))))

print("\n\t\tFor Population 3 value greater than the mean:")
print("The z-score of",ran_greater_population3,"is",(z_score(ran_greater_population3,mean(population3),stdev(population3,mean(population3)))))

#Testing Z score for the maximum value in each data set

print("\n\t\tFor the maximum value of Population 1:")
print("The z-score of",max_population1,"is",(z_score(max_population1,mean(population1),stdev(population1,mean(population1)))))

print("\n\t\tFor the maximum value of Population 2:")
print("The z-score of", max_population2, "is", (z_score(max_population2, mean(population2), stdev(population2, mean(population2)))))

print("\n\t\tFor the maximum value of Population 3:")
print("The z-score of", max_population3, "is", (z_score(max_population3, mean(population3), stdev(population3, mean(population3)))))
