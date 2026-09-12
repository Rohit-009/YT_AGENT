from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.youtube import YouTubeTools
import os
from agno.models.groq import Groq
load_dotenv()

def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(
                    id="openai/gpt-oss-20b",
                    api_key=os.getenv("GROQ_API_KEY"),
                ),
        tools=[YouTubeTools()],
        instructions=[
            "Analyze the provided YouTube video.",
            "Summarize the main points clearly.",
            "Extract important topics and key takeaways.",
            "Use simple and understandable English.",
        ],
        add_datetime_to_context=True,
        markdown=True,
    )

# youtube_agent.print_response(
#     "Analyze this video: https://www.youtube.com/watch?v=JkaxUblCGz0",
#     stream=True,
# )