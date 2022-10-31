sandwich_orders = ['chicken', 'beef', 'pastrami', 'pastrami', 'egg', 'nutella','pastrami']
finished_sandwiches = []
                                                                                                                 
print("I'm sorry, we're all out of pastrami today.")                                    #repeating the same process while only removing pastrami sandwich from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")