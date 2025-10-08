# dictionary={"a":1,"b":2,"c":4}
# print(dictionary)
# print(dictionary["a"])
# dictionary["c"]=10
# print(dictionary)
# dictionary["d"]=11
# # print(dictionary)
# # dictionary={}
# print(dictionary)
# for key in dictionary:
#     print(key)
#     print(dictionary[key])

# GRADING SYSTEM
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades={}
# for key in student_scores:
#     if 91<=student_scores[key]<=100:
#         student_grades[key]="Outstanding"
#     elif 81<=student_scores[key]<=90:
#         student_grades[key]="Expectations"
#     elif 91<=student_scores[key]<=100:
#         student_grades[key]="Outstanding"
#     elif 71<=student_scores[key]<=80:
#         student_grades[key]="Acceptable"
#     elif student_scores[key]<=70:
#         student_grades[key]="Fail"
# print(student_grades)

#BIDDING PROGRAM
def bidding(bidding_dictionary):
    # highest_bid=0
    # winner=""
    # for i in bidding_dictionary:
    #     if bidding_dictionary[i]>highest_bid:
    #         highest_bid=bidding_dictionary[i]
    #         winner=i
    # print(bidding_dictionary)
    # print(f"the winner is {winner} with amount {highest_bid}")
    # it is an simple method for getting maximum value from dictionary using max() function
    print(max(bidding_dictionary,key=bidding_dictionary.get))


list_of_peoples={}
should_continue=True
while should_continue:
    name=input("Enter your name:\n").lower()
    price=int(input("Enter your price:\n"))
    list_of_peoples[name]=price
    Next_entry=input("Type Yes for next entry or NO:\n").lower()
    if Next_entry=="no":
        should_continue=False
        bidding(list_of_peoples)
    elif Next_entry=="yes":
        print("\n"*15)
        should_continue=True
    else:
        print("ERROR")
        exit()
    list_of_peoples[name]=price
