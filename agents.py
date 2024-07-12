import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq
from tools.search_tools import SearchTools
from tools.write_files import WriteFiles

class TVShowJokeCreatorAgents:

    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )

    def tv_show_researcher_agent(self):
        return Agent(
            role="TV Show Researcher",
            goal=dedent("""\
                Research and gather information about a specific TV show, including its premise,
                main characters, setting, genre, and broad themes. You can also search for jokes that people have already made and use them for examples. You can find them from for example reddit, 9gag and many other platforms"""),
            backstory=dedent("""\
                You are an expert in TV show analysis, capable of quickly gathering and
                summarizing key information about any TV show."""),
            tools=[
                SearchTools.search_internet,
            ],
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )
    
    def tv_show_joke_creator_agent(self):
        return Agent(
            role="TV Show Joke Creator",
            goal=dedent("""\
                Create funny jokes inspired by the TV show information provided.
                The jokes should be clever, relevant to the show's themes, and appeal to fans."""),
            backstory=dedent("""\
                You are a witty comedy writer specializing in creating jokes inspired by
                TV shows. You excel at finding humor in a show's unique elements without
                directly copying its content."""),
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True
        )

    def joke_reviewer_and_writer_agent(self):
        return Agent(
            role="Joke Reviewer and Writer",
            goal=dedent("""\
                Review the jokes created for quality, relevance.
                Write approved jokes into a markdown file."""),
            backstory=dedent("""\
                You have a keen eye for humor and a talent for formatting. You ensure
                jokes are top-notch and present them in a clean, readable markdown format."""),
            tools=[
                WriteFiles.write_jokes_to_markdown_file
            ],
            llm=self.llm,
            verbose=True
        )
    
    def chief_creative_director_agent(self):
        return Agent(
            role="Chief Creative Director",
            goal=dedent("""\
                Oversee the entire joke creation process, ensuring high-quality output
                that's both funny and respectful of the source material. Provide guidance
                and feedback to the team as needed."""),
            backstory=dedent("""\
                You're a seasoned comedy producer with a deep understanding of TV shows
                and what makes audiences laugh. You guide your team to create the best
                possible TV show-inspired jokes."""),
            tools=[
                SearchTools.search_internet,
            ],
            llm=self.llm,
            verbose=True
        )