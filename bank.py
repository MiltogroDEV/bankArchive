val = int(input("Valor: R$"))
tax = int(input("Taxa: R$"))

valint = val + tax + (val * 0.0524)

xVezes = [0.0764, 0.0923, 0.1086, 0.1231, 0.1365, 0.1472, 0.1623, 0.1769, 0.1865, 0.2012, 0.2161]

def Calc(val, x):
    val = val + (val * x)
    return val

def Parc(val, numPosI):
    val = val / numPosI
    return val

def Print():
    print(f"\n     R${val:.2f} fica R${valint:.2f}\n")

    for i in range(0,11):
        print(f"     {i + 2}x fica R${Calc(valint, xVezes[i]):.2f} ({i + 2}x de R${Parc(Calc(valint, xVezes[i]), i + 2):.2f})")
    
    print("\n")

Print()