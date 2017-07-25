user_words = []
for mad_libs_categories in ['adjective', 'adverb', 'proper noun', 'color', 'part of the body', 'plural noun', 'verb']:
	user_words.insert(len(user_words),input('Give us a word that\'s a ' + mad_libs_categories + ' --> '))
print(user_words)