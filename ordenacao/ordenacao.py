from __future__ import annotations
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


def mergesort(lista: list, chave=None, reverso: bool = False) -> list:

    if chave is None:
        chave = lambda x: x

    n = len(lista)
    if n <= 1:
        return list(lista)

    res = list(lista)

    def mesclar(arr: list, esq: int, meio: int, dir: int) -> None:
        L = arr[esq:meio]
        R = arr[meio:dir]

        i = j = 0
        k = esq

        while i < len(L) and j < len(R):
            comp = (chave(L[i]) > chave(R[j])) if reverso else (chave(L[i]) <= chave(R[j]))
            if comp:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    tamanho = 1
    while tamanho < n:
        for esq in range(0, n, 2 * tamanho):
            meio = min(esq + tamanho, n)
            dir = min(esq + 2 * tamanho, n)
            if meio < dir:
                mesclar(res, esq, meio, dir)
        tamanho *= 2

    return res


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
