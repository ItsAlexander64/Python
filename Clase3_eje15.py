n=10
x=4
def vasos(n,x):
  total=0
  while n>=x:
      reciclados=n//x
      sobran=n%x
      total+=reciclados
      n=reciclados+sobran
      print("N: ",n," Reciclados: ",reciclados," sobran ",sobran," total ",total)
  return total
n=31
x=2
print(vasos(n,x))  