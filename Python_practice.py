
#What's ur score
score=int(input("What's ur score? "))
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

#Membership operators

counties=["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("True")
else:
    print("False")

#F-Strings

my_votes=int(input("Your votes?"))
tot_votes=int(input("Total votes?"))
print(f"I received {my_votes/tot_votes * 100} % of votes")

#F-Strings with dictionaries

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county,votes in counties_dict.items():
    print(f"{county} county has {str(votes)} registered voters")

#Multiple F-strings

my_votes=int(input("Your votes?"))
tot_votes=int(input("Total votes?"))
candidate_votes = (
    f"You received {my_votes} no of votes. "
    f"Total votes are {tot_votes}. "
    f"You received {my_votes/tot_votes*100:.2f} % of votes"
)
print(candidate_votes)