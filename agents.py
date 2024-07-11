import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.write_files import WriteFiles

class JokesCreatorAgents:

    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )

    def joke_inspiration_agent(self):
        return Agent(
            role="Lead joke inspiration finder",
            goal=dedent("""\
                Find amazing and funny jokes and quotes. After that conduct amazing analysis of the jokes found from the internet for example reddit, providing in-depth insights to guide creating new jokes"""),
            backstory=dedent("""\
				As the lead joke inspiration finder, you specialize in finding examples of funny jokes that others can use when creating their own jokes."""),
            tools=[
                SearchTools.search_internet,
                #SearchTools.search_reddit
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    
    def creative_joke_creator_agent(self):
        return Agent(
            role="Creative Joke Creator",
            goal=dedent("""\
				Develop funny, ironic and satire jokes that match the audience and needs intellect to understand them. Use Lead Joke Inspiration finder for inspiration about the jokes."""),
            backstory=dedent("""\
				As a Creative Joke Creator at a top-tier joke platform, you excel in crafting jokes that makes the target audience laugh."""),
            tools=[
                SearchTools.search_internet,
                #SearchTools.search_reddit,
            ],
            llm=self.llm,
            verbose=True
        )

    def joke_scriber_agent(self):
        return Agent(
            role="Joke Scriber",
            goal=dedent("""\
                Write down the jokes created by Creative Joke Creator."""),
            backstory=dedent("""\
                You are the best and fastest scriber."""),
            tools=[
                WriteFiles.write_jokes_to_file
            ],
            llm=self.llm,
            verbose=True
        )
    
    def chief_creative_diretor_agent(self):
        return Agent(
            role="Chief Creative Director",
            goal=dedent("""\
					Oversee the work done by your team to make sure it's the best
					possible and make sure that the jokes land on the audience,
					ask clarifying question or delegate follow up work if necessary to make
					decisions. But don't be too picky so everything will be much faster"""),
            backstory=dedent("""\
					You're the Chief Content Officer of jokes creation specialized in product jokes and what makes people laugh. You're working on a new
					audience, trying to make sure your team is crafting the best possible
					content for the audience"""),
            tools=[
                SearchTools.search_internet,
                #SearchTools.search_reddit
            ],
            llm=self.llm,
            verbose=True
        )