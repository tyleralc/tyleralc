def all_postive(lst):
    pos_num=[]

    for i in lst:
        if type(i)==int or type(i)==float:
            pi=abs(i)
            pos_num.append(pi)
        
        if type(i)==str:
            try:
                ni=float(i)
                pni=abs(ni)
                pos_num.append(pni)
            except:
                pass
    return pos_num 

print(all_postive([3, 6, 8, -7, -.23, '5', 'word', '-.07']))
print(all_postive(['this', 'should', 'be', 'an', 'empty', 'list']))
print(all_postive([23, 1234, -234, -.234, .67, 'five', '-7']))