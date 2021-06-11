"""Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных."""
from collections import Counter


class Node:
    def __init__(self, char="", value=None, left=None, right=None):
        self.char = char
        self.value = value
        self.left = left
        self.right = right

    def __add__(self, other):
        if isinstance(other, Node):
            char = self.char + other.char
            value = self.value + other.value
            return Node(char, value, left=self, right=other)
        else:
            raise TypeError

    def show_tree(self, indent=0):
        if self.right:
            self.right.show_tree(indent + 8)
        print(f"{' ' * indent}* |{self.char}|")
        if self.left:
            self.left.show_tree(indent + 8)


class HuffmanCodec:
    """
    Один экземпляр класса строит только одно бинарное дерево для последовательности символов,
        чтобы закодировать новые символы создайте новый экземпляр
    1 строит бинарное древо, сохраняет голову дерева в переменную top_node
    2 _set_codes() рекурсивно обходит все ветви дерева с головы сохраняя путь в словарь
    3 _set_chars() заполняет обратный словрь для доступа к символу по его бинарному коду
    """
    def __init__(self, string):
        self.string = string
        self.top_node = self._build_tree()
        self.codes = self._set_char_codes(self.top_node) #self.top_node
        self.chars = self._set_chars()

    def _build_tree(self):
        char_count = Counter(self.string).most_common(len(Counter(self.string)))
        nodes = [Node(char, value) for char, value in char_count]
        if nodes:
            nodes.sort(key=lambda x: x.value)
            if len(nodes) == 1:
                new_node = Node(char=nodes[0].char, left=nodes[0])
            while len(nodes) > 1:
                new_node = nodes[0] + nodes[1]
                nodes = nodes[2:]
                nodes.append(new_node)
                nodes.sort(key=lambda x: x.value)
        return new_node

    def _set_char_codes(self, current_node, root='', res={}):
        """
        Рекурсивно читает дерево, сохраня путь
        Когда находит лепесток добавляет его название и путь в словарь codes
        """
        if len(current_node.char) > 1:
            if current_node.left:
                self._set_char_codes(current_node.left, root + '0')
            if current_node.right:
                self._set_char_codes(current_node.right, root + '1')
        else:
            res[current_node.char[0]] = root + '0'
        return res

    def _set_chars(self):
        return {code: char for char, code in self.codes.items()}

    def encode(self, text: str):
        res = ''
        if text:
            for char in text:
                if char in self.codes.keys():
                    res += self.codes[char] + ' '
                else:
                    raise Exception('Символ в объекте не закодирован')
        return res.rstrip()

    def decode(self, bits: str):
        res = ''
        if bits:
            for bit in bits.split():
                if bit in self.chars.keys():
                    res += chars[bit]
                else:
                    raise Exception('Код не соответствует ни одному из символов зашифрованному в объекте')
        return res

    def __str__(self):
        return  self.encode(self.string)


if __name__ == '__main__':
    beep = HuffmanCodec('beep boop beer!') # Beep boop beer!
    print(beep)
    print(beep.chars)
    print(beep.top_node.show_tree())


    """s = 'qweriuypoityrk;alkj;alskdgfjdghz,.mcbv.m,xb/n,/zcxv.mbma;asdog[poiu[iqw]pqwoyuoity139287503498657805135091-'
    huffman = HuffmanCodec(s)
    print(huffman)
    huffman.top_node.show_tree()"""
