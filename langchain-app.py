import os
#load dotenv to load environment variables from .env file
from dotenv import load_dotenv
#import the ChatOpenAI class from langchain_openai
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()


def main():
    # Check that required API keys are available
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set.")

    if not os.getenv("LANGSMITH_API_KEY"):
        raise ValueError("LANGSMITH_API_KEY is not set.")

    # Create the OpenAI chat model through LangChain
    model = ChatOpenAI(model="gpt-4o-mini",temperature=0)

    # Input prompt
    prompt = "Explain what a Business Analyst does in simple terms."

    # Send the prompt through LangChain
    response = model.invoke(prompt)

    # Print the response in the terminal
    print("\nModel Response:")
    print(response.content)

    # Get user input and send it through the same model
    user_prompt = input("Enter your prompt: ")
    response = model.invoke(user_prompt)
    print(response.content)


if __name__ == "__main__":
    main()
