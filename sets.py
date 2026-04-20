days_of_the_week={"Mon","Tue","Wed","Thur","Fri","Sat","Sun","Sun","Mon"}
print(days_of_the_week)

# remove friday an sunday
days_of_the_week.remove("Fri")
days_of_the_week.remove("Sun")
print(days_of_the_week)

# add them back
days_of_the_week.add("Fri")
days_of_the_week.add("Sun")
print(days_of_the_week)
