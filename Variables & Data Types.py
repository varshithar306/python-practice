name = "varshitha"
college_name = "snpsu"
yop =2028
cgpa=8.5
print(f"student name:{name},college name:{college_name},year of passing:{yop},cgpa:{cgpa}")

#program 2
a=10
b=5
c=a+b
sub=a-b
mul=a*b
print(f"addition:{c},subtraction:{sub},multiplication:{mul}")
if(a>b):
    print("a is larger")
else:
    print("b is larger")


#program 3 day 1
arr=[78,85,92,67,88]
marks=sum(arr)
avg=marks/len(arr)
print("total:",marks)
print("average:",avg)
print("percentage:",(marks/(len(arr)*100))*100)
if(avg>=40):
    print("pass")
else:
    print("fail")