# using langchain 
# download model on our system and then use it  along with langchain as interface 
# we did this in HuggingFaceCore but there langchain was not used as interface to talk to HF.

from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens = 100
    )
)
# it will be downloaded (2.1 GB) delete it after use.

model = ChatHuggingFace(llm=llm)

response = model.invoke("where is auckland situated ?")
print(response.content)