glossary = {
  'indentation' : "Indentation refers to the spaces at the beginning of a code line.", 
  'string': "A series of characters.",
  'list': "A collection of items in a particular order.", 
  'Set' : "A set is an unordered, and unchangeable, collection.", 
  'comments' : "Comments are code lines that will not be executed.",
  'dictionary' : "A collection of key-value pairs.",
  'print' : "The print() function literally prints the result to the screen.",
  'input' : "It allows us to get input from the user.",
  'Int' :	"The integer number type.",
  'Arithmetic Operators' : "Arithmetic operator are used to perform common mathematical operations."
   }


for word,definition in glossary.items():
    print( word.title() + " : " + definition)
  
