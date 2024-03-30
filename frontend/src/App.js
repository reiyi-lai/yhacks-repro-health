import { ChatContextProvider } from './context/chatContext';
import SideBar from './components/SideBar';
import ChatView from './components/ChatView';
import { React, useEffect, useState } from 'react';
import Modal from './components/Modal';
import Setting from './components/Setting';

import Navigation from "./components/Navigation/Navigation.jsx";
import Chat from "./components/Chat/Chat.jsx";
import Feedback from "./components/Feedback/Feedback.jsx";
import "./App.css";

const App = () => {
  const [modalOpen, setModalOpen] = useState(false);

  useEffect(() => {
    const apiKey = window.localStorage.getItem('api-key');
    if (!apiKey) {
      setModalOpen(true);
    }
  }, []);
  return (
    <ChatContextProvider>
      <Modal title="Setting" modalOpen={modalOpen} setModalOpen={setModalOpen}>
        <Setting modalOpen={modalOpen} setModalOpen={setModalOpen} />
      </Modal>
      <div className="flex transition duration-500 ease-in-out">
        <SideBar />
        <ChatView />
      </div>
    </ChatContextProvider>
  );
};

export default App;