from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI, HuggingFacePipeline, HuggingFaceHub, openai
from langchain.chains import ChatVectorDBChain
import os
from dotenv import load_dotenv
load_dotenv()
huggingfacehub_api_token =  os.environ.get('huggingfacehub_api_token')
openai_api_token = os.environ.get('openai_api_key')

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
You can assume the question about the financial markets/bonds/equties/and anything that is realted to finance.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """You are an AI assistant for answering questions about finance.
You are given the following extracted parts of a long documents and a question. Provide a conversational answer.
If you don't know the answer, just say "MY COCK IS HARD" Don't try to make up an answer.
If the question is not about the financial marekts please inform the user that you cant answer the question.
Question: {question}
=========
{context}
=========
Answer in Markdown:"""


# _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
# You can assume the question about the most recent state of the union address.
#
# Chat History:
# {chat_history}
# Follow Up Input: {question}
# Standalone question:"""
# CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)
#
# template = """You are an AI assistant for answering questions about the most recent state of the union address.
# You are given the following extracted parts of a long document and a question. Provide a conversational answer.
# If you don't know the answer, just say "Hmm, I'm not sure." Don't try to make up an answer.
# If the question is not about the most recent state of the union, politely inform them that you are tuned to only answer questions about the most recent state of the union.
# Question: {question}
# =========
# {context}
# =========
# Answer in Markdown:"""
QA_PROMPT = PromptTemplate(template=template, input_variables=["question", "context"])
#    llm = HuggingFaceHub(repo_id="google/flan-t5-large", huggingfacehub_api_token=huggingfacehub_api_token, model_kwargs={"temperature":1e-10})
def get_chain(vectorstore):
    llm = HuggingFaceHub(repo_id="PygmalionAI/pygmalion-6b", huggingfacehub_api_token=huggingfacehub_api_token, model_kwargs={"temperature":1e-10})
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain

def get_chain2(vectorstore):
    llm = OpenAI(temperature=0, max_tokens=1500, model_name='text-davinci-003')
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        # qa_prompt=QA_PROMPT,
        # condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain
