paragraph = "Big Data refers to a collection of data that is so huge and complex that none of the traditional data management tools are able to store it or process it efficiently. according to Forbes there are 2.5 quintillion bytes of data created every day now you might be wondering how Big Data fools managed to handle such a huge amount of data when Netflix offers you personalized recommendations from its library of thousands of movies and TV shows that's big deer at work. With the growing increase in the volume of data big data will grow bigger. Demand for data management experts will shoot out the gap between the demand for data professionals and the availability will widen. This will help data scientists and analysts draw higher salaries. Start learning this trending technology using antiochus expertly curated courses.  "


import wikipediaapi
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

def get_bart_summary(paragraph):

    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    inputs = tokenizer(paragraph, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary.strip()

def decide_title_from_summary(summary):

    summary_words = summary.split()
    if len(summary_words) >= 2:
        return ' '.join(summary_words[:2]).strip()
    elif summary_words:
        return summary_words[0].strip()
    else:
        return "No title found"

def search_on_wikipedia(title):
    wiki_wiki = wikipediaapi.Wikipedia('VidSense (auuchavan@gmail.com)', 'en')

    page_py = wiki_wiki.page(title)

    if page_py.exists():
        print("\nWikipedia page found for the decided title:")
        return page_py.fullurl
    else:
        return f"\nNo Wikipedia page found for the decided title: {title}"

def main(paragraph):

    summary = get_bart_summary(paragraph)

    print("\nSummary of the paragraph:")
    print(summary)

    title = decide_title_from_summary(summary)

    print("\nDecided Title:")
    print(title)

    link = search_on_wikipedia(title)
    return link 

if __name__ == "__main__":
    main(paragraph)
