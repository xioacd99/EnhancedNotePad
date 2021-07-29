import ast

from numpy import *
from ast import *


class NodeRewriter(ast.NodeTransformer):
    def visit_Import(self, node: Import):
        return None

    def visit_ImportFrom(self, node: ImportFrom):
        return None

    def visit_Name(self, node: Name):
        new_node = Name(node)
        new_node.id = ''
        return new_node


class TreeCheck(object):
    def distance(self, v1, v2):
        sum = 0.0
        for i in range(len(v1)):
            sum += (v1[i] - v2[i]) ** 2
        return sqrt(sum)

    def Levenshtein(self, a, len_a, b, len_b):
        if len_a == 0 or len_b == 0:
            return len_a if (len_b == 0) else len_b

        re1 = self.Levenshtein(a, len_a - 1, b, len_b) + 1
        re2 = self.Levenshtein(a, len_a, b, len_b - 1) + 1
        re3 = self.Levenshtein(a, len_a - 1, b, len_b - 1) + (0 if (a[len_a - 1] == b[len_b - 1]) else 1)

        return min(array([re1, re2, re3]))

    def Levenshtein_distance(self, str1, str2):
        return self.Levenshtein(str1, len(str1), str2, len(str2))

    def NodeVector(self, ast_root):
        ast_root.vector = array([0 for i in range(10)])
        for cn in iter_child_nodes(ast_root):
            self.NodeVector(cn)

    def CalculateVector(self, ast_root):
        # Literals
        if isinstance(ast_root, Constant) \
                or isinstance(ast_root, FormattedValue) \
                or isinstance(ast_root, JoinedStr) \
                or isinstance(ast_root, List) \
                or isinstance(ast_root, Tuple) \
                or isinstance(ast_root, Set) \
                or isinstance(ast_root, Dict):
            ast_root.vector[0] += 1

        # Variables
        if isinstance(ast_root, Name) \
                or isinstance(ast_root, Load) \
                or isinstance(ast_root, Store) \
                or isinstance(ast_root, Del) \
                or isinstance(ast_root, Starred):
            ast_root.vector[1] += 1

        # Expressions
        if isinstance(ast_root, Expr) \
                or isinstance(ast_root, UnaryOp) \
                or isinstance(ast_root, UAdd) \
                or isinstance(ast_root, USub) \
                or isinstance(ast_root, Not) \
                or isinstance(ast_root, Invert) \
                or isinstance(ast_root, Add) \
                or isinstance(ast_root, Sub) \
                or isinstance(ast_root, Mult) \
                or isinstance(ast_root, Div) \
                or isinstance(ast_root, FloorDiv) \
                or isinstance(ast_root, Mod) \
                or isinstance(ast_root, Pow) \
                or isinstance(ast_root, LShift) \
                or isinstance(ast_root, RShift) \
                or isinstance(ast_root, BitOr) \
                or isinstance(ast_root, BitXor) \
                or isinstance(ast_root, BitAnd) \
                or isinstance(ast_root, MatMult) \
                or isinstance(ast_root, BoolOp) \
                or isinstance(ast_root, And) \
                or isinstance(ast_root, Or) \
                or isinstance(ast_root, Compare) \
                or isinstance(ast_root, Eq) \
                or isinstance(ast_root, NotEq) \
                or isinstance(ast_root, Lt) \
                or isinstance(ast_root, LtE) \
                or isinstance(ast_root, Gt) \
                or isinstance(ast_root, GtE) \
                or isinstance(ast_root, Is) \
                or isinstance(ast_root, IsNot) \
                or isinstance(ast_root, In) \
                or isinstance(ast_root, NotIn) \
                or isinstance(ast_root, Call) \
                or isinstance(ast_root, keyword) \
                or isinstance(ast_root, IfExp) \
                or isinstance(ast_root, Attribute) \
                or isinstance(ast_root, NamedExpr):
            ast_root.vector[2] += 1

        # Subscripting
        if isinstance(ast_root, Subscript) \
                or isinstance(ast_root, Slice):
            ast_root.vector[3] += 1

        # Comprehensions
        if isinstance(ast_root, ListComp) \
                or isinstance(ast_root, SetComp) \
                or isinstance(ast_root, GeneratorExp) \
                or isinstance(ast_root, DictComp) \
                or isinstance(ast_root, comprehension):
            ast_root.vector[4] += 1

        # Statements
        if isinstance(ast_root, Assign) \
                or isinstance(ast_root, AnnAssign) \
                or isinstance(ast_root, Raise) \
                or isinstance(ast_root, Assert) \
                or isinstance(ast_root, Delete) \
                or isinstance(ast_root, Pass):
            ast_root.vector[5] += 1

        # Imports
        if isinstance(ast_root, Import) \
                or isinstance(ast_root, ImportFrom) \
                or isinstance(ast_root, alias):
            ast_root.vector[6] += 1

        # Control flow
        if isinstance(ast_root, If) \
                or isinstance(ast_root, For) \
                or isinstance(ast_root, While) \
                or isinstance(ast_root, Break) \
                or isinstance(ast_root, Continue) \
                or isinstance(ast_root, Try) \
                or isinstance(ast_root, ExceptHandler) \
                or isinstance(ast_root, With) \
                or isinstance(ast_root, withitem):
            ast_root.vector[7] += 1

        # Function and class definitions
        if isinstance(ast_root, FunctionDef) \
                or isinstance(ast_root, Lambda) \
                or isinstance(ast_root, arguments) \
                or isinstance(ast_root, arg) \
                or isinstance(ast_root, Return) \
                or isinstance(ast_root, Yield) \
                or isinstance(ast_root, YieldFrom) \
                or isinstance(ast_root, Global) \
                or isinstance(ast_root, Nonlocal) \
                or isinstance(ast_root, ClassDef):
            ast_root.vector[8] += 1

        # Async and await
        if isinstance(ast_root, AsyncFunctionDef) \
                or isinstance(ast_root, Await) \
                or isinstance(ast_root, AsyncFor) \
                or isinstance(ast_root, AsyncWith):
            ast_root.vector[9] += 1

        # Add child node vector value
        for cn in iter_child_nodes(ast_root):
            self.CalculateVector(cn)
            ast_root.vector[0:10] += cn.vector[0:10]

    def strCheck(self, src_1, src_2):
        # Get AST from different src file
        fo1 = open(src_1, "r")
        src_code1 = fo1.read()
        ast_root_1 = parse(src_code1)

        fo2 = open(src_2, "r")
        src_code2 = fo2.read()
        ast_root_2 = parse(src_code2)

        # modify node structure
        nrw = NodeRewriter()
        nrw.visit(ast_root_1)
        nrw.visit(ast_root_2)

        self.NodeVector(ast_root_1)
        self.NodeVector(ast_root_2)

        self.CalculateVector(ast_root_1)
        self.CalculateVector(ast_root_2)

        # find the closet node in different ast
        Distance = sys.maxsize
        close_pair_ast1_node = ast_root_1
        close_pair_ast2_node = ast_root_2

        for ast1_node in walk(ast_root_1):
            for ast2_node in walk(ast_root_2):
                v1 = ast1_node.vector
                v2 = ast2_node.vector
                if sum(v1) > 20 and sum(v2) > 20:
                    d = self.distance(v1, v2)
                    if d < Distance:
                        close_pair_ast1_node = ast1_node
                        close_pair_ast2_node = ast2_node
                        Distance = d

        # use those node to calculate similarity

        str1 = dump(close_pair_ast1_node)
        str2 = dump(close_pair_ast2_node)

        for ch in str1:
            if not ch.isalpha():
                str1 = str1.replace(ch, ' ')

        for ch in str2:
            if not ch.isalpha():
                str2 = str2.replace(ch, ' ')

        split_str1 = str1.split()
        split_str2 = str2.split()
        dict1 = {}.fromkeys(split_str1 + split_str2, 0)
        dict2 = {}.fromkeys(split_str1 + split_str2, 0)

        for word in split_str1:
            dict1[word] += 1

        for word in split_str2:
            dict2[word] += 1

        vec1 = list(dict1.values())
        vec2 = list(dict2.values())

        print(vec1)
        print(vec2)

        cos = dot(vec1, vec2) / (self.distance(vec1, [0 for i in vec1]) * self.distance(vec2, [0 for i in vec1]))
        Euler_similarity = cos

        return Euler_similarity

    def fileCheck(self, lFile, rFile):
        results = 0
        if os.path.exists(lFile) and os.path.exists(rFile):
            with open(lFile, 'r',encoding='utf-8') as lFin:
                with open(rFile, 'r',encoding='utf-8') as rFin:
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine and rLine:
                    results += self.strCheck(lLine, rLine)
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine:
                    results += self.strCheck(lLine, '')
                    lLine = lFin.readline()
                while rLine:
                    results += self.strCheck('', rLine)
                    rLine = rFin.readline()
        else:
            print('%s or %s does not exited, please check whether the file path is correct' % lFile, rFile)
        return results


if __name__ == '__main__':
    test = TreeCheck()
    ans = test.fileCheck('ENTest.txt', 'CETest.txt')
    print(ans)
