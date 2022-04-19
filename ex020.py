command = ""
started = False
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command.lower() == "quit":
        print("Bye!")
    else:
        print("Sorry, I don't understand that...")

