from agents import TVShowJokeCreatorAgents  # Updated class name
from tasks import TVShowJokeCreatorTasks    # Updated class name
from crewai import Crew, Process
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

agents = TVShowJokeCreatorAgents()
tasks = TVShowJokeCreatorTasks()

tv_show = "rantabaari"
joke_requirements = f"Clever jokes that reference the show's medical themes, character quirks, and catchphrases. Suitable for fans of {tv_show}."

tv_show_researcher = agents.tv_show_researcher_agent()
tv_show_joke_creator = agents.tv_show_joke_creator_agent()
joke_reviewer_and_writer = agents.joke_reviewer_and_writer_agent()
chief_creative_director = agents.chief_creative_director_agent()

research = tasks.tv_show_research(tv_show_researcher, tv_show)
joke_creation = tasks.joke_creation(tv_show_joke_creator, tv_show, joke_requirements)
review_and_write = tasks.joke_review_and_write(joke_reviewer_and_writer, tv_show)

tv_show_joke_crew = Crew(
    agents=[
        tv_show_researcher,
        tv_show_joke_creator,
        joke_reviewer_and_writer,
        chief_creative_director
    ],
    tasks=[
        research,
        joke_creation,
        review_and_write
    ],
    memory=True,
    verbose=True,
    process=Process.hierarchical,
    max_rpm=4,
    manager_llm=ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama3-70b-8192"
    ),
    manager_agent=chief_creative_director
)

jokes_result = tv_show_joke_crew.kickoff()

print("\n\n########################")
print("## Here are the TV show jokes:")
print(jokes_result)


file_name = f"{tv_show.lower().replace(' ', '_')}_jokes.md"
if os.path.exists(file_name):
    print(f"\nJokes have been written to {file_name}")
    with open(file_name, 'r') as f:
        print(f.read())
else:
    print(f"\nWarning: {file_name} was not created.")