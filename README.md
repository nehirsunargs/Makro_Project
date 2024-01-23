# FastAPI Chat Application

## Description

This FastAPI Chat Application is a simple server that allows users to interact with each other through chat messages. It provides API endpoints to retrieve and post messages in chat rooms. The application is built using the FastAPI framework and uses Pydantic for data validation.

## Features

- **Get Chat Messages:** Retrieve chat messages for a specific chat room.
- **Post Chat Messages:** Post new chat messages to a chat room.
- **User Verification:** Verify users based on their ID and session.
- **Data Models:** Utilizes data models for users, chat data, and messages.
- **Error Handling:** Handles errors and exceptions gracefully.

## Technologies Used

- **FastAPI:** Used for building the web API.
- **Pydantic:** Used for data validation and modeling.
- **uuid4:** Used for generating unique message IDs.
- **time:** Used for recording message timestamps.

## API Endpoints

- **GET /chat/{chat_id}/messages:** Retrieve chat messages for a specific chat room.

- **POST /chat/{chat_id}/messages:** Post new chat messages to a chat room.

## Author

- Nehir Sunar
