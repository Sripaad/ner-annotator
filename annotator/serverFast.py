import nltk

from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
async def index():
    return {'message': 'Hello World!'}


@app.post('/tokenize')
async def tokenize(request: Request):
    body = await request.json()
    text = body["text"]
    print(text)
    try:
        spans = list(TreebankWordTokenizer().span_tokenize(text))
    except LookupError:
        nltk.download('punkt')
        spans = list(TreebankWordTokenizer().span_tokenize(text))
    return {"tokens": [(s[0], s[1], text[s[0]:s[1]]) for s in spans]}


@app.post('/detokenize')
async def detokenize(request: Request):
    body = await request.json()
    tokens = body["tokens"]
    return {"text": TreebankWordDetokenizer().detokenize(tokens)}
