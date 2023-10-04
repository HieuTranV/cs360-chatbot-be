from .config import elasticsearch_client
from llama_index.llms import OpenAI
from llama_index import ServiceContext, load_index_from_storage, StorageContext, Document, VectorStoreIndex
from llama_index.chat_engine.types import ChatMode, BaseChatEngine
import json

def getCustomerBasicInfo(customer_id: int):
  query = {
    'match': {
      'customer_id': customer_id
    }
  }

  resp = elasticsearch_client.search(index='customer-profile-basic-info', query=query)
  if len(resp['hits']['hits']) > 0:
    return resp['hits']['hits'][0]['_source']
  return None


def getVectorizedData(customer_id: int):
  query = {
    'match': {
      'customer_id': customer_id
    }
  }

  resp = elasticsearch_client.search(index='customer-vectorize-data', query=query)
  if len(resp['hits']['hits']) > 0:
    return json.loads(resp['hits']['hits'][0]['_source']['vector_data'])
  return None


def vectorizeCustomerData(customer_id: int):
  documents = []
  documents.append(Document(text="My basic information"))
  customer_data = getCustomerBasicInfo(customer_id)
  if customer_data is None:
    return None
  
  for key, value in customer_data.items():
    documents.append(Document(text='%s is %s'%(key, value)))
  
  llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=512)
  service_context = ServiceContext.from_defaults(llm=llm, chunk_size=800, chunk_overlap=20)
  index = VectorStoreIndex.from_documents(documents=documents, service_context=service_context)
  elasticsearch_client.index(
    index='customer-vectorize-data',
    document={
      'vector_data': json.dumps(index.storage_context.to_dict()),
      'customer_id': customer_id
    }
  )
  return index

def getChatEngine(customer_id: int) -> BaseChatEngine: 
  vectorizedData = getVectorizedData(customer_id=customer_id)
  if vectorizedData is not None:
    index = load_index_from_storage(StorageContext.from_dict(vectorizedData))
  else:
    index = vectorizeCustomerData(customer_id=customer_id)

  chat_engine = index.as_chat_engine(chat_mode=ChatMode.CONTEXT)
  return chat_engine