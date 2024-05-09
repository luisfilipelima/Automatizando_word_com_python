from docx import Document
from datetime import datetime

documento = Document("Contrato.docx")

nome = input("Digite o nome:")
item1 = input("Digite o item:")
item2 = input("Digite o item:")
item3 = input("Digite o item:")

referencias = {
     "XXXX": nome ,
     "YYYY": item1,
     "ZZZZ": item2,
     "WWWW": item3,
     "DD": str(datetime.now().day),
     "MM": str(datetime.now().month),
     "AAAA": str(datetime.now().year),
}

for paragrafo in documento.paragraphs: # pecorre todos os paragrafos do documento (LER TODOS OS PARAGRAFOS)
   for codigo in referencias: # PECORRE MEU DICIONARIO 
     valor = referencias[codigo] # pego o valor de cada chave do meu dicionário 
     paragrafo.text = paragrafo.text.replace(codigo,valor) # Realizo a troca dos codigos pelo valor contido no dicionário 
 
documento.save(f"Contrato - {nome}.doc")
 