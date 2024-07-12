from crewai import Task
from textwrap import dedent

class TVShowJokeCreatorTasks:
    def tv_show_research(self, agent, tv_show):
        return Task(description=dedent(f"""\
            Research the TV show "{tv_show}". Gather information about:
            1. The show's premise
            2. Main characters and their traits
            3. Setting and time period
            4. Recurring themes or plot devices
            5. Popular catchphrases or running gags
            6. Any other unique elements that could inspire jokes
        """),
        agent=agent
        )
    
    def joke_creation(self, agent, tv_show, joke_requirements):
        return Task(description=dedent(f"""\
            Create original jokes inspired by the TV show "{tv_show}" based on the research provided.
            Requirements: {joke_requirements}
            
            Guidelines:
            1. Create at least 5 jokes
            2. Ensure jokes are original and not copied from existing sources
            3. Reference character traits, plot elements, or themes from the show
            5. Make the jokes clever and appealing to fans of the show
        """),
        agent=agent
        )
    
    def joke_review_and_write(self, agent, tv_show):
        return Task(description=dedent(f"""\
            Review the jokes created for "{tv_show}" in the previous task and write them in a markdown file.

            Your tasks:
            1. Evaluate each joke from the previous 'joke_creation' task for quality, relevance to the show, and appropriateness
            2. Select the best jokes (at least 3, but no more than 10)
        """),
        agent=agent
        )