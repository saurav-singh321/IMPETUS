list=[]
while (True):
    n_str = int(input("Input an integer (0 terminates): \n"))
    if n_str!=0:
        odd_sum,even_sum,odd_count,even_count,positive_int_count = 0,0,0,0,0
        list.append(n_str)
        for i in list:
            if i%2==1 and i>0:
                odd_sum += i
                odd_count+=1
                positive_int_count+=1

            elif i%2==0 and i>0:
                even_sum += i
                even_count+=1
                positive_int_count+=1
        continue

    else:
        break
print(list)
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
