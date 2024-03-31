// import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from "axios";
import Sidebar from './components/SideBar.js';
import ChatBubble from './components/ChatBubbles.js';
import ChatInputBar from './components/ChatInputBar.js';

function App() {
  const handleSendMessage = (message) => {
    // Handle sending message logic here (e.g., sending message to chat server)
    console.log('Sending message:', message);
  };

  const[data, setdata] = useState('');

  function getData(){
    axios({
      method: "GET",
      url:"/data",
    })
    .then((response) => {
      const res = response
      setdata(res)
    }).catch((error) => {
      if (error.response) {
        console.log("HEREEEE")
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
  

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
