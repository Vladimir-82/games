
dc_1={'key1':8,'key2':5,'key3':6}
dc_2={'key4':11,'key5':22,'key6':33}
dc_3={'key7':777,'key8':444,'key9':999}

list_summary=[dc_1,dc_2,dc_3]
n=len(list_summary)

while n!=0:
    list_summary[n-1].update(list_summary[n])
    n-=1

print(list_summary[0])

#dc_2.update(dc_3)
#dc_1.update(dc_2)

#print(dc_1)