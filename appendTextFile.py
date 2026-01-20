print ("Jarand5122")
path="C:\\PythonFiles\\myTextFile.txt"
fopen=open(path, "a")
fopen.write('\n' + "This is the third line of text in my file.")

#ensures new text is written to file
fopen.flush()

fopen.close