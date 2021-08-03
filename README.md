# PaperScript
A semi-parody esolang for writing very specific papers.


To run code: execute PaperScript.py with command line arguments of <file> <numbers>
  Numbers put after the file will be pushed to the stack

Code blocks are encapsulated around '<' and '>' and pushed to the stack.
  
  
## Additional Built-ins
  Built-in | Function
  -------- | --------
  L | Pops two values from the stack. Left value is how many times the loop should execute. Right value must be a string to be parsed as code.
  c | output the paper's conclusion paragraph
  g | output the paper's papargraph on golfing languages
  e | output the paper's introduction to escoteric languages
  r | output the paper's explanation on the terminology of the community
  b | output the paper's basic information about the Code Golf Stack Exchange Community
  i | output the paper's introduction to Code Golfing
