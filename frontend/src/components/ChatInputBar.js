import React, { useState } from 'react';
// import './ChatInputBar.css';

const ChatInputBar = ({ onSubmit }) => {
  const [message, setMessage] = useState('');

  const handleChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (message.trim() !== '') {
      onSubmit(message);
      setMessage('');
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
      <button type="submit">Send</button>
    </form>
  );
};

export default ChatInputBar;