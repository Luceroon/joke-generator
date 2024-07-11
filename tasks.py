from crewai import Task
from textwrap import dedent

class JokesCreatorTasks:
    def joke_analysis(self, agent, jokes_from, jokes_details):
        return Task(description=dedent(f"""\
            Find and analyze the jokes from media {jokes_from} using the details: {jokes_details}.
            Look for patterns, common themes, and humor techniques. 
            Get examples from reddit and all over the internet from people who have made jokes about the media that we are analysing. It's currenlty 2024. Find atleast 30 good sources then you can move on to another task.
        """),
        agent=agent
        )
    
    def joke_creation(self, agent, jokes_from, jokes_details):
        return Task(description=dedent(f"""\
            Create new jokes based on the inspiration and details provided: {jokes_details}.
            Ensure the jokes are fresh, humorous, and relevant to the target audience.
        """),
        agent=agent
        )
    
    def joke_scribing(self, agent):
        return Task(description=dedent("""\
            Write down the jokes made in joke_creation
        """),
        agent=agent
        )
    
    def joke_review(self, agent, jokes_from, jokes_details):
        return Task(description=dedent(f"""\
            Review the jokes created by Creative Joke Creator and make sure that the jokes are the best possible. 
            Ask clarifying questions or delegate follow-up work if necessary to make decisions. 
            When delegating work, send the full draft as part of the information.
        """),
        agent=agent
        )