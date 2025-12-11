import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatWindowRef = useRef(null);

  useEffect(() => {
    const initialMessage =
      "Hiya! 🌟 I'm NitikaNexus 🤖, your go-to AI for all things Nitika! Whether you're curious about her work, her favorite Netflix shows, or just want to know what's she's up to when she's not coding away—ask away! Let's get started! 🚀";
    setMessages([{ bot: initialMessage }]);
  }, []);

  const formatText = (text) => {
    const formattedText = text.replace(/\*(.*?)\*/g, "<strong>$1</strong>");
    return formattedText.replace(/\n/g, "<br />");
  };

  const sendMessage = async () => {
    if (input.trim() === "") return;

    const response = await fetch("https://nitikanexus.onrender.com/ask", {  // ✅ FIXED
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
    if (chatWindowRef.current) {
      chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="App">
      <h1>
        NitikaNexus <span style={{ WebkitTextFillColor: 'initial' }}>🤖</span>  {/* ✅ FIXED */}
      </h1>
      {/* Rest of your JSX... */}
    </div>
  );
}

export default App;
