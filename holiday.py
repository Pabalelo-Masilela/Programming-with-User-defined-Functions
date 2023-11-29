'''This program serves to calculate and display in a user friendly manner, the cost of a users holiday, including plane costs,hotel costs and car rental costs.'''
# user input for calculations to be made.
city_flight = input('''Choose and enter an option from below:
a - Johannesburg
b - Durban
c - Cape Town
d - Port Elizabeth \n''')
num_nights = int(input("Enter number of nights for stay:\n"))
rental_days = int(input("Enter number of days for car hire:\n"))

# creating a function for hotel cost calculation
def hotel_cost(num_nights, cost = 950): 
        return cost * num_nights
       


# creating a function for plane cost calculation
def plane_cost(city_flight):
    if city_flight == "a":
        return 1200
        
    elif city_flight == "b":
        return 1500        
    elif city_flight == "c":
        return 2000        
    elif city_flight == "d":
        return 1000    
    else:
        print("Invalid flight city input.")

# creating a function for car hire calculation
def car_rental(rental_days, rental_fee = 350):
  return rental_days * rental_fee

# creating a function to calculate all holiday costs
def holiday_cost(hotel_cost, plane_cost, car_rental):
    hotel_calculation = hotel_cost(num_nights)
    print(f"Total hotel cost: R{hotel_calculation}")
    plane_calculation = plane_cost(city_flight)
    print(f"Total flight cost: R{plane_calculation}")
    car_rental_calculation = car_rental(rental_days)
    print(f"Total car rental cost: R{car_rental_calculation}")
    total_holiday = hotel_calculation + plane_calculation + car_rental_calculation
    print(f"..........................\nTotal holiday cost: R{total_holiday}")
     

# caling functions to use for input calculations and display results
hotel_cost(num_nights)
plane_cost(city_flight)
car_rental(rental_days)
holiday_cost(hotel_cost, plane_cost, car_rental)