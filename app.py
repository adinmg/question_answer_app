from flask import Flask, request, render_template
from flask_caching import Cache
from transformers import pipeline

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

model_checkpoint = "josueadin/miniLM-finetuned-squad"

@cache.memoize(timeout=99999)
def create_question_answerer():
    return pipeline("question-answering", model=model_checkpoint)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        mydict = request.form
        context = mydict.get("context", "")
        question = mydict.get("question", "")
        if context:
            question_answerer_cached = create_question_answerer()
            prediction = question_answerer_cached(question=question, context=context)
            answer = prediction.get("answer", "")
            score = prediction.get("score", "")
            formatted_score = "{:.2%}".format(score)
            return render_template("index.html", question=question, context=str(context)[:100], answer=answer, score=formatted_score, showresult=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
