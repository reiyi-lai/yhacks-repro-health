import axios from "axios";
import React, { useState, useEffect } from 'react';
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';

function App() {
  const [data, setData] = useState('');

  useEffect(() => {
    axios.get('/')
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

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
      {data && <p>{data}</p>}
    </div>
  );
}

export default App;
