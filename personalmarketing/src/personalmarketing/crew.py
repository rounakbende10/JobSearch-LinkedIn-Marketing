from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool,FileWriterTool, FileReadTool, DirectoryReadTool, ScrapeWebsiteTool
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from personalmarketing.tools.custom_tool import LinkedInPostAnalyzer, ResearchTopicAnalyzer, ResumeOptimizer, InnovationTracker

_=load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class Content(BaseModel):
    content_type: str = Field(...,
                              description="The type of content to be created (e.g., LinkedIn post, research blog, thought leadership article)")
    topic: str = Field(..., description="The topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself")


@CrewBase
class Personalmarketing():
    """LinkedIn Job Search and Research Publication Marketing crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def linkedin_strategy_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['linkedin_strategy_specialist'], # type: ignore[index]
            tools=[SerperDevTool(),FileWriterTool(), FileReadTool(), DirectoryReadTool('resources/drafts'), ScrapeWebsiteTool(), LinkedInPostAnalyzer(), ResumeOptimizer(), InnovationTracker()],
            max_rpm=3,
            reasoning=True,
            inject_date=True,
            allow_delegation=True,
            verbose=True
        )

    @agent
    def content_creator_linkedin(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_linkedin'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('resources/drafts'), ScrapeWebsiteTool(), LinkedInPostAnalyzer(), InnovationTracker()],
            inject_date=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=30,
            verbose=True
        )

    @agent
    def research_blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['research_blog_writer'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('resources/drafts'), ScrapeWebsiteTool(), ResearchTopicAnalyzer(), InnovationTracker()],
            max_rpm=3,
            max_iter=5,
            allow_delegation=True,
            inject_date=True,
            verbose=True
        )

    @agent
    def seo_research_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_research_specialist'], # type: ignore[index]
            tools=[FileWriterTool(), FileReadTool(), DirectoryReadTool('resources/drafts'), ScrapeWebsiteTool(), LinkedInPostAnalyzer(), ResearchTopicAnalyzer(), InnovationTracker()],
            verbose=True,
            allow_delegation=True,
            max_rpm=3,
            max_iter=3,
            reasoning=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def linkedin_market_research(self) -> Task:
        return Task(
            config=self.tasks_config['linkedin_market_research'], # type: ignore[index]
            agent=self.linkedin_strategy_specialist()
        )

    @task
    def develop_linkedin_strategy(self) -> Task:
        return Task(
            config=self.tasks_config['develop_linkedin_strategy'], # type: ignore[index]
            agent=self.linkedin_strategy_specialist()
        )

    @task
    def create_linkedin_content_calendar(self) -> Task:
        return Task(
            config=self.tasks_config['create_linkedin_content_calendar'], # type: ignore[index]
            agent=self.content_creator_linkedin()
        )

    @task
    def prepare_linkedin_posts(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_linkedin_posts'], # type: ignore[index]
            agent=self.content_creator_linkedin(),
            output_file='linkedin_posts.md'
        )

    @task
    def research_topic_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['research_topic_analysis'], # type: ignore[index]
            agent=self.seo_research_specialist()
        )

    @task
    def draft_research_blogs(self) -> Task:
        return Task(
            config=self.tasks_config['draft_research_blogs'], # type: ignore[index]
            agent=self.research_blog_writer(),
            output_file='research_blogs.md'
        )

    @task
    def optimize_professional_content(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_professional_content'], # type: ignore[index]
            agent=self.seo_research_specialist(),
            output_file='optimized_content.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LinkedIn Job Search and Research Publication Marketing crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
