i = ""
started = False
while True:
    i = input(" >")
    if i == 'start':
        if started:
            print("Car is Already started")
        else:
            started = True
            print("Car started")

    elif i == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car stopped")

    elif i == 'help':
        print("""
start - To start the car
stop  - To stop the car
quit  - To exit
             """)
    elif i == 'quit':
        break
    else:
        print("cant find,Please reEnter")
