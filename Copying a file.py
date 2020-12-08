fileInput = open('e:\\Kalai Python\Sample Text file.txt')
fileContent = fileInput.read()
fileInput.close()
outFile = open('e:\\Kalai Python\Sample Out Text file.txt','w')
outFile.write(fileContent)
outFile.close()

