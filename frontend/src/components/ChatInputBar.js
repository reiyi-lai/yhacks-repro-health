import React from 'react';
import sendicon from './assets/send-icon.png'; 

const ChatInputBar = ({ userInput, onChange, onSubmit }) => {

  return (
    <form className="chat-input-bar" onSubmit={(event) => {
      event.preventDefault();
      onSubmit();
    }}>
      <input
        type="text"
        placeholder="Type your message..."
        value={userInput}
        onChange={onChange}
      />
      <button type="submit">
        <img src={sendicon} alt='Send'/>
      </button>
    </form>
  );
};
export default ChatInputBar;