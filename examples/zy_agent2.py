from python_a2a import A2AClient, Message, TextContent, MessageRole
from python_a2a.utils import pretty_print_message

# Create a client connected to an A2A-compatible agent
client = A2AClient("http://localhost:5000/a2a")

# Create a simple message
message = Message(
    content=TextContent(text="Hello, A2A!"),
    role=MessageRole.USER
)

# Send the message and get a response
response = client.send_message(message)

# Display the response
pretty_print_message(response)