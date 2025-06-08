#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from news_poetry.crew import NewsPoetry

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("Running the NewsPoetry crew...")
    inputs = {
        'topic': 'Newest developments in the Sudanese civil war',
        'current_year': str(datetime.now().year)
    }
    
    try:
        NewsPoetry().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    print("Training the NewsPoetry crew...")
    inputs = {
        "topic": "Newest developments in the Sudanese civil war",
        'current_year': str(datetime.now().year)
    }
    try:
        NewsPoetry().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    print("Replaying the NewsPoetry crew...")
    try:
        NewsPoetry().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    print("Testing the NewsPoetry crew...")
    inputs = {
        "topic": "Newest developments in the Sudanese civil war",
        "current_year": str(datetime.now().year)
    }
    
    try:
        NewsPoetry().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
