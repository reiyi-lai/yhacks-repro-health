// import logo from './logo.svg';
import './App.css';
import React from 'react';
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';

function App() {
  const handleSendMessage = (message) => {
    // Handle sending message logic here (e.g., sending message to chat server)
    console.log('Sending message:', message);
  };

  return (
    <div className="app-container">
      <Sidebar />
      <div className="chat-container">
        <div className="chat-view">
          <ChatBubble text="Hi! How are you feeling today?" isBot={true} />
          {/* Add more chat bubbles */}
        </div>
        <ChatInputBar onSubmit={handleSendMessage} /> {/* Add the ChatInputBar component */}
      </div>
    </div>
  );
}

export default App;
