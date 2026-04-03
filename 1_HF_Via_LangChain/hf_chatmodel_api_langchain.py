# hugginface using api key.
# here it is langchain vala hugging face.

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.3-70B-Instruct",
    task = "text-generation",
    huggingfacehub_api_token= "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"
)

model = ChatHuggingFace(llm=llm)

# rest all is same as you normally interact with a llm in langchain

response = model.invoke("Who is the PM of Italy?")

# print(response)
# print("--------------------------")
print(response.content)