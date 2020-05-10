while 1:
    command = input("> ").lower()
    if command == 'help':
        print("start - to start the car\nstop - to stop the car\nexit - to exit")
    elif command == 'start':
        print("Car started...Ready to go!")
    elif command == 'stop':
        print("Car stopped.")
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
