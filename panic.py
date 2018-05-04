phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#new_phrase = plist[1:8]
#new_phrase.remove("'")
#new_phrase.extend([new_phrase.pop(),new_phrase.pop()])
#new_phrase.insert(2,new_phrase.pop(3))

new_phrase =''.join(plist[1:3])

new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])

#new_phrase = ''.join(new_phrase)   
print(new_phrase)
