from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain_pydantic
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

from core.schemas import GetFlightInPeriodCheckInput
from core.constants import promptTemplate
from core.constants import requiredBookingDetails

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model="gpt-4")
memory = ConversationBufferMemory(
    memory_key="chat_history")
system_template = promptTemplate
system_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{input_data}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    MessagesPlaceholder(variable_name="chat_history"),
    human_prompt],
)

memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True,
    input_key="input_data",
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    # verbose=True
)

extraction_chain = create_tagging_chain_pydantic(GetFlightInPeriodCheckInput, llm)

user_flight_details = GetFlightInPeriodCheckInput(**requiredBookingDetails)
