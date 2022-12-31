#NAME:MALIK ABDUL HADI
#REG NO: 200901053
#COURSE: COMPILER CONSTRUCTION
#MODULE 2 FROM THE ASSIGNMENT:
import ast #IMPORTING AST(ABSTRACT SYNTAX TREE) PYTHON LIBRARAY


#Defining function that will take expression and will perform parse tree.
def parse_tree_expression(expression):
    return ast.parse(expression)

#Defining function that will print the tree.
def print_abstract_syntax_tree(tree):
    print("Abstract syntax tree",ast.dump(tree))

print("ABSTRACT SYNTAX TREE GENERATOR: ")
print("________________________________")
print("\n")
#taking regular expression from the user.
expression = str(input("Please, enter the expression: "))
#printing the original expression inputted from the user
print("OUTPUT OF THE ORIGINAL EXPRESSION: ", expression)
print("\n")
#calling function and passing expression that was inputted from the user to the function.
tree = parse_tree_expression(expression)
#printing the tree.
print_abstract_syntax_tree(tree)