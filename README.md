# Lexical-Analyzer-and-Syntax-Tree-Generator

# 200901053_Assign_02 ===>>> LEXICAL ANALYZER CODE
# 200901053_Assign_2 ===>>> SYNTAX TREE CODE

# Algorithm for lexical analyzing:

1.	Split the expression into individual tokens using a regular expression or a set of rules that define what constitutes a token. For example, you could use the following regular expression to tokenize an arithmetic expression: '[\d\w]+|[\+\-\*\/\(\)]'
2.	This regular expression will match one or more digits or letters (to recognize variables or numbers), or one of the following characters: +, -, *, /, (, and ).
3.	You can use a library like re in Python to apply this regular expression to the expression and extract the tokens.
4.	The regular expression used for tokenization should be designed to match the tokens that are relevant to the language or domain you are working with.
5.	In the case of an arithmetic expression, the regular expression should be able to recognize variables (i.e., letters), numbers (i.e., digits), and the four basic arithmetic operations (i.e., +, -, *, and /). It should also be able to recognize parentheses, as they are used to indicate the order of operations.
6.	Outputting tags/tokens:
7.	Once the expression has been tokenized, you can output the tags/tokens by iterating through the list of tokens and printing or storing each one.
8.	For example, given the input 'a+(b*c)', the output could be: ['a', '+', '(', 'b', '*', 'c', ')'].

# Explanation of Lexical Analyzer Code:

In this code I have used re library that provides a set of powerful regular expression facilities, which allows you to quickly check whether a given string matches a given pattern (using the match function) or contains such a pattern (using the search function).
Then I predefined tokens such as for for Alpanumeric characters, for numeric characters, for plus, for mins, for division, for multiplication, for left paranthesis and for right paranthesis.
After that I used .join() function that takes all items in an iterable and joins them into one string and stored those iterated items into a variable named Regularexpression_tokens.
After that I defined a function named tokenize(expression) that will take expression as argument and the purpose of this function is to return the tokens from the expression. In this function I have used built in function findall() that is used to find all the matches and returns them as a list of strings, with each string representing one match. And after that we returned the tokens.
Now in the main block, we are taking regular expression input from the user and storing that regular expression in the variable name regularexpression that was passed in the tokenize(expression) function.
Now in the last we will after inputting the expression from the user we will get the original output that was entered by the user and we will get tokens as output.

# OUTPUT OF Lexical Analyzer Code:

![image](https://user-images.githubusercontent.com/92660593/210151075-e0939002-6697-4156-9553-cfddf2e5142b.png)
![image](https://user-images.githubusercontent.com/92660593/210151078-9e917c92-730c-4ae7-be79-b06b69ff5257.png)


# Explanation of Syntax Tree Code:

In this code we are using ast (ABSTRACT SYNTAX TREE) library that is a built-in Python module that allows you to parse Python code and generate an abstract syntax tree. You can then use this tree to analyze or modify the code in various ways.
In this code we have defined two functions, 
First function parse_tree_expression(expression) that will take expression and will perform the functionality and generate parse tree we have used ast.parse() function that splits the source code into tokens based on the grammar. These tokens are then transformed to build an Abstract Syntax Tree. And the tokens will be returned. This parse_tree_expression  function takes argument that is expression it is taken from the user in the main block.
Then the second function is print_abstract_sytax_tree(tree) that prints the tree. We have used ast.dump() function that is used to print abstract syntax tree. And it takes argument tree.
Now in the main block, we are taking regular expression input from the user. And storing that expression into the variable named expression and this was passed in parsed_tree_expression function. That generated tokens now we are storing these tokens in tree variable and passing this tree variable in second function that was print_abstract_syntax_tree(tree) that will print the tree and this will be the output.

# Output of Syntax Tree Code:

![image](https://user-images.githubusercontent.com/92660593/210151086-44e6f171-e61c-48d5-9c76-af742d1787e7.png)
![image](https://user-images.githubusercontent.com/92660593/210151093-0a0e100e-db4d-4edc-a746-4065c2b746a6.png)
![image](https://user-images.githubusercontent.com/92660593/210151100-7ae7092a-c4cd-4824-a35c-4e122b896625.png)



