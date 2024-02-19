def main():
    my_list = [2, 4, 5, 18, 55]
    while True:
        operation = input('''
Select operation from the menu:
[1] Add number to the list 
[2] Remove number from the list 
[3] Display list
[4] Multiply some index from the list 
[5] Subtract index from list 
[6] Change first index with the last one 
[7] Add string in the end of the list and then remove index 1 from the list
[8] Check if today is your lucky list day :) Xoxo
[9] Exit program''')

        if operation == '1':
            print("Type the number you would like to add to the list.")
            number = int(input())
            my_list.append(number)

        elif operation == '2':
            print("Type position of the element number which you want to remove from the list.")
            number = int(input())
            my_list.pop(number)

        elif operation == '3':
            print(my_list)

        elif operation == '4':
            print("Type position of the element number from the list to multiply.")
            number = int(input())
            print("Type the multiply number.")
            multiply = int(input())
            my_list[number] *= multiply
            print(f"Complete task. Well done! Look your multiply list how is looking now{my_list}")

        elif operation == '5':
            print("Enter the index which you prefer to subract from the list")
            number = int(input())
            print("Type the number with which you want to subtract the list index")
            subtract_number = int(input())
            my_list[number] -= subtract_number
            print(f"Complete task. Well done! Look your subtract list is how is looking now{my_list}")

        elif operation == '6':
            my_list[0] = my_list[4]
            print(my_list)
        elif operation == '7':
            string = input()
            my_list.append(string)
            my_list.remove(my_list[1])
            print(my_list)

        elif operation == '8':
            print("Insert your favorite list number and check if today is your lucky list day")
            numbers = int(input())
            if numbers % 2 == 0:
                print(f'Its your lucky day with number {numbers} ')
            else:
                print("Sorry, today is not your lucky day. Try next day!")

        elif operation == '9':
            break
        else:
            print("Invalid choice. Please try again,darling.")


main()
