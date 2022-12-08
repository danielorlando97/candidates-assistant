import spacy



class CustomTokenizer:
    def __init__(self) -> None:
        self.nlp = spacy.load("en_core_web_sm")
        self.index = {} 


    def skipper(self, token: spacy.tokens.Token):
        return (token.is_stop or token.is_punct)

    def analyze(self, text: str, text_id):
        for token in self.nlp(text):
            if self.skipper(token): continue

            try:
                self.index[token.text.lower()].add(text_id)
            except KeyError:
                self.index[token.text.lower()] = set([text_id])

    @property
    def index_list(self):
        for i, doc_list in self.index.items():
            yield {
                "name": i,
                'doc_list': doc_list
            }
