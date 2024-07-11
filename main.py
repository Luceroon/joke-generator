from agents import JokesCreatorAgents
from tasks import JokesCreatorTasks
from crewai import Crew
from dotenv import load_dotenv
load_dotenv()

agents = JokesCreatorAgents()
tasks = JokesCreatorTasks()

jokes_from = "House M.D"
jokes_details = f"Funny jokes that can only be understood by people who know {jokes_from}. Funny jokes are often satire and ironic."

joke_inspiration_agent = agents.joke_inspiration_agent()
creative_joke_creator_agent = agents.creative_joke_creator_agent()
joke_scriber_agent = agents.joke_scriber_agent()
chief_creative_director_agent = agents.chief_creative_diretor_agent()

inspiration = tasks.joke_analysis(joke_inspiration_agent, jokes_from, jokes_details)
creation = tasks.joke_creation(creative_joke_creator_agent, jokes_from, jokes_details)
scribing = tasks.joke_scribing(joke_inspiration_agent)
review = tasks.joke_review(chief_creative_director_agent, jokes_from, jokes_details)


copy_crew = Crew(
    agents=[
        joke_inspiration_agent,
        creative_joke_creator_agent,
        #joke_scriber_agent,
        chief_creative_director_agent
    ],
    tasks=[
        inspiration,
        creation,
        review,
        #scribing
    ],
    verbose=True,
    # Remove this when running locally. This helps prevent rate limiting with groq.
    max_rpm=4
)

jokes_copy = copy_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print(jokes_copy)
