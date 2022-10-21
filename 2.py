#Напишите программу, которая помогает определить какие вещи могут поместиться в рюкзак. Вводится существующий объем рюкзака.....
volume=int(input())
objects=input()
objects_list=[int(x) for x in objects.split()]
objects_list.sort()
total_sum=0
objects_sum=[]
for i in range(len(objects_list)):
    if total_sum+objects_list[i]<volume:
        total_sum+=objects_list[i]
        objects_sum.append(objects_list[i])
print(objects_sum)