import React from 'react';
// import './sidebar.css';
import CompanyIcon from '..assets/ovary.png';

function Sidebar() {
  return (
    <div className="sidebar">
      <img src={CompanyIcon} alt="Company Icon"/>
      <h2>Chat App</h2>
      <ul>
        <li>New Chat</li>
        <li>Chat 1</li>
        <li>Chat 2</li>
        <li>Chat 3</li>
        {/* Add more list items for additional chats */}
      </ul>
    </div>
  );
}

export default Sidebar;