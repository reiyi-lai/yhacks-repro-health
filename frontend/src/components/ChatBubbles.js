import React from 'react';
// import './Chat.css';

const ChatBubbles = ({ text, isBot }) => {
    return (
      <div className={`chat-bubble ${isBot ? 'bot' : 'user'}`}>
        {text}
      </div>
    );
  };
  
  export default ChatBubbles;