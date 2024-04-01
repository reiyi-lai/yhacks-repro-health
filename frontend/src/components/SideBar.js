// import './sidebar.css';
import axios from "axios"
import React from 'react';
import logo from './assets/ovary-logo.png'

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="logo-title-container">
        <img src={logo} alt='logo'/>
        <h1>Repro-Bot</h1>
      </div>
      <ul>
        <li>New Chat</li>
        <li className="inactive-chat">Chat 1</li>
        <li className="inactive-chat">Chat 2</li>    
        <li className="inactive-chat">Chat 3</li>
        {/* Add more list items for additional chats */}
      </ul>
    </div>
  );
}

export default Sidebar;