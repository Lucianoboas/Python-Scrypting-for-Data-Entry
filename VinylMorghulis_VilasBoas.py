# The comeback of Vinyl Records is real and the sales continue to grow every year. 

# This program was designed to help vinyl collectors to budget their future purchasing
# and help them to keep track of their collection. The focus it's not on what has been spent
# in the past (the user's past amount spent on buying records).

# Although I'm mentioning the idea of best and worst scenarios here, this code
# by no means explores the details of Cash-Flow, NPV, IRR, Payback, Valuation etc
# The scenarios will be based on the monthly budget a user have set themselves.

# The average price of a vinyl record varies a lot - it can litteraly go from a few cents
# to thousands of dollars, all depends on a miriade of different factors.
# For that reason, the user will type the average price that best fits his/her reality.

# Importing Pandas to design a summarized table:
from pandas import Series, DataFrame
from time import *
sleep (5)

# defining main function:
def main():
    # setting up constants:
    BEST_SCENARIO = .2  # I didn't want to allow the user to insert the percent.
    WORST_SCENARIO = .35 # I didn't want to allow the user to insert the percent.
    YEAR = 12
    # printing out initial message:
    print("LET'S BUDGET YOUR PURCHASES AND FORECAST YOUR VINYL COLLECTION FOR THE NEXT 12 MONTHS:")
    print()
    print('*Remember to hit "Enter" to move to the next sections*')
    
    # asking for user's input:
    my_collection = int(input("How many records do you currently have in your collection? "))
    
    # setting up auto messages upon certain conditions:
    if my_collection <= 200:
        print('         "Records you must buy, my young padawan"')
        
    elif my_collection <= 999:
        print('             "The Vinyl is strong with this one"')
            
    elif my_collection >= 1000:
        print('                "May the Vinyl be with you"')
    
    # forcing user to hit "enter" in order to keep the program running:     
    input()    
    
    # ...asking for user's input:
    my_average = float(input("What is the average price you pay for a record $"))
    my_budget = float(input("How much do you plan to spend per month $"))
    print()
    
    # setting up base case scenario:
    records_number = my_budget / my_average
    forecast_year = records_number * YEAR + my_collection
    total_spent = my_budget * YEAR
    
    # printing out base case scenario message:
    print("Assuming you'll keep the same budget, in one year you'll have a total of",
          '{:,.0f}'.format(forecast_year), "records, and spent about " '${:,.2f}'.format(total_spent))
    print()
    
    # forcing user to hit "enter" in order to keep the program running:     
    input() 
    
    # Best and Worst Case Scenarios were based on the user keeping the same average price for a record,
    # but the monthly budget will increse or decrease based on the top-down constants.
    # So, we will have the same average price for all scenarios but budget will depend on percents of each scenarios.
    
    # setting up best case scenario:
    wonderland_records_n = my_budget * BEST_SCENARIO + my_budget
    wonderland_records = wonderland_records_n / my_average * YEAR + my_collection
    wonderland_budget = wonderland_records_n / my_average * YEAR * my_average
    
    # printing out best case scenario message:
    print("In a Best Case Scenario a", '{:.0f}%'.format(BEST_SCENARIO*100),
          "increment in your budget would give you a total of", '{:,.0f}'.format(wonderland_records),
          "records, and spent of", '${:,.2f}'.format(wonderland_budget) )
 
    # forcing user to hit "enter" in order to keep the program running:     
    input() 

    # setting up out worst case scenario:
    cruel_world_records_n = - my_budget * WORST_SCENARIO + my_budget 
    cruel_world_records = cruel_world_records_n / my_average * YEAR + my_collection
    cruel_world_budget = cruel_world_records_n / my_average * YEAR * my_average
    
    
    # printing out worst case scenario message:
    print("In a Worst Case Scenario a", '{:.0f}%'.format(WORST_SCENARIO*100),
          "decrease in your budget would give you a total of", '{:,.0f}'.format(cruel_world_records),
          "records, and spent of", '${:,.2f}'.format(cruel_world_budget) )

    # forcing user to hit "enter" in order to keep the program running:     
    input() 
    
    # creating DataFrame to show the summarized scenarios: 
    et_vinyl_home = {'Average Price': ['${:.2f}'.format(my_average), '${:.2f}'.format(my_average), '${:.2f}'.format(my_average)],
                      'Montly Budget': ['${:.2f}'.format(my_budget), '${:.2f}'.format(wonderland_records_n), '${:.2f}'.format(cruel_world_records_n)],   
                      'Total Records': ['{:.0f}'.format(forecast_year), '{:.0f}'.format(wonderland_records), '{:.0f}'.format(cruel_world_records)],
                      'Total Investment': ['${:.2f}'.format(total_spent), '${:.2f}'.format(wonderland_budget), '${:.2f}'.format(cruel_world_budget)]}
        
    # Customizing indexes:
    delorean_scenarios = ['Base Case Scenario', 'Best Case Scenario', 'Worst Case Scenario']  
    my_precious_table = DataFrame(et_vinyl_home, index = delorean_scenarios)
    
   # printing out DataFrame:
    print("Here is Your Summarized Table with Expected Scenarios:")
    print('______________________________________________________________________________')        
    print(my_precious_table)  
    print('______________________________________________________________________________')        

    # forcing user to hit "enter" to close the program:     
    input()
    
    
# calling main function:
main()

