largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))
rendimento_tinta = float(input("Digite o rendimento da tinta (metros quadrados por litro): "))

area_parede = largura * altura
quantidade_tinta = area_parede / rendimento_tinta

print(f"A área total da parede é {area_parede:.2f} m².")
print(f"Você precisará de {quantidade_tinta:.2f} litros de tinta para pintar toda a parede.")
