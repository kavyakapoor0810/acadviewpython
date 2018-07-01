#question2


import re
t = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
s=re.findall(r'[Bb][\w]{1,20}',t)
print(s)


#question3
sentence = "A, very very; irregular_sentence"
red=re.sub("[;_:,]"," ",sentence)
print(red)

#question4

def show (blue):
    blue=re.sub("http\S+\s"," ",blue)
    blue=re.sub("RT"," ",blue)
    blue=re.sub("cc"," ",blue)
    blue=re.sub("#\S+"," ",blue)
    blue = re.sub("@\S+", " ", blue)
    blue = re.sub("\!", " ", blue)
    blue = re.sub("\:", " ", blue)
    blue=re.sub("\s+"," ",blue)
    return blue

blue = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(show(blue))