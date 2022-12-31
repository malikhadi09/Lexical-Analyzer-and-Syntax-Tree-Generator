#NAME:MALIK ABDUL HADI
#REG NO: 200901053
#COURSE: COMPILER CONSTRUCTION
#MODULE 1 FROM THE ASSIGNMENT:
import re #IMPORTING RE LIBRARY FROM THE PYTHON

# defining the tokens
#for Alpanumeric characters:
Alphanumeric = r'[a-zA-Z][a-zA-Z0-9]*'
#for numeric characters:
Integernumericvalues = r'\d+'
#for plus:
plus = r'\+'
#for minus:
minus = r'\-'
#for division:
division = r'/'
#for multiplication:
multiplication = r'\*'
#for left paranthesis:
openingparanthesis = r'\('
#for right paranthesis:
closingparanthesis = r'\)'



# Regular expression for all tokens
Regularexpression_tokens= '|'.join([Alphanumeric,Integernumericvalues,plus, minus,division, multiplication, openingparanthesis, closingparanthesis ])

#defining function that will return the tokens.
def tokenize(expression):
  # Use the regular expression to find all tokens in the input string
  tokens = re.findall(Regularexpression_tokens, expression)
  return tokens


print(" Lexical Analyzer")
print("__________________")
print("\n")
#Taking regular expression input from the user
regularexpression=str(input("Please enter any expression: "))
print("\n")
print("ORIGINAL INPUTED EXPRESSION: ", regularexpression)
print("\n")
#Printing the tokens of inputed expression
print("TOKENS OF INPUTED EXPRESSION: ",tokenize(regularexpression))
