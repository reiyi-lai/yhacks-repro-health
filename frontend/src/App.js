// import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';

const ChatApp = () => {
  const [messages, setMessages] = useState([]);

  const handleNewMessage = (message) => {
    // Add the new message to the messages array
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
