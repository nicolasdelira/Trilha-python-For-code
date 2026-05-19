### Sistema de auxílio para viagens

Orçamentoreais  = float(input("Qual o seu orçamento em reais ?: "))
destino = input("onde você vai ?: ")
custopassagem = float(input("qual o valor da passagem?: "))
custohospedagem = float(input("qual o custo da hospedagem em euros ?: "))
dias = int(input("quantos dias ?: "))
try: 
  custoreais = custohospedagem * 6.10 
  custototal = (custoreais * dias) + custopassagem
  print("O custo da hospedagem em reais é:", custoreais)  
  if Orçamentoreais == custototal:
    print("O orçamento é possível")
    print("VIÁVEL")

  elif Orçamentoreais < custototal:
    print("O custo total é: ", custototal)
    diferença = abs(custototal - Orçamentoreais)
    print("O orçamento é impossível, falta: ", diferença, "reais para sua viagem ser possível")
    print("STATUS FINAL: INVIÁVEL")

  elif Orçamentoreais > custototal:
    print("O custo total é: ",custototal)
    diferença = abs(custototal - Orçamentoreais) 
    print("O orçamento é possível, sobrará: ",diferença, "reais para você usar ")
    print("STATUS FINAL: VIÁVEL")
except ValueError:
    print("Digite número quando é pedido números, exceto quando pede o nome do país ") 
      