def make_change(total,biggest):
    if total<0:
        return False
    if total==0:
        return []
    elif biggest==0:
        return False
    else:
        wit=make_change(total-biggest,biggest)
        op=make_change(total,biggest-1)
        if wit==False and op==False:
            return False
        if wit==False:
            return op
        elif op==False:
            return [biggest]+wit
        else:
            return [[biggest]+wit+op]
        


def find(n,sym):
    if sym[0]==n:
        return ['car']
    elif sym==None:
        return None
    else:
        if isinstance(sym[0],list):
            li=find(n,sym[0])+['cdr']
        
        