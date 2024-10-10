import nltk
from nltk.corpus import stopwords
from gensim import corpora
from gensim.models.ldamodel import LdaModel
nltk.download('stopwords')

# Step 1: Preprocess the text and split into individual articles
articles = [
    "Actress Jenna Fischer has revealed she has been receiving treatment for breast cancer since December last year.",
    "A Nepalese teenager has broken the world record for the youngest mountaineer to summit Earth’s 14 highest peaks.",
    "Hurricane Milton has made landfall in Florida, with US officials warning that 'life-threatening storm surge, extreme winds and flash flooding' are occurring in central parts of the southern state.",
    "A new book by veteran Watergate reporter Bob Woodward says Donald Trump secretly sent coveted Covid-19 testing machines to Vladimir Putin for personal use when they were in short supply, a claim angrily dismissed by the Trump campaign.",
    "The northern Indian state of Haryana and Indian-administered Kashmir sprang surprises on Tuesday as votes were counted in assembly elections there."
]

# Step 2: Tokenize and clean each article
stop_words = set(stopwords.words('english'))

def preprocess_article(article):
    return [word for word in article.lower().split() if word.isalpha() and word not in stop_words]

# Preprocess all articles
preprocessed_articles = [preprocess_article(article) for article in articles]

# Step 3: Create a dictionary and a document-term matrix for all articles
dictionary = corpora.Dictionary(preprocessed_articles)
corpus = [dictionary.doc2bow(article) for article in preprocessed_articles]

# Step 4: Apply LDA model
lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)

# Step 5: Print the topics for each article
topics = lda_model.print_topics(num_words=4)
for topic in topics:
    print(topic)

