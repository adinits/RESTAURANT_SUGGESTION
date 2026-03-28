import restaurant_ai.secret_key_example as secret_key_example
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from langchain.chains import LLMChain              
from langchain.chains.sequential import SequentialChain 

api_key = secret_key_example.key_groq

llm = ChatGroq(                       
    temperature=0.6,
    groq_api_key=api_key,
    model_name="groq/compound-mini"  
)

def restaurant_name_suggestor(cuisine):

    # Chain 1: Name of the Restaurant
    name_prompt_template = PromptTemplate(
        input_variables=['cuisine'],
        template="I want name suggestion to open a {cuisine} food. Suggest a interesting and attractive name."
    )

    name_chain = LLMChain(
        llm=llm,
        prompt=name_prompt_template,
        output_key="resturant_name"
    )

    # Chain 2: Items for the menu
    item_prompt_template = PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest a list of 20 menu items sorted lexicographically for the resturant {resturant_name}. Give as comma separated string"
    )

    items_chain = LLMChain(
        llm=llm,
        prompt=item_prompt_template,
        output_key="item_list"
    )

    final_chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=['cuisine'],
        output_variables=['resturant_name', 'item_list']
    )

    response = final_chain.invoke({'cuisine': cuisine})
    return response
