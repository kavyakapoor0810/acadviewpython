#question3

import re
sentence = "A, very very; irregular_sentence"
ee1=re.sub("[;_:,]"," ",sentence)
print(ee1)