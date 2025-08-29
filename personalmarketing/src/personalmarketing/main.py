#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from personalmarketing.crew import Personalmarketing

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew for LinkedIn job search marketing and research publications.
    """
    inputs = {
        "user_profession": "Senior AI/ML Engineer",
        "target_industries": "Technology, Healthcare, Finance, e-Commerce",
        "user_location": "United States (open to relocation)",
        "user_skills": "LLMs (GPT-4, Llama-3, BERT), RAG Systems, LangChain, LangGraph, MLOps, Apache Airflow, Chroma DB, QLoRA, RLHF, PyTorch, TensorFlow, AWS, GCP, Databricks, Kafka, Docker, Kubernetes, FastAPI, Gradio, Streamlit",
        "user_experience": "5+ years in AI/ML engineering with expertise in LLMs, RAG systems, and production deployment",
        "user_projects": "InboxAI: Intelligent Email Assistant using LLMs - Deployed LangGraph, OpenAI/Llama3 LLMs, and Gmail/Outlook APIs for seamless real-time email retrieval and dynamic reply generation. Orchestrated ML workflows with Apache Airflow, leveraging Chroma DB vector embeddings for rapid semantic search across email data. Health Bot: Healthcare Assistant using LLMs - Constructed a Bi-RNN, GloVe, BERT pipeline for NLP-driven disease diagnosis, boosting precision in healthcare conversational AI tasks. Enhanced response accuracy through LoRA and RLHF, enabling advanced semantic interaction and nuanced dialogue with healthcare users.",
        "research_interests": "Advanced LLM architectures, RAG systems optimization, MLOps and production deployment, Healthcare AI applications, Explainable AI, Multi-modal AI, Edge AI and real-time inference, Reinforcement learning systems",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }
    
    try:
        Personalmarketing().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "user_profession": "Senior AI/ML Engineer",
        "target_industries": "Technology, Healthcare, Finance, e-Commerce",
        "user_skills": "LLMs (GPT-4, Llama-3, BERT), RAG Systems, LangChain, LangGraph, MLOps, Apache Airflow, Chroma DB, QLoRA, RLHF, PyTorch, TensorFlow, AWS, GCP, Databricks, Kafka, Docker, Kubernetes, FastAPI, Gradio, Streamlit",
        "research_interests": "Advanced LLM architectures, RAG systems optimization, MLOps and production deployment, Healthcare AI applications, Explainable AI, Multi-modal AI, Edge AI and real-time inference, Reinforcement learning systems",
        'current_year': str(datetime.now().year)
    }
    try:
        Personalmarketing().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Personalmarketing().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "user_profession": "Senior AI/ML Engineer",
        "target_industries": "Technology, Healthcare, Finance, e-Commerce",
        "user_skills": "LLMs (GPT-4, Llama-3, BERT), RAG Systems, LangChain, LangGraph, MLOps, Apache Airflow, Chroma DB, QLoRA, RLHF, PyTorch, TensorFlow, AWS, GCP, Databricks, Kafka, Docker, Kubernetes, FastAPI, Gradio, Streamlit",
        "research_interests": "Advanced LLM architectures, RAG systems optimization, MLOps and production deployment, Healthcare AI applications, Explainable AI, Multi-modal AI, Edge AI and real-time inference, Reinforcement learning systems",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Personalmarketing().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
