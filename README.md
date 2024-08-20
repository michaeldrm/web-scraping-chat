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
To set up the project, install the required packages using pip. First, create a `requirements.txt` file with the necessary dependencies, then run:

```bash
pip install -r requirements.txt
