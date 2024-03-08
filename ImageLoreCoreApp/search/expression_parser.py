import re

from ImageLoreCoreApp.search.query_value_executors import evaluate_value

OPERATORS = ['&', '+', '|', '-', '(', ')']
PREFIXES = ['#', '@', '/']


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def query(self):
        pass


class ExpressionParser:
    expression = ''
    tokens = []
    root = None

    def __init__(self, expression: str):
        self.expression = expression

    def preprocess(self):
        if len(self.tokens) == 0:
            self.tokens = ['*']
        # state, determines if last token is value
        last_token_is_value = False
        processed_tokens = []
        # for token, check if there is implicit "&" operations
        for token in self.tokens:
            # if encounters operator, then set state to false, and append the operator
            if token in OPERATORS:
                print('operator: ', token)
                last_token_is_value = False
            # if it's value token, then
            else:
                print('value: ', token)
                # check if last token is value token
                if last_token_is_value:
                    print('    add &')
                    # if so, then there's an implicit '&' operator in between
                    # append it
                    processed_tokens.append('&')
                # set the state to true, indicates that last token is operator
                last_token_is_value = True
            # and always append the operator at the end
            processed_tokens.append(token)
        print(processed_tokens)
        # and finally replace self.tokens with the processed one
        self.tokens = processed_tokens


    def tokenize(self):
        expression = self.expression
        for prefix in PREFIXES:
            expression = expression.replace(f'{prefix}', f' {prefix}')
        self.expression = expression
        print('after replace: ', expression)
        operator_pattern = '|'.join(re.escape(op) for op in OPERATORS)
        tokens = re.findall(r'[\w#@*/!！]+|[%s]' % operator_pattern, self.expression)
        print(tokens)
        self.tokens = tokens
        return tokens

    def parse(self):
        self.tokenize()
        self.preprocess()
        output_queue = []
        operator_stack = []

        precedence = {'!': 3, '*': 2, '+': 1, '|': 1, '&': 1, '-': 1}

        for token in self.tokens:
            if token not in OPERATORS:
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack[-1] == '(':
                    operator_stack.pop()  # Discard the '('
            else:
                while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        stack = []
        for token in output_queue:
            if token not in OPERATORS:
                node = Node(token)
                stack.append(node)
            else:
                node = Node(token)
                right = stack.pop()
                left = stack.pop()
                node.children.extend([left, right])
                stack.append(node)

        if len(stack) != 1:
            raise ValueError("Invalid expression format")

        self.root = stack[0]

    def evaluate(self):
        return self._evaluate_recursive(self.root)

    def _evaluate_recursive(self, node):
        if node.value not in OPERATORS:
            return evaluate_value(node.value)
        else:
            left = self._evaluate_recursive(node.children[0])
            right = self._evaluate_recursive(node.children[1])
            return self._evaluate_operation(node.value, left, right)

    def _evaluate_operation(self, operator, left, right):
        if operator == '&':
            return left & right
        elif operator == '+':
            return left | right
        elif operator == '|':
            return left | right
        elif operator == '-':
            return left - right

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, indent):
        print('  ' * indent + str(node.value))
        for child in node.children:
            self._print_tree_recursive(child, indent + 1)


# expression_parser = ExpressionParser("  #你好 + #我是 & ( @一个 | *aaa ) ")
# expression_parser = ExpressionParser("#世界  #你好 + #我是 & ( ！@一个 | !*aaa ) - (/myfolders - ( #未分类 + @作者 - @灵魂) + *)")
# expression_parser = ExpressionParser('#小式建筑')
# expression_parser.parse()
# expression_parser.print_tree()
# result = expression_parser.evaluate()
# print(result)
