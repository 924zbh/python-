dct = {"cn" : "中国","uk" : "英国","us" : "美国","de" : "德国"}
print(dct["cn"])    #打印索引"cn"对应的值
print(dct.get("cn","该键不存在"))  #打印"cn"对应的值，不存在会抛出异常

dct["fr"] = "法国"   #增加索引"fr"对应"法国
del dct["uk"]  #删除"uk"对应的项
dct.pop("us")   #弹出"us"对应的项
print(dct)

print(dct.keys())      #打印所有键
print(dct.values())     #打印所有值
print(dct.items())      #打印所有项
print("ca" in dct.keys())   #是否包含"ca"

dct2 = {"au":"澳大利亚","cz":"捷克共和国"}
dct.update(dct2)   #用dct2批量更新dct
print(dct)
print(len(dct))   #打印长度
