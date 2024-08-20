import streamlit as st 
import requests 
from bs4 import BeautifulSoup
from htmlressources import css, user_template, bot_template
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.memory import ConversationBufferMemory 
from langchain.chains import ConversationalRetrievalChain


# Todo : scrape with selenium later 
def get_website_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  #check requests
        
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Split the parsed text to chunks for embedding
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectors_stored(chunks):
    embedding_model = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embedding_model)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def chat(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)



def main():

    load_dotenv()

    st.set_page_config(page_title="Chat with Web Scraping AI Bot")
    st.markdown(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Chat with Web Scraping AI Bot")
    user_question = st.text_input("Ask a question about the URL content sent")
    if user_question and st.session_state.conversation:
        chat(user_question)
    elif user_question and not st.session_state.conversation:
        st.warning("Please process a URL first before asking a question.")

    with st.sidebar:
        st.subheader("List of website pages URL to scrape :")
        ## Todo : make a button for several URL 
        ## Todo : create an COMPLETE AUTOSCRAP CMD
        url = st.text_input("URL")
        if st.button("Process") :
            with st.spinner("Processing"):
                # scrape website
                raw_text = get_website_text(url)
                chunks = get_text_chunks(raw_text)

                vectorstore = get_vectors_stored(chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("URL processed successfully. You can now ask questions.")

if __name__ == "__main__":
    main()