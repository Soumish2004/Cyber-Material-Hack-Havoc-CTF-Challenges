string1 = 'wertyuiopasdfghjlcbnm1234567890_' # input
string2 = 'jslcbnmr12u3p4d5ye67i890_gwtoafh' # output
challenge = 'owoosHiai1w1aia_awJ3ally!0awwa_o'
ans = []
anslist = []
for i in range(0, 32):
    ans.append('')
for stri in string2:
    anslist.append(string1.find(stri))
print(anslist)
print(len(anslist))
for i in range(0, len(challenge)):
    strj = challenge[i]
    pos = anslist[i]
    ans[pos] = strj
print('CM{'+''.join(ans)+'}')