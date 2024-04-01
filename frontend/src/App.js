import React from "react";
import axios from 'axios';
import Sidebar from './components/SideBar'; 
import ChatBubble from './components/ChatBubbles';  
import ChatInputBar from './components/ChatInputBar';  

class ChatInterface extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            messages: [],  
            userInput: "",  // Current user input
            step: 'greeting',  // Track the conversation step: 'greeting', 'clarifying', 'symptoms'
        }
    }

    componentDidMount() {
      console.log('Component did mount called');
      axios.get('http://127.0.0.1:5001/initial_greeting').then(response => {
        const greeting = response.data.greeting;
        this.setState({
          messages: [{ text: greeting, sender: 'bot' }],
          step: 'clarifying',
        });
      }).catch(error => {
        console.log(error);
      });
    }

    handleUserInput = (input) => {
        this.setState({ userInput: input });
    }

    fetchChatResponse = () => {
      const { userInput, step } = this.state;
      let endpoint = '';
    
      if (step === 'clarifying') {
        endpoint = 'http://127.0.0.1:5001/generate_clarifying_questions';
      } else if (step === 'symptoms') {
        endpoint = 'http://127.0.0.1:5001/list_relevant_symptoms';
      }
    
      axios.post(endpoint, { user_input: userInput }).then(response => {
        const newMessage = step === 'clarifying' ? response.data.question : response.data.symptoms;
        this.setState({
          messages: [...this.state.messages, {text: userInput, sender: 'user'}, {text: newMessage, sender: 'bot'}],
          userInput: "",
          step: step === 'clarifying' ? 'symptoms' : 'done',
        });
      }).catch(error => console.log(error));
    }

    render() {
        const { messages, userInput } = this.state;
        return (
            <div className="app-container">
                <Sidebar />
                <div className="chat-container">
                    <div className="chat-view">
                        {messages.map((message, index) => (
                            <ChatBubble key={index} text={message.text} isBot={message.sender !== 'user'} />
                        ))}
                    </div>
                    <ChatInputBar
  userInput={userInput}
  onChange={(e) => this.handleUserInput(e.target.value)} 
  onSubmit={this.fetchChatResponse}
/>
                                  </div>
            </div>
        );
    }
}

export default ChatInterface;

