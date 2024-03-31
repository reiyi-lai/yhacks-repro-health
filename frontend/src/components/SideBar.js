// import './sidebar.css';
import axios from "axios"
import React from 'react';

function Sidebar() {
  return (
    <div className="sidebar">
      <h2>Repro-Bot</h2>
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