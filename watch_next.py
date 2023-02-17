import spacy
nlp = spacy.load('en_core_web_md')

#Sentence to compare
Planet_Hulk_with_the_description = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator'''

# EMpty list to append similarity values in it 
similarity_list = []
#empty dictionary to add movie name and similarity in it 
dict = {}

model_sentence = nlp(Planet_Hulk_with_the_description)
movie_open = open('movies.txt')
movie_read = movie_open.readlines()
for movie in movie_read:
    movie_split = movie.split(' :')
    movie_description = movie_split[1]
    movie_name = movie_split[0]
    similarity = nlp(movie_description).similarity(model_sentence)
    dict[movie_name] = similarity
    similarity_list.append(similarity)
movie_open.close()
# max similarity value
max = max(similarity_list)
# print the the most similar movie
for movie in dict:
    if dict[movie] == max :
      print(f"The most similar movie is : [{movie}] .")