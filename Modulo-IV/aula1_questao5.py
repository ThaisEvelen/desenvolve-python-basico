n= int(input("Digite a quantidade de respondentes: "))
while n >1:
    idade=int(input("Digite a idade do respondente"))
    idade=idade+0
    media =(idade)/n 
    n = n-1
print(media)