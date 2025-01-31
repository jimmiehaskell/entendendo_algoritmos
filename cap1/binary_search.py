class BinarySearch():
    def pesquisa_binaria(self, lista, item) -> int or None:
        _baixo = 0
        _alto = len(lista) - 1

        while _baixo <= _alto:
            _meio = (_baixo + _alto) // 2
            _chute = lista[_meio]

            if _chute == item:
                return _meio
            elif _chute > item:
                _alto = _meio - 1
            else:
                _baixo = _meio + 1

        return None

    def pesquisa_binaria_recursiva(self, lista, baixo, alto, item) -> int or None:
        if alto > baixo:
            _meio = (alto + baixo) // 2
            _chute = lista[_meio]

            if _chute == item:
                return _meio
            elif _chute > item:
                return self.pesquisa_binaria_recursiva(lista, baixo, _meio - 1, item)
            else:
                return self.pesquisa_binaria_recursiva(lista, _meio + 1, alto, item)
        else:
            return None

if __name__ == '__main__':
    bs = BinarySearch()
    lista = [1, 2, 3, 4, 5, 13, 50, 100, 300, 237]
    print(bs.pesquisa_binaria(lista, 3))
    print(bs.pesquisa_binaria(lista, -1))