import React from 'react';
// import './index.css'; // Import your CSS file for styling

function Sidebar() {
  return (
    <div className="sidebar">
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