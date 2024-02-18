def main():
    my_list = []
    while True:
        operation = input(''''
Select operation:
[1] Add number to the list 
[2] Remove number from the list 
[3] Display list
[4] Multiply list
[5] Subtract first index from list 
[6] Change first index with the last one 
[7] 
[8]
[9] Exit program''')
        if operation == '1':
            print("Type the number you would like to add to the list")
            number = int(input())
            my_list.append(number)

        elif operation == '2':
            print("Type position of the element number which you want to remove from the list")
            number = int(input())
            my_list.pop(number)

        elif operation == '3':
            print(my_list)

        elif operation == '4':
            print("Type position of the element number  from the list to multiply")
        elif operation == '9':
            break
        else:
            print("Invalid choice. Please try again,darling.")


main()
