"""Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных."""
from collections import Counter


class Node:
    def __init__(self, char="", value=None, left=None, right=None):

        self.char = char
        self.value = value
        self.left = left
        self.right = right

    def view_structure(self, indent=0):
        if self.right:
            self.right.view_structure(indent + 8)
        print(f"{' ' * indent}*{' ' * (indent + 10)}/{self.char}/ -- {self.value}")
        if self.left:
            self.left.view_structure(indent + 8)



class HuffmanCodec:
    """
    Один экземпляр класса строит только одно бинарное дерево для последовательности символов
    1 класс получает строку при инициализации класса
    2 _build_tree() строит дерево Хаффмана, сохраняет голову дерева в переменную top_node
    3 _get_codes() вызывает рекурсивную функцию для поиска пути до каждого символа строки в дереве,
        сохраняет результаты в словарь - теперь мы можем получить доступ к коду символа
    4 _get_chars() заполняет обратный словрь, чтобы мы могли получить доступ к символу по его бинарному коду
    5 кодирует строку переданную при инициализации и выводит ее на экран
    """
    def __init__(self, string):

        self.string = string
        self.top_node = self._build_tree()
        self.char_code = self._read_nodes(self.top_node) #self.top_node
        self.code_char = self._get_chars()

    def _build_tree(self):
        char_count = Counter(self.string).most_common(len(Counter(self.string)))
        nodes = [Node(char, value) for char, value in char_count]

        if nodes:
            nodes.sort(key=lambda x: x.value)
            if len(nodes) < 2:
                top_node = Node(char=nodes[0].char, value=1, left=nodes[0])
                return
        else:
            return

        while len(nodes) > 2:
            new_node = Node(char=nodes[0].char + nodes[1].char,
                            value=nodes[0].value + nodes[1].value,
                            left=nodes[0], right=nodes[1])
            nodes = nodes[2:]
            nodes.append(new_node)
            nodes.sort(key=lambda x: x.value)

        top_node = Node(char=nodes[0].char + nodes[1].char,
                        value=nodes[0].value + nodes[1].value,
                        left=nodes[0], right=nodes[1])
        return top_node

    def _read_nodes(self, current_node, root='', res={}):
        """ Дерево строится снизу и каждму верхнему узлу передаются символы его потомков
            Таким образом голова дерева будет содержать все символы из последовательности """
        if len(current_node.char) > 2:
            if current_node.left:
                self._read_nodes(current_node.left, root + '0')
            if current_node.right:
                self._read_nodes(current_node.right, root + '1')
        else:
            res[current_node.char[0]] = root + '0'
            if len(current_node.char) == 2:
                res[current_node.char[1]] = root + '1'
        return res

    def _get_chars(self):
        return {code: char for char, code in self.char_code.items()}

    def encode(self, string):
        return ' '.join(self.char_code[i] for i in string)

    def decode(self, bit_string):
        return ''.join(self.code_char[i] for i in bit_string.split())

    def __str__(self):
        return  f'{self.string} - {self.encode(self.string)}'


if __name__ == '__main__':
    beep_beer = HuffmanCodec('beep boop beer!') # Beep boop beer!
    print(beep_beer)

    s = 'qweriuypoityrk;alkj;alskdgfjdghz,.mcbv.m,xb/n,/zcxv.mbma;asdog[poiu[iqw]pqwoyuoity139287503498657805135091-'
    huffman = HuffmanCodec(s)
    print(huffman)
    huffman.top_node.view_structure()
