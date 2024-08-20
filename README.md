# WebQueryBot

## Overview
WebQueryBot is an AI-driven application designed to scrape web content, process the text, and facilitate interactive conversations based on the extracted information. The project employs web scraping techniques to gather text from user-provided URLs, and leverages advanced NLP models to create a conversational agent capable of responding to queries about the content of the scraped web pages. The integration of tools such as BeautifulSoup, FAISS, and OpenAI's GPT-3.5-turbo ensures accurate and insightful interactions.

## Dataset
The dataset for this project consists of text data extracted from web pages based on user-provided URLs. The project does not use a traditional dataset but rather dynamically scrapes and processes content from the web as needed.

## Features
- **Scraping**: Utilizes BeautifulSoup for extracting text from web pages.
- **Text Processing**: Employs RecursiveCharacterTextSplitter for chunking text.
- **Vector Storage**: Uses FAISS for storing and retrieving text embeddings.
- **Conversational AI**: Integrates OpenAI’s GPT-3.5-turbo for generating conversational responses.

## Techniques Used
- **Web Scraping**: BeautifulSoup
- **Text Splitting**: RecursiveCharacterTextSplitter
- **Vector Storage**: FAISS
- **Conversational Model**: OpenAI GPT-3.5-turbo

## Installation
To set up and use WebQueryBot, follow these steps:

1. **Clone the repository** to your local machine:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required dependencies** by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Obtain an API key** from OpenAI and add it to the `.env` file in the project directory. Your `.env` file should contain:

    ```plaintext
    OPENAI_API_KEY=your_secret_api_key
    ```

## Usage
To use WebQueryBot, follow these steps:

1. **Ensure that you have installed the required dependencies** and added the OpenAI API key to the `.env` file.

2. **Run the application** using the Streamlit CLI. Execute the following command:

    ```bash
    streamlit run app.py
    ```

3. The application will launch in your default web browser, displaying the user interface.

4. **Input a URL** in the sidebar to scrape content from the desired web page.

5. **Ask questions** about the content of the scraped web pages using the chat interface.

## Author
Michael Diop
