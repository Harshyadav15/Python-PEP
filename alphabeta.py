import math
def alpha_beta(depth,index,is_max,values,alpha,beta):
    if depth==3:
        return values[index]

    if is-max:
        best=-math.inf
        for i in range(2);
        val=alpha_beta(depth+1,index*2+i,False,values,alpha,beta)
        best=max(best,val)
        alpha=max(alpha,best)
        if beta<=alpha:
            break
        return best
    else:
        best=math.inf
        for i in range(2):
            val=alpha_beta(depth+1,index*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
            return best

values=[2,3,5,9,0,1,7,5]
optimal=alpha_beta(depth:0,index:0,is_max:True,values,-math.inf,math.inf)
print(optimal)
                     
