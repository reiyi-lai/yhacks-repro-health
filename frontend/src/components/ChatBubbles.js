import React from 'react';

const ChatBubbles = ({ messages }) => {
  return (
    <div>
      {messages.map((message, index) => (
        <div className={`chat-bubble ${isBot ? 'bot' : 'user'}`}>
          {message.text}
        </div>
      ))}
    </div>
  );
};

export default ChatBubbles;