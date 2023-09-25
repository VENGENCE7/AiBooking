"use client";
import React, { useEffect, useState } from "react";
import PageHeader from "./components/PageHeader";
import PromptBox from "./components/PromptBox";
import Title from "./components/Title";
import TwoColumnLayout from "./components/TwoColumnLayout";
import ResultWithSources from "./components/ResultWithSources";
import Table from "./components/Table";
import "./globals.css";

const Memory = () => {
  const [prompt, setPrompt] = useState("");
  const [error, setError] = useState(null);
  const [messages, setMessages] = useState([]);
  const [firstMsg, setFirstMsg] = useState(true);
  const [flightDetails, setFlightDetails] = useState(false);
  const [flights, setFlights] = useState([]);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const handlePromptChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleSubmitPrompt = async () => {
    try {
      // Update the user message
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: prompt, type: "user", sourceDocuments: null },
      ]);
      const response = await fetch("http://127.0.0.1:8000", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ input: prompt, firstMsg }),
      });

      if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
      }

      setPrompt("");
      // So we don't reinitialize the chain
      setFirstMsg(false);
      const searchRes = await response.json();
      if (searchRes.success) {
        setFlights(searchRes?.data);
        setFlightDetails(true);
      }
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: searchRes.response, type: "bot", sourceDocuments: null },
      ]);
      setError("");
    } catch (err) {
      console.error(err);
      setError(err);
    }
  };

  return (
    mounted && (
      <>
        <section>
          <Title headingText={"Memory"} emoji="🧠" />
          <TwoColumnLayout
            leftChildren={
              <div>
                <PageHeader
                  heading="Booked.ai - Flight Booking Assistant"
                  description="Your Personal Travel Assistant"
                />
                {flightDetails && <Table data={flights} />}
              </div>
            }
            rightChildren={
              <>
                <ResultWithSources messages={messages} pngFile="brain" />
                <PromptBox
                  prompt={prompt}
                  handleSubmit={handleSubmitPrompt}
                  error={error}
                  handlePromptChange={handlePromptChange}
                />
              </>
            }
          />
        </section>
      </>
    )
  );
};

export default Memory;
