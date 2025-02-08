# A program to determine the fastest route based on distance and speed
# Date: Jan 30, 2025
# CSC121 m1Lab2 – Review
# Michael Odoom

#Pseudocode
#1. Initialize fastest_time to a large number (e.g., infinity) and fastest_route to 0.
#2. Initialize route_counter to 1.
#3. While the user wants to enter more routes:
#   a. Prompt for distance in miles.
#   b. Validate distance (must be greater than 0).
#   c. Prompt for speed in miles per hour.
#   d. Validate speed (must be greater than 0).
#   e. Calculate time in minutes using the formula: time = (distance / speed) * 60.
#   f. Display the time for the current route.
#   g. If the current route's time is less than fastest_time:
#      i. Update fastest_time and fastest_route.
#   h. Ask if the user wants to enter more routes.
#4. Display the fastest route and its time.

# Initialize variables
fastest_time = float('inf')  # Set to a large number initially
fastest_route = 0
route_counter = 1

# Loop to input route details
while True:
    # Prompt for distance
    distance = float(input(f"Enter route {route_counter} distance (miles): "))
    while distance <= 0:  # Validate distance
        print("Distance must be greater than 0. Please try again.")
        distance = float(input(f"Enter route {route_counter} distance (miles): "))

    # Prompt for speed
    speed = float(input(f"Enter route {route_counter} speed (miles/hour): "))
    while speed <= 0:  # Validate speed
        print("Speed must be greater than 0. Please try again.")
        speed = float(input(f"Enter route {route_counter} speed (miles/hour): "))

    # Calculate time in minutes
    time = (distance / speed) * 60
    print(f"Route {route_counter} will take {time:.2f} minutes.")

    # Check if this route is the fastest
    if time < fastest_time:
        fastest_time = time
        fastest_route = route_counter

    # Ask if the user wants to enter more routes
    more_routes = input("More routes (y/n)?: ").strip().lower()
    if more_routes != 'y':
        break  # Exit the loop if the user does not want to enter more routes

    route_counter += 1  # Increment route counter

# Display the fastest route
print(f"Route {fastest_route} is fastest; {fastest_time:.2f} minutes")