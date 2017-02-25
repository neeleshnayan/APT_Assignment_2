list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 3, 5, 7, 9]
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 3, 5, 7, 9}


def q1():  # Answer to the first question
    print('Union and intersection of two lists without using list operators')

    # Code for union
    union = []
    for each in list_1:
        union.append(each)
    for each in list_2:
        if each not in list_1:
            union.append(each)

    print('Union of', list_1, 'and', list_2, 'is:', union)

    # Code for intersection
    intersection = []
    for each in list_1:
        if each in list_2:
            intersection.append(each)

    print('Intersection of', list_1, 'and', list_2, 'is:', intersection)

    # End of the first answer


def q2():  # Answer to the second question
    print('Difference and symmetric difference of two lists without using list operators')

    # code for difference
    difference = []
    for each in set_1:
        if each not in set_2:
            difference.append(each)

    print('Difference of', set_1, 'and', set_2, 'is:', difference)

    # code for symmetric difference
    sym_difference = []
    for each in set_1:
        if each not in set_2:
            sym_difference.append(each)

    for each in set_2:
        if each not in set_1:
            sym_difference.append(each)

    print('Symmetric difference of', set_1, 'and', set_2, 'is:', sym_difference)

    # End of the second question


def q3():  # Answer to the third question
    print('Theory question. Google it. Don\'t read it from the slides.')


def q4():  # Answer to the fourth question
    print('To find if a given list is palindrome or not')
    palin_check = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    if palin_check == palin_check[::-1]:
        print(palin_check, 'is Palindrome')
    else:
        print('Not palindrome')


def q5():  # Answer to the fifth question
    l=[1,3,2,4,2]
    for i in l:
	for j in l[i:len(l)]:
		if l[i]>l[j]:
			l[i],l[j]=l[j],l[i]
    print(l)


def main():  # main function
    print('1: Q1 \n2: Q2 \n3: Q3 \n4: Q4 \n5: Q5')
    choice = int(input('Enter the desired choice: '))
    if choice == 1:
        q1()  # call of the function q1
    elif choice == 2:
        q2()  # call of the function q2
    elif choice == 3:
        q3()  # call of the function q3
    elif choice == 4:
        q4()  # call of the function q3
    elif choice == 5:
        q5()  # call of the function q3


main()  # call of the main function
