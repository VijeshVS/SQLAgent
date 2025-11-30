import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.mcp import MCPServerHTTP
import dotenv

dotenv.load_dotenv()

@CrewBase
class SqlAgent():
    """SqlAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @agent
    def sql_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['sql_expert'],
            verbose=True,
            mcps=[
                MCPServerHTTP(
                    url=f"https://mcp.supabase.com/mcp?project_ref={os.getenv('PROJECT_REF')}&read_only=true",
                    headers = {
                        "Authorization": f"Bearer {os.getenv('SUPABASE_AUTH_TOKEN')}"
                    },
                    streamable=True,
                    cache_tools_list=True,
                )
            ]
        )
    
    @task
    def sql_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['sql_query_task'],
            output_file="output.txt"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SqlAgent crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
