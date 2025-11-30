#!/usr/bin/env python
import sys
import warnings
import dotenv
from crew import SqlAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
dotenv.load_dotenv()

def run():
    """
    Run the crew.
    """
    inputs = {
        'user_query': "Just give me no of candidates who have cgpa greater than 8.8 in the candidates table.",
    }

    try:
        SqlAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()