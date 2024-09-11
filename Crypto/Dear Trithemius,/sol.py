encrypt= 'LPXH_Z_AZRDSQZWJI'
decrypt=''
for i in range(0,len(encrypt)):
    if encrypt[i] == '_':
        decrypt+='_'
    else:
        temp=ord(encrypt[i])-i
        if temp<65:
            temp+=26
        decrypt+=chr(temp)
print(decrypt)