operator = str(input("\nSelecione a operecao desejada entre + - * /: "))
num1 = float(input("\nDigite o primeiro numero da operacao: "))
num2 = float(input("\nDigite o segundo numero da operacao: "))
digits = int(input("\nQuantas casas decimais deseja? "))

if operator == '+':
    print(f"\nO resultado é: {round(num1+num2, digits)}")
elif operator == '-':
    print(f"\nO resultado é: {round(num1-num2, digits)}")
elif operator == '*':
    print(f"\nO resultado é: {round(num1*num2, digits)}")
elif operator =='/':
    print(f"\nO resultado é: {round(num1/num2, digits)}")
else:
    print("\nO sinal inserido não é valido.")