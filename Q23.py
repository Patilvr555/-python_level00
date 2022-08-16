empcode=int(input("enter employee code :"))
empname=str(input("employee name :"))
bsal=float(input("enter basic salary :"))

hra=bsal/100*40

print("HRA=",hra)

da=bsal/100*10
print("DA=",da)
cca=bsal/100*5
print("CCA=",cca)

gs=bsal+hra+da+cca
print("GS=",gs)

pf=gs/100*10
print("PF",pf)

it=gs/100*10
print("IT=",it)

ns=gs-(pf+it)
print("NS=",ns)