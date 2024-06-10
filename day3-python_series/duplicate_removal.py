def d_prod(res_l):
    prod=1
    for x in res_l:
        prod*=x
    return prod

d_list=[1,3,2,3,5]
print("my original list:"+str(d_list))
res=[]
[res.append(i) for i in d_list if i not in res]
print("unquiue list::",res)
print(d_prod(res))
