from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from llama_index.core import StorageContext, load_index_from_storage
from pydantic import BaseModel
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
import ollama
import json

import os

Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

Settings.llm = Ollama(model="qwen2:0.5b", request_timeout=10.0)

app = FastAPI()

prompts = ["You are a world-renowned professor, you will be explaining concisely the following topic: {topic}.",
          "Explain the topic of {topic} in gangster terms."]

class Document(BaseModel):
    file:str

@app.post("/itemy/")
def send(doc:Document):
    if not os.path.exists('docs'):
        os.mkdir('docs')
    with open('docs/textbook.txt', 'w') as f:
        f.write(doc.file)
    
    # Run inference with the LLaMA model
    response = ollama.chat(model="qwen2:0.5b",
                   messages=[{"role": "user", "content": f"Given the context: {doc.file[:500]}, lift up the most important topic and use 3 words to describe it."}])
    
    topics = [response.message.content]
    
    persist_dir = './index'
    documents = SimpleDirectoryReader("docs").load_data()

    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=persist_dir)

    persist_dir = './index'
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

    # load index
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    
    return_dict = {}
    for t in topics:
        return_dict[t] = []
    for p in prompts:
        for t in topics:
            response = query_engine.query(p.format(topic=t))
            return_dict[t].append(response.response)
    
    return_obj = json.dumps(return_dict)
    return return_obj


@app.get("/video/{index}")
def video1(index:int):
    return FileResponse(f"vid{index}.mp4")