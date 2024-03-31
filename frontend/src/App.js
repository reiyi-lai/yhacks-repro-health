import axios from "axios";
import React, { useState } from 'react';
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';
import { fetchAPI } from './services/api';

function ChatApp() {
  const [messages, setMessages] = useState([]);

  const handleNewMessage = (message) => {
    // Handle sending message logic here (e.g., sending message to chat server)
    setMessages([...messages, { text: message, isBot: false }]);
  };

  return (
    <div className="app-container">
      <Sidebar />
      <div className="chat-container">
        <div className="chat-view">
          <ChatBubble text="Hi! How are you feeling today?" isBot={true} />
          {messages.map((message, index) => (
          <ChatBubble key={index} text={message.text} isBot={message.isBot} />
        ))}
        </div>
        <ChatInputBar onSubmit={handleNewMessage} /> 
      </div>
    </div>
  );
}

export default ChatApp;
