import os
os.system("clear")

irrf = 0

def calculo_inss(salario):
    if salario <= 1320:
        desconto = salario * 0.075  
    elif salario <= 2571.29:
        desconto = salario * 0.09
    elif salario <= 3856.94:
        desconto = salario * 0.12
    elif salario <= 7507.49:
        desconto = salario * 0.14
    else:
        desconto = salario * 0.14  
    
    return min(desconto, 1051.05)

def calculo_irrf(salario, dependente):
    deducao = dependente * 189.59  
    calculo = salario - deducao

    if calculo <= 2112:
        irrf = 0
    elif calculo <= 2826.65:
        irrf = calculo * 0.075
    elif calculo <= 3544.00:
        irrf = calculo * 0.15
    elif calculo <= 4256.00:
        irrf = calculo * 0.225
    else:
        irrf = calculo * 0.275 

    return irrf

Matricula = float(input("Digite sua matrícula: "))
Senha = float(input("Digite sua senha: "))
salario_base = float(input("Digite o seu salário base(R$): "))
vale_transporte = input("Deseja receber o vale transporte (S/N): ").strip().lower()
vale_refeicao = float(input("Qual o valor do vale refeição fornecido pela empresa? : "))
dependente = 1  

print("\n---FOLHA DE PAGAMENTOS---")
desconto_inss = calculo_inss(salario_base)
desconto_irrf = calculo_irrf(salario_base, dependente)
desconto_vale_transporte = salario_base * 0.06 if vale_transporte == 's' else 0  
desconto_plano_saude = dependente * 150.00  
desconto_vale_refeicao = vale_refeicao * 0.20 

total_desconto = desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_plano_saude + desconto_vale_refeicao


salario_liquido = salario_base - total_desconto

print("\n---RESUMO---")
print(f"\nSua Matrícula: {Matricula}")
print(f"Sua Senha: {Senha}")
print(f"Desconto do INSS: R${desconto_inss:.2f}")
print(f"Desconto IRRF: R${desconto_irrf:.2f}")
print(f"Desconto vale transporte: R${desconto_vale_transporte:.2f}")
print(f"Desconto plano de saúde: R${desconto_plano_saude:.2f}")
print(f"Desconto vale refeição: R${desconto_vale_refeicao:.2f}")
print(f"\nSalário Líquido: R${salario_liquido:.2f}")
