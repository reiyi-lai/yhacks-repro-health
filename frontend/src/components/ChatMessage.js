import React from 'react';

function ChatMessage() {
    return (
        <div className="chat">
            <form className="input-form">
                <div className="input-container-column">
                    <input
                    className="them-input"
                    type="text"
                    placeholder="Type your love interest's message here..."
                    // value={themInputValue}
                    // onChange={handleThemInputChange}
                    />
                    <input
                    className="me-input"
                    type="text"
                    placeholder="Type your message here..."
                    // value={meInputValue}
                    // onChange={handleMeInputChange}
                    />
                </div>
                <button type="submit" className="submit-btn">➤</button>
            </form>
            </div>
    )
}

export default ChatMessage;