// ChatInputBar.js
import React, { useState } from 'react';
import sendicon from './assets/send-icon.png'

const ChatInputBar = ({ onSubmit }) => {
  const [message, setMessage] = useState('');

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (message.trim() !== '') {
      onSubmit(message); // Call the onSubmit function with the message
      setMessage(''); // Clear the input field after submission
    }
  };

  return (
    <form className="chat-input-bar" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={handleChange}
      />
      <button type="submit">
        <img src={sendicon} alt='send'/>
      </button>
    </form>
  );
};

export default ChatInputBar;