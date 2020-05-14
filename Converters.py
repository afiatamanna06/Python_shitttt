def lbs_to_kg(weight):
    return weight*0.45

def find_max(numbers):
    maximum = numbers[0]
    for item in numbers:
        if maximum<item:
            maximum = item

    return maximum
