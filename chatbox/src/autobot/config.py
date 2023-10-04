import os
from ...config import settings
from elasticsearch import Elasticsearch
os.environ['OPENAI_API_KEY'] = settings.openai.key

elasticsearch_client = Elasticsearch(settings.elasticsearch.host, basic_auth=(settings.elasticsearch.name, settings.elasticsearch.password))



# from llama_index.llms import OpenAI
# from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext

# documents = SimpleDirectoryReader('data').load_data()

# index = VectorStoreIndex.from_documents(documents)
# # OpenAI.api_key = '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'
# query_engine = index.as_query_engine()
# response = query_engine.query("Which system does Hieu build?")

# print(response)

# llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=256)
# service_context = ServiceContext.from_defaults(llm=llm, chunk_size=800, chunk_overlap=20)
# index = VectorStoreIndex.from_documents(documents, service_context=service_context)
# query_engine = index.as_query_engine(streaming=True)
# response = query_engine.query("Which system does Hieu build?")
# response.print_response_stream()