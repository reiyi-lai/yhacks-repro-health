import React from 'react';

const ChatBubbles = ({ text, isBot }) => {
  return (
    <div className={`chat-bubble ${isBot ? 'bot' : 'user'}`}>
      {text}
    </div>
  );
};

export default ChatBubbles;