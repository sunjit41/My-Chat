## Running with Docker

1. **Clone the repository and configure your API key:**
   ```bash
   git clone https://github.com
   cd My-Chat
   cp .env.example .env
   ```
   Open `.env` and add your free [Google AI Studio](https://google.com) API key.

2. **Build the Docker image:**
   ```bash
   docker build -t my-chat .
   ```

3. **Run the interactive AI assistant:**
   ```bash
   docker run -it --rm --env-file .env my-chat
   ```
