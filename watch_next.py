# head
print("""
=========================================================================
                            MOVIE PICKER
=========================================================================
""")

# Comparison String
comparator = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Create variable for loading text into
descriptions = []

# Iterate through input text, and load into descriptions variable
with open('movies.txt', 'r+') as text:
    for line in text:
        descriptions += line.rstrip().split('\n')

# Import spacy, load md model
import spacy
nlp = spacy.load('en_core_web_md')

# Pass comparison text through model
comparison_text = nlp(comparator)

# Variables for holding highest similarity ND NAME OF MOVIE
highest = 0
most_similar = ""

# Iterate through descriptions, comparing each movie description (less the name) to the comparison
for description in descriptions:
    similarity = nlp(description[9:]).similarity(comparison_text)
    # print(similarity, " = ",  description[9:150] + "...")
    # Update the highest score and name variables where highest similarity exceeded
    if similarity > highest:
        highest = similarity
        most_similar = f"{description[0:7]}"
    else:
        continue

# Output results to console
print(f"""The movie most simlar to Planet Hulk, description:

'{comparator}'

is > {most_similar}, {highest}.

We recommend that you watch {most_similar} next!!!
""")
