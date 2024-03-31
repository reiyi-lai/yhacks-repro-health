// import logo from './logo.svg';
import './App.css';
import React from 'react';
import Sidebar from './components/SideBar.js';
import Chatbubbles from './components/ChatBubbles.js';
import Chatinputbar from './components/ChatInputBar.js';

function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="chat-container">
        <div className="chat-view">
          <Chatinputbar text="Hello! How can I assist you?" isBot={true} />
          <Chatinputbar text="Hi! I have a question about..." isBot={false} />
          {/* Add more chat bubbles */}
        </div>
        <ChatInputBar onSubmit={handleSendMessage} /> {/* Add the ChatInputBar component */}
      </div>
    </div>
  );
}

export default App;
