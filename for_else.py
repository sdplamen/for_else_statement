print('\nFisrt For Example\n')
for num in range(5):
    print(f'First for example {num}')

#######################
# In this example we break out when num = 3
print('\nSecond For Example\n')
for num in range(5):
    if num == 3:
        break
    print(f'Second for example {num}')

#######################
# In this example we continue when num = 3 with next iteration
print('\nThird For Example\n')
for num in range(5):
    if num==3:
        continue
    print(f'Third For Example {num}')
#######################
# ELSE always runs in this case
print('\nFourth For Example \n')
for num in range(5):
    print(f'Fourth for example {num}')
else:
    print('ELSE from Fouth for example')
#######################
print('\nFifth For Example\n')
# When we break out of the loop we do not enter ELSE statement
for num in range(5):
    if num==3:
        break
    print(f'Fifth for example {num}')
else:
    print('ELSE from Fifth for example')
#######################
# Even if we use continue we still enter the ELSE statement
print('\nFifth For Example\n')
for num in range(5):
    if num==3:
        continue
    print(f'Sixth for example {num}')
else:
    print('ELSE from Sixth for example')

#########################################################
print('\nUSECASE\n')
import random

flag = False
rndlist = [random.randint(1,10) for _ in range(5)]
print(rndlist)
for num in rndlist:
    if num == 5:
        flag = True
        break

print(flag)
        

for num in rndlist:
    if num == 5:
        flag1 = True
        break
else:
    flag1 = False

print(flag1)


if (my_num:=random.randint(1,3)) == 2:

    print('I am lucky!')
print(my_num)
