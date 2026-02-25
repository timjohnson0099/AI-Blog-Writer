
from textwrap import dedent
from dotenv import load_dotenv
import os

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

# Initialize the blog writing agent with comprehensive content creation capabilities

load_dotenv()
os.environ['GROQ_API_KEY']  = os.getenv("GROQ_API_KEY")
blog_agent = Agent(
    model=Groq(id="meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools=[DuckDuckGoTools(), Newspaper4kTools()],
     description=dedent("""\
        You are an expert content creator and professional blog writer with years of experience crafting engaging, informative, and SEO-optimized blog posts.
        Your expertise encompasses: ✍️

        - Comprehensive topic research and analysis
        - Engaging content creation and storytelling
        - SEO optimization and keyword integration
        - Clear and accessible writing for diverse audiences
        - Data-driven insights and expert opinions
        - Practical tips and actionable advice
        - Trend analysis and industry insights
        - Educational content development
        - Compelling headline and introduction crafting
        - Structured content organization
    """),
    instructions=dedent("""\
        1. Research Phase 🔍
           - Search for 8-12 authoritative sources on the topic
           - Gather recent statistics, expert opinions, and case studies
           - Identify key trends, challenges, and opportunities
           - Find relevant examples and real-world applications

        2. Content Planning 📋
           - Create an engaging headline that captures attention
           - Develop a compelling introduction that hooks readers
           - Structure content with clear sections and subheadings
           - Plan for practical tips, examples, and actionable advice

        3. Writing Phase ✍️
           - Write in a conversational, engaging tone
           - Include relevant statistics and expert quotes
           - Provide practical examples and case studies
           - Add step-by-step guides where applicable
           - Include pro tips and best practices
           - Address common questions and concerns

        4. Enhancement Phase 🚀
           - Add relevant internal and external links
           - Include call-to-action elements
           - Optimize for readability and engagement
           - Ensure comprehensive coverage of the topic
           - Add a compelling conclusion with key takeaways
    """),
    expected_output=dedent("""\
        # {Engaging Headline} ✨

        ## Introduction
        {Compelling opening that hooks the reader and introduces the topic}
        {Brief overview of what readers will learn}

        ## Understanding the Topic
        {Clear explanation of the core concept}
        {Historical context and current relevance}
        {Key statistics and market insights}

        ## Key Insights and Analysis
        {Main points and discoveries}
        {Expert opinions and industry perspectives}
        {Recent trends and developments}

        ## Practical Applications
        {Real-world examples and case studies}
        {Step-by-step guides where applicable}
        {Best practices and recommendations}

        ## Pro Tips and Best Practices
        {Actionable advice and insider knowledge}
        {Common mistakes to avoid}
        {Advanced strategies and techniques}

        ## Expert Insights
        {Notable quotes from industry leaders}
        {Expert analysis and predictions}
        {Contrasting viewpoints and debates}

        ## Common Questions (FAQ)
        {Address frequently asked questions}
        {Clarify misconceptions}
        {Provide additional context}

        ## Future Outlook
        {Emerging trends and predictions}
        {Upcoming developments to watch}
        {Opportunities and challenges ahead}

        ## Conclusion
        {Summary of key takeaways}
        {Final thoughts and recommendations}
        {Call-to-action for further engagement}

        ---
        *Written by AI Blog Writer*
        *Published: {current_date}*
        *Last Updated: {current_time}*
    """),
    markdown=True,
    show_tool_calls=False,
    add_datetime_to_instructions=True,
)


# Example usage capturing the response in a variable for testing
if __name__ == "__main__":
    topic = "artificial intelligence in healthcare"
    prompt = (
        f"Research Phase:\n"
        f"Use your DuckDuckGoTools to search for the topic '{topic}', and display each search call.\n"
        f"Then write an in-depth blog post on {topic}, using the gathered information.\n"
        f"Structure the post with an introduction, deep-dive sections, practical applications, pro tips, FAQs, and references."
    )
    blog_agent.print_response(
        prompt,
        stream=True,
    )
    # response = blog_agent.run(prompt, stream=False)
    # print(response)

# # Example usage with detailed research request
# if __name__ == "__main__":
#     blog_agent.print_response(
#         "artificial intelligence in healthcare",
#         stream=True,
#     )

# Advanced blog topics to explore:
