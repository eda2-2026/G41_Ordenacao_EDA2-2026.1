from __future__ import annotations
from heapq import heapify
from typing import Any

def _particionar(lista: list, baixo: int, alto: int, chave, reverso: bool) -> int:
   
    mid = (baixo + alto) // 2
    a = chave(lista[baixo])
    b = chave(lista[mid])
    c = chave(lista[alto])

    if (a < b < c) or (c < b < a):
        pivot_idx = mid
    elif (b < a < c) or (c < a < b):
        pivot_idx = baixo
    else:
        pivot_idx = alto

    lista[pivot_idx], lista[alto] = lista[alto], lista[pivot_idx]
    pivo = chave(lista[alto])
    i = baixo - 1

    for j in range(baixo, alto):
        valor_j = chave(lista[j])
        condicao = (valor_j > pivo) if reverso else (valor_j < pivo)
        if condicao:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1


def _quicksort_recursivo(lista: list, baixo: int, alto: int, chave, reverso: bool) -> None:
    if baixo < alto:
        idx_pivo = _particionar(lista, baixo, alto, chave, reverso)
        _quicksort_recursivo(lista, baixo, idx_pivo - 1, chave, reverso)
        _quicksort_recursivo(lista, idx_pivo + 1, alto, chave, reverso)


def quicksort(lista: list, chave=None, reverso: bool = False) -> list:
    resultado = list(lista)
    if chave is None:
        chave = lambda x: x
    if resultado:
        _quicksort_recursivo(resultado, 0, len(resultado) - 1, chave, reverso)
    return resultado


def _merge(esq: list, dir: list, chave, reverso: bool) -> list:
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        val_e = chave(esq[i])
        val_d = chave(dir[j])

        if reverso:
            preferir_esq = val_e >= val_d
        else:
            preferir_esq = val_e <= val_d

        if preferir_esq:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


def heapsort(lista: list, chave=None, reverso: bool = False) -> list:
    if chave is None:
        chave = lambda x: x
    def heapify(arr: list, n: int, i: int) -> None:
        extremidade = i
        esq = 2 * i + 1
        dir = 2 * i + 2

        if esq < n:
            comp_esq = (chave(arr[esq]) < chave(arr[extremidade])) if reverso else (chave(arr[esq]) > chave(arr[extremidade]))
            if comp_esq:
                extremidade = esq

        if dir < n:
            comp_dir = (chave(arr[dir]) < chave(arr[extremidade])) if reverso else (chave(arr[dir]) > chave(arr[extremidade]))
            if comp_dir:
                extremidade = dir

        if extremidade != i:
            arr[i], arr[extremidade] = arr[extremidade], arr[i]
            heapify(arr, n, extremidade)

    copia = list(lista)
    n = len(copia)

    for i in range(n // 2 - 1, -1, -1):
        heapify(copia, n, i)

    for i in range(n - 1, 0, -1):
        copia[i], copia[0] = copia[0], copia[i]
        heapify(copia, i, 0)

    return copia


def registrarAvaliacao(livros: dict, livro_id: str, nota: float) -> dict | None:


   if not (0.0 <= nota <= 5.0):
       raise ValueError(f"Nota inválida: {nota}. Deve estar entre 0.0 e 5.0.")


   if livro_id not in livros:
       return None


   livro = livros[livro_id]


   _garantir_campos_metricas(livro)


   total_atual = livro["total_avaliacoes"]
   media_atual = livro["nota_media"]


   novo_total = total_atual + 1
   nova_media = round((media_atual * total_atual + nota) / novo_total, 2)


   livro["total_avaliacoes"] = novo_total
   livro["nota_media"] = nova_media


   return livro


def _garantir_campos_metricas(livro: dict) -> None:
   livro.setdefault("nota_media", 0.0)
   livro.setdefault("total_avaliacoes", 0)
   livro.setdefault("contagem_emprestimos", 0)

def incrementar_emprestimo(livros: dict, livro_id: str) -> dict | None:


   if livro_id not in livros:
       return None


   livro = livros[livro_id]
   _garantir_campos_metricas(livro)
   livro["contagem_emprestimos"] += 1
   return livro

def ordenar_por_titulo(livros: dict | list, reverso: bool = False) -> list:
   lista = list(livros.values()) if isinstance(livros, dict) else list(livros)
   return quicksort(
       lista,
       chave=lambda l: l.get("titulo", "").lower(),
       reverso=reverso
   )


def ranking_por_avaliacao(livros: dict | list) -> list:
   lista = list(livros.values()) if isinstance(livros, dict) else list(livros)


   for livro in lista:
       _garantir_campos_metricas(livro)


   return heapsort(
       lista,
       chave=lambda l: l["nota_media"],
       reverso=True   # maior nota primeiro
   )


def ranking_por_popularidade(livros: dict | list, reverso: bool = True) -> list:
   lista = list(livros.values()) if isinstance(livros, dict) else list(livros)


   for livro in lista:
       _garantir_campos_metricas(livro)


   def calcular_score(livro: dict) -> float:
       emprestimos = float(livro.get("contagem_emprestimos", 0) or 0)
       nota = float(livro.get("nota_media", 0.0) or 0.0)
       return (emprestimos * 0.7) + (nota * 0.3)


   return quicksort(
       lista,
       chave=calcular_score,
       reverso=reverso
   )

def radix_sort_por_ano(lista: list, reverso: bool = False) -> list:

    def get_ano(livro: dict) -> int:
        val = livro.get("ano", 0)
        if val is None:
            return 0
        try:
            return max(0, int(val))
        except (ValueError, TypeError):
            return 0

    def maior_exp(arr: list) -> int:
        maximo = 0
        for livro in arr:
            ano = get_ano(livro)
            if ano > maximo:
                maximo = ano
        exp = 1
        while maximo // exp >= 10:
            exp *= 10
        return exp

    def msd_recursivo(arr: list, exp: int) -> list:
        if len(arr) <= 1 or exp == 0:
            return arr

        baldes = [[] for _ in range(10)]

        for livro in arr:
            digito = (get_ano(livro) // exp) % 10
            baldes[digito].append(livro)

        resultado = []
        for balde in baldes:
            sub = msd_recursivo(balde, exp // 10)
            for item in sub:
                resultado.append(item)

        return resultado

    if not lista:
        return []

    copia = list(lista)

    exp_inicial = maior_exp(copia)

    ordenado = msd_recursivo(copia, exp_inicial)

    if reverso:
        ordenado.reverse()

    return ordenado



         
                
