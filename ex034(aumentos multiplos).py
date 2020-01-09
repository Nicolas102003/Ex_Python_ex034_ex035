sal = float(input('Quando vc ganhar ??'))
if sal <= 1250:
    n15 = ((15 * sal) / 100) + sal
    print('seu novo salário é R${:.3f}'.format(n15))

else:
    n10 = ((10 * sal) / 100) + sal
    print('Seu salario novo de {:.2f}'.format(n10))
