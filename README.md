# Nexus AI Chatbot

Nexus AI is a lightweight, locally hosted conversational AI assistant designed to run efficiently on low-resource devices. It leverages Ollama and Gemma 2B, enabling intelligent conversations even on small machines with limited RAM. Nexus AI provides a smooth, real-time chat experience and supports voice input, making it a flexible assistant for everyday tasks.

## Features

- **Lightweight & Local**: Runs entirely on-device with minimal RAM usage, perfect for small laptops or embedded systems.  
- **Powered by Ollama & Gemma 2B**: A compact language model that provides rich conversational AI without requiring cloud-based services.  
- **Voice Input**: Integrated voice recognition allows users to speak their queries, making the interaction natural and hands-free.  
- **Chat History**: Maintains conversation history within the session, so you can see past questions and answers.  
- **On-Device Learning**: While lightweight, the model can handle a variety of queries and improves over time with usage.  
- **Clean UI**: Built using Streamlit, offering a simple, responsive interface.

## Technologies Used

- **Python**: The core programming language.  
- **Streamlit**: For building the web interface.  
- **Ollama**: Local model hosting and execution.  
- **Gemma 2B**: A compact LLM for efficient inference.  
- **SpeechRecognition**: For capturing voice input from the user.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kumar4rpit/nexus-ai-chatbot.git
2. Navigate into the project directory:

cd nexus-ai-chatbot

3. Install the dependencies:

pip install -r requirements.txt

4. Run the application:

streamlit run app.py
Project Structure
app.py: Main application logic (handles the chat interface and AI interaction).
requirements.txt: Lists all necessary Python packages.
README.md: Project documentation.
Future Enhancements
Voice Output: Enable the AI to speak responses back to the user.
Document Interaction: Upload and ask questions about PDFs.
Web Search Integration: Combine AI answers with real-time web search for enhanced information.
Author

Developed by Kumar Arpit
Created as a hackathon project using Ollama, Streamlit, and Python.

License

This project is open-source under the MIT License.
