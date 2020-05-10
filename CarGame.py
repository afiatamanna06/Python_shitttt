started = False
while 1:
    command = input("> ").lower()
    if command == 'help':
        print("start - to start the car\nstop - to stop the car\nexit - to exit")
    elif command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
