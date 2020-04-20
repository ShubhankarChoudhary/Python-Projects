ls1 = ['Shubhankar','Goutham','Jibin','Abhijeet','Ajmal','Aditya','Nandu','Shubhankar']
ls2 = ['Deoghar','Pune','Kottayam','Muzzafarpur','Trishur','Dhanbad','Cochin','Deoghar']

ls3 = list(zip(ls1,ls2))
for i in ls3:
    print(i)
print('*****************')
ls3 = set(zip(ls1,ls2))
for j in ls3:
    print(j)
print('*****************')
ls3 = dict(zip(ls1,ls2))
print(ls3)
print('*****************')
ls3=zip(ls1,ls2)
for (m,n) in ls3:
    print(m,n)
