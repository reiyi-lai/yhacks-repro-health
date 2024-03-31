import axios from "axios";
import React, { useState, useEffect } from 'react';
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';
import { fetchAPI } from './services/api';

function App() {
  const [data, setData] = useState('');
  const [loading, setLoading] = useState(false);


  useEffect(() => {
    const fetchData = async () => {
      if(loading){
        fetchAPI("poem").
          then(res => {
          setData(res);
          setLoading(false);
        });
      }

    };
    fetchData();
  }, [loading]);



  const handleSendMessage = (message) => {
    // Handle sending message logic here (e.g., sending message to chat server)
    console.log('Sending message:', message);
  };

  const handleLoading = () => {
    setLoading(true);
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
      <button onClick={handleLoading} style={{ marginLeft: '220px' }}> Click me to load a poem</button>
      <p style={{ marginLeft: '220px' }}>{data}</p>
    </div>
  );
}

export default App;
