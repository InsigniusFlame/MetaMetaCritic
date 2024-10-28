from scraper import review_text_list
from transformers import AutoTokenizer, AutoModelForSequenceClassification,pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

documents = review_text_list
tfidf = TfidfVectorizer(max_df=0.85, stop_words='english')
tfidf_matrix = tfidf.fit_transform(documents)
keywords = tfidf.get_feature_names_out()
print(keywords) # This is getting dogshit results

model_name = "yangheng/deberta-v3-base-absa-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name,use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("text-classification", model=model,tokenizer=tokenizer)

for review in review_text_list:
    for keyword in keywords:
        if keyword not in review:
            continue
        else:
            print(keyword,classifier(review,text_pair=keyword))