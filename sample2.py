import vertexai
from vertexai.preview.language_models import TextGenerationModel

prompt = '''
input: I had to compare two versions of Hamlet for my Shakespeare class and unfortunately I picked this version…
Classify the sentiment of the message: negative

input: This Charles outing is decent but this is a pretty low-key performance….
Classify the sentiment of the message: negative

input: My family has watched Arthur Bach stumble and stammer since the movie first came out. We have most lines memorized…
Classify the sentiment of the message: positive

input: {review}
Classify the sentiment of the message:
'''

def predict_large_language_model(
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    tuned_model_name: str = "",
    ) :
    
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
      model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    return response.text

review = "Something surprised me about this movie - it was actually original. It was not the same old recycled crap that comes out of Hollywood every month. I saw this movie on video because I did not even know about it before I saw it at my local video store. If you see this movie available - rent it - you will not regret it."

content = prompt.format(review=review)

response_text = predict_large_language_model(
    "text-bison@001", 
    temperature=0.2, 
    max_decode_steps=5, 
    top_p=0.8, 
    top_k=1, 
    content=content)
print(response_text)
