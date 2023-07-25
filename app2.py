import streamlit as st
from langchain.llms import LlamaCpp
from langchain import PromptTemplate
from langchain.chains import LLMChain

def generate_response(input_text):
    llm = LlamaCpp(model_path = "./model/llama-2-7b.ggmlv3.q4_K_S.bin")
    prompt_template = """You are an helpful AI bot that generates accurate responses at whatever the user says
  QUESTION: {question}
  """

    prompt = PromptTemplate(template=prompt_template, input_variables=["question"])
    query_llm = LLMChain(llm=llm, prompt=prompt)
    response = query_llm.run({"question": str(input_text)})
    #response =   response['choices'][0]['text']    
    st.info(response)
    
st.markdown(" LLAMA LOCAL")
st.sidebar.markdown(" LLAMA LOCAL")

with st.form('my_form'):
    text = st.text_area('Prompt:', '',
        placeholder='welcome to the age of ai') 
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
