
dc_1={'key1':8,'key2':5,'key3':6}
dc_2={'key4':11,'key5':22,'key6':33}
dc_3={'key7':777,'key8':444,'key9':999}
res={}
for i in (dc_1, dc_2, dc_3):
    res.update(i)
print(res)