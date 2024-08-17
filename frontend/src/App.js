import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatWindowRef = useRef(null);

  // Add bot's initial message on component mount
  useEffect(() => {
    const initialMessage =
      "Hiya! 🌟 I’m NitikaNexus 🤖, your go-to AI for all things Nitika! Whether you're curious about her work, her favorite Netflix shows, or just want to know what she’s up to when she’s not coding away—ask away! Let’s get started! 🚀";
    setMessages([{ bot: initialMessage }]);
  }, []);

  const formatText = (text) => {
    // Replace *text* with <strong>text</strong> for bold text
    const formattedText = text.replace(/\*(.*?)\*/g, "<strong>$1</strong>");
    // Replace newline characters with <br /> for proper line breaks
    return formattedText.replace(/\n/g, "<br />");
  };

  const sendMessage = async () => {
    if (input.trim() === "") return;

    const response = await fetch("http://localhost:5001/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: input }),
    });
    const data = await response.json();
    const formattedBotResponse = formatText(data.answer);
    setMessages([...messages, { user: input, bot: formattedBotResponse }]);
    setInput("");
  };

  useEffect(() => {
    // Scroll to the bottom when messages change
    if (chatWindowRef.current) {
      chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="App">
      <img src="/Users/nitikaborkar/SAP-Project/frontend/src/wave.svg" alt="Wave" class="wave-overlay"></img>
       <h1>NitikaNexus <span style={{ WebkitTextFillColor: 'initial' }}>🤖</span></h1>
      <div className="chat-window" ref={chatWindowRef}>
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`message-container ${
              msg.user ? "user-message-container" : "bot-message-container"
            }`}
          >
            {msg.user && (
              <p className="user-message">
                <strong>You:</strong> {msg.user}
              </p>
            )}
            {msg.bot && (
              <p
                className="bot-message"
                dangerouslySetInnerHTML={{ __html: `<strong>NitikaNexus:</strong> ${msg.bot}` }}
              />
            )}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>
          <div className="svg-wrapper-1">
            <div className="svg-wrapper">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                width="24"
                height="24"
              >
                <path fill="none" d="M0 0h24v24H0z"></path>
                <path
                  fill="currentColor"
                  d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                ></path>
              </svg>
            </div>
          </div>
          <span>Send</span>
        </button>
      </div>
    </div>
  );
}

export default App;
