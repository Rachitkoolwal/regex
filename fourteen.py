words = []
with  open('demo.txt','r')  as  f:
      for line in f:
        words.extend(line.split())

from collections import Counter
from itertools import count 
counts = Counter(words)
most_frequent_word = count.most_common(1)
print(most_frequent_word)    
