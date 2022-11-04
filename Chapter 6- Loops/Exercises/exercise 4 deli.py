sandwich_orders = ['chicken', 'beef', 'egg', 'nutella']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()                                                      #creating a new variable(current sandwich) for storing orders in that variable
    print("I'm working on your " + current_sandwich + " sandwich.")                               #and using the pop funtion to remove it from the sanwich orders list then
    finished_sandwiches.append(current_sandwich)                                                  #creating a new variable(fin..) and using the append function

for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")