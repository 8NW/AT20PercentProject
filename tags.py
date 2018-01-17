

import pickle
import re

file = open("htmltags.text", "r") 


tags = {}
index = 0

for line in file:
	pattern = re.compile("\<\s*(.*?)\s*\>")
	res = pattern.match(line)

	if res:
		tag = res.group(1)
		print(str(index) + ": " + tag)
		tags[tag] = index
		index += 1


#print(tags['<picture>'])

pkl_file = open('tags_dict.pkl', 'wb')
pickle.dump(tags, pkl_file)