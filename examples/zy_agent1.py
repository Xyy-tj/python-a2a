from python_a2a import A2AServer, Message, TextContent, MessageRole, run_server, OpenAIA2AServer
import logging
import dotenv
import os

# Load environment variables from .env file
dotenv.load_dotenv()
# Set up logging to print debug messages
logging.basicConfig(level=logging.DEBUG)


class EchoAgent(A2AServer):
    """A simple agent that echoes back messages with a prefix."""
    
    def handle_message(self, message):
        print("echoing back message with prefix")
        return Message(
            content=TextContent(text=f"Echo: {message.content.text}"),
            role=MessageRole.AGENT,
            parent_message_id=message.message_id,
            conversation_id=message.conversation_id
        )




# Run the server
if __name__ == "__main__":
    # agent = EchoAgent()

    agent = OpenAIA2AServer(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
    model="gpt-4o-mini",
    system_prompt="You are a helpful AI assistant specialized in explaining complex topics simply."
)

    run_server(agent, host="0.0.0.0", port=5000, debug=True)