s = 'abc2306cba'
print(s.translate({ord(i): None for i in 'abc'}))
