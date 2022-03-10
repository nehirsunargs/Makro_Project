from typing import Optional
from uuid import uuid4
import time
from fastapi import FastAPI, Path, Header, HTTPException
from pydantic import BaseModel    

app = FastAPI()


class User(BaseModel):
    id: str
    session: str

class ChatData(BaseModel):
    user1: str
    user2: str
    chat_id: int

class MessageData(BaseModel):
    chat_id: int
    sender: str
    message: str
    message_id : int
    send_time: int
    
class MessageRequestData(BaseModel):
    message: str

users = {"nehir": User(id="nehir",session="123"),"aybars": User(id="aybars",session="123"),"altan": User(id="altan",session="123")}

chats = {
    1: {
        "chat_data": ChatData(user1="nehir", user2="altan", chat_id=1),
        "messages": []
    }
}

def check_if_user_in_chat(user_id, chat_data: ChatData):
    return chat_data.user1 == user_id or chat_data.user2 == user_id

def verify_user(user_id, user_session):
    user = users.get(user_id)
    if user:
        if user.session == user_session:
            return user
    return None

@app.get("/chat/{chat_id}/messages")
def get_chat(chat_id: int = Path(None),user_id: Optional[str] = Header(None),user_session: Optional[str] = Header(None)):
    user = verify_user(user_id, user_session)
    if not user:
        raise HTTPException(status_code=403, detail={"error":{"msg": "no id or session"}})
    if chat_id not in chats:
        raise HTTPException(status_code=500, detail={"error":{"status": "NO_CHAT"}})
    chat_info = chats[chat_id]
    if not check_if_user_in_chat(user_id,chat_info["chat_data"]):
        raise HTTPException(status_code=500, detail={"error":{"status": "NO_CHAT"}})
    return chats[chat_id]

@app.post("/chat/{chat_id}/messages")
def post_chat(chat_id: int, message: MessageRequestData,user_id: Optional[str] = Header(None),user_session: Optional[str] = Header(None)):
    user = verify_user(user_id, user_session)
    if not user:
        raise HTTPException(status_code=403, detail={"error":{"msg": "no id or session"}})
    if chat_id not in chats:
        raise HTTPException(status_code=500, detail={"error":{"status": "NO_CHAT"}})
    chat_info = chats[chat_id]
    if not check_if_user_in_chat(user_id,chat_info["chat_data"]):
        raise HTTPException(status_code=500, detail={"error":{"status": "NO_CHAT"}})

    id = uuid4()
    current_time  = time.time()
    message_data = MessageData(message=message.message,sender=user_id,chat_id=chat_id,message_id=id,send_time=current_time)
    print(message_data)
    chat_info["messages"].append(message_data)
    return chats[chat_id]