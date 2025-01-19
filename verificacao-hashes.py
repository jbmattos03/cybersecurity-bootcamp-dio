def verificar_hashes(lista_hashes):
  
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        # Remover espaços
        hash_calculado = "".join(filter(lambda c: c != " ", hash_calculado))
        hash_esperado = "".join(filter(lambda c: c != " ", hash_esperado))
        
        # Realizar verificação
        if (hash_calculado == hash_esperado):
            print("Correto")
        else:
            print("Inválido")
        
            
        
hashes_usuario = input()

lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)
