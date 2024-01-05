import vertexai
from vertexai.preview.language_models import TextGenerationModel
import pandas as pd

data = pd.read_csv("Coursera.csv").head(10).to_markdown(index=False)
prompt = '''
input: This table contains information about courses. The first row includes the table headers, while each subsequent row displays the corresponding data separated by the "|" symbol.
{data}

input: {review}
'''

def predict_large_language_model(
    model_name: str,
    temperature: float,
    max_output_tokens: int,
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
        max_output_tokens=max_output_tokens,
        top_k=top_k,
        top_p=top_p,)
    return response.text

review = "Please recommend me one course name which university is 'ISES Business School'"

content = prompt.format(review=review, data=data)

response_text = predict_large_language_model(
    "text-bison@001", 
    temperature=0.2, 
    max_output_tokens=256, 
    top_p=0.8, 
    top_k=1, 
    content=content)
print(response_text)
