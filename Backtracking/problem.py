#iven a number n- generate all strs of len n using only 'A' & 'B'
def Backtrack(s,n):
    if len(s)==n: #0==2
        print(s)
        return
    Backtrack(s+'A',n) #(A,2)=1==2 ,(AA,2) if 2==2,AA
    Backtrack(s+'B',n) #(B,2)=1==2, ()

Backtrack("",2)
