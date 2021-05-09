try:
    import nltk
    from fastapi import Request
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from nltk.tokenize.treebank import TreebankWordTokenizer
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    from aitextgen import aitextgen
    from transformers import pipeline
    import uvicorn

except Exception as e:
    print("Some modules could not be imported {}".format(e))


classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
generator = pipeline('text-generation', model='gpt2')
ai = aitextgen()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/api')
async def index():
    return {'message': 'Hello World!'}


@app.post('/api/tokenize')
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


@app.post('/api/detokenize')
async def detokenize(request: Request):
    body = await request.json()
    tokens = body["tokens"]
    return {"text": TreebankWordDetokenizer().detokenize(tokens)}


@app.post('/api/generate')
async def generatorTextgen(request: Request):
    body = await request.json()
    prompt_text = body["prompt_text"]
    generated_text = ai.generate_one(prompt=prompt_text, max_length=100)
    return {
        "generated_text": generated_text
    }


@app.post('/api/classify')
async def classify(request: Request):
    body = await request.json()
    sentence = body["sentence"]
    labels = [
        "Happy",
        "Enthusiasm",
        "Discontentment",
        "Frustration",
        "Gratitude",
        "Trust",
        "Confusion",
        "Neutral"
        ]
    data = classifier(sentence, labels, multi_label=True)
    emotions = dict(zip(data['labels'], data['scores']))
    confidence = max(emotions.values())
    for k, v in emotions.items():
        if v == confidence:
            emotion = k
    return{
        "Highest_emotion": emotion,
        "Confidence": confidence,
        "Emotions": emotions
    }


@app.post('/api/generate/gpt2')
async def generatorGpt2(request: Request):
    body = await request.json()
    prompt_text = body["prompt_text"]
    text = generator(
        prompt_text,
        max_length=100,
        num_return_sequences=1
        )
    generated_text = text[0]["generated_text"]
    return {
        "generated_text": generated_text
    }


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5555, reload=True)  # workers=4
