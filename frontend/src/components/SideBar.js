// import './sidebar.css';
import axios from "axios"
import React, { useState, useEffect} from 'react';

function Sidebar() {

  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('/')
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);
  

  // function getPoem() {
  //   setLoading(true);
  //   axios({
  //     method: "GET",
  //     url: "/data",
  //   })
  //   .then((response) => {
  //     setPoem(response.data.poem); // Assuming response contains poem data
  //     setLoading(false);
  //   }).catch((error) => {
  //     setError(error.message);
  //     setLoading(false);
  //   });
  // }

  const sidebarStyle = {
    backgroundColor: '#f0f0f0',
    padding: '20px',
    borderRadius: '5px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    color: 'black'
  };
  return (
    <div className="sidebar">
      <h2>Chat App</h2>
      <ul>
        <li>New Chat</li>
        <li>Chat 1</li>
        <li>Chat 2</li>
        <li>{data && <p>{data.message}</p>}</li>
        
        <li>Chat 3</li>
        {/* Add more list items for additional chats */}
      </ul>
    </div>
  );
}

export default Sidebar;