from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredFileLoader, DirectoryLoader
from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceHubEmbeddings
import pickle
import os
from dotenv import load_dotenv
load_dotenv()

huggingfacehub_api_token = "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";
openai_api_key = "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"



# loader = DirectoryLoader('/dirload', glob="**/*.txt")
# raw_documents = loader.load()
#Load Data
loader = UnstructuredFileLoader("empclean.txt")

raw_documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap  = 20)
documents = text_splitter.split_documents(raw_documents)


# Load Data to vectorstore
#openai_api_key=openai_api_key
#embeddings = OpenAIEmbeddings()
embeddings = HuggingFaceHubEmbeddings(huggingfacehub_api_token=huggingfacehub_api_token)
vectorstore = FAISS.from_documents(documents, embeddings)
#vectorstore = Chroma.from_documents(documents,embeddings)

# Save vectorstore
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)
