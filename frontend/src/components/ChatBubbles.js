// ChatBubble.js
import React from 'react';

const ChatBubble = ({ text, isBot }) => {
  const bubbleClass = isBot ? "chat-bubble bot" : "chat-bubble user";
  return (
    <div className={bubbleClass}>
      {text}
    </div>
  );
};

export default ChatBubble;
