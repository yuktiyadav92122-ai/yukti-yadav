INTRO="Hello!! Welcome to my project .\nThis mini project aims to help them build a Python-based CLI (Command Line Interface) tool where they can log their meals and keep track of total calories consumed, compare against a personal daily limit, and save session logs for future tracking."
print(INTRO)

meal=input("Meal name :- ").split()
calories=list(map(float,input("Calories Amount :-").split()))
print(meal)
print(calories)

total_calories=sum(calories)

avg_calories=total_calories/len(calories)

print("Total_calories_intake",total_calories)
print("Avg_calories",avg_calories)

daily_limit=float(input("your daily calories limit"))
print(daily_limit)

if total_calories>= daily_limit:
    print("WARNING!! you exceed your daily limit")
else:
    print("you  are in limit")


print(f"{'Meal':<15} {'Calories'}")

print("-" * 20)

for i in range(len(meal)):
    print(f"{meal[i]:<15} {calories[i]}")

print(f"{'TOTAL':<15} {total_calories}")