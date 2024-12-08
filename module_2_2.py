#Домашнее задание по теме "Условные операторы if, else, elif"

first=int(input())
second=int(input())
third=int(input())
if first==second and first==third:
    print(3)
if (first==second and first!=third and second!=third
or first==third and second!=third and second!=first
or second==third and second!=first and first!=third):
    print(2)
else:
    print(0)
