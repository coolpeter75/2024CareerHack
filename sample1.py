import datetime
from vertexai.language_models import TextGenerationModel

text_generation_model = TextGenerationModel.from_pretrained("text-bison@001")

print("Start: ", datetime.datetime.now())
for response in text_generation_model.predict_streaming(
    prompt="Count to 100",
    max_output_tokens=1000
):
    print(datetime.datetime.now(), "|", response)
print("End: ", datetime.datetime.now())
