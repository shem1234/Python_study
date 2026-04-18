days_of_the_week = ("Sun","Mon","Tue","Wed","Thur","Fri","Sat")
print(type(days_of_the_week))
print(days_of_the_week[2:4])

# Display Saturday
print(days_of_the_week[4:5])

# Display Thursday to Satuday
print(days_of_the_week[4:7])

# Sun to Sunday
days_of_the_week=list(days_of_the_week)
days_of_the_week[0]="Sunday"
days_of_the_week=tuple(days_of_the_week)
print(days_of_the_week)

# add jan to the tuple
days_of_the_week=list(days_of_the_week)
days_of_the_week=days_of_the_week.append(Jan)
print(days_of_the_week)
