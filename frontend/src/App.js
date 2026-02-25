import React, { useState, useRef } from "react";
import styles from "./App.module.css";
import "./fonts.css";
import BlogMarkdown from "./BlogMarkdown";

const AGENT_STEPS = [
  "Crafting a title that's sure to grab attention.",
  "Researching and outlining the main sections.",
  "Writing detailed content and tips.",
  "Finalizing, formatting, and adding references."
];

function App() {
  const [page, setPage] = useState("input");
  const [topic, setTopic] = useState("");
  const [blog, setBlog] = useState("");
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);
  const [error, setError] = useState("");
  const abortRef = useRef(null);

  const handleGenerate = async () => {
    setPage("loading");
    setBlog("");
    setLoading(true);
    setStep(0);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/generate-blog", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic }),
      });

      if (!response.body) {
        setError("No response from server.");
        setLoading(false);
        return;
      }

      const reader = response.body.getReader();
      let text = "";
      let done = false;
      let chunkCount = 0;

      const totalSteps = AGENT_STEPS.length;
      while (!done) {
        const { value, done: doneReading } = await reader.read();
        done = doneReading;
        if (value) {
          const chunk = new TextDecoder().decode(value);
          text += chunk;
          setBlog(text);

          // Update agent step and progress
          if (chunkCount < totalSteps && text.length > (chunkCount + 1) * 600) {
            setStep(chunkCount + 1);
            chunkCount++;
          }
        }
      }
      setLoading(false);
      setPage("result");
    } catch (e) {
      setError("Failed to generate blog post.");
      setLoading(false);
      setPage("input");
    }
  };

  return (
    <>
      <div className={styles.bgGlow}>
        <div className={styles.glow + ' ' + styles.glow1}></div>
        <div className={styles.glow + ' ' + styles.glow2}></div>
        <div className={styles.glow + ' ' + styles.glow3}></div>
      </div>
      <div className={styles.container}>
      {page === "input" && (
        <>
          <div className={styles.inputSection} style={{ textAlign: "center", maxWidth: "100%", margin: "0 auto" }}>
            <div className={styles.title} style={{fontSize: "4.5rem", textAlign: "center", maxWidth: "60%", margin: "0 auto", display: "flex", justifyContent: "center", alignItems: "center" }}>
              <span>Use <span className={styles.highlight}>AI Blog Writer</span> to Write Blog in <span className={styles.highlight}>One Click</span></span>
            </div>
            
            <div className={styles.inputRow} style={{ justifyContent: "center" }}>
              <input
                className={styles.inputBox}
                type="text"
                value={topic}
                onChange={e => setTopic(e.target.value)}
                placeholder="Enter Your Blog Title"
                autoFocus
              />
              <button
                className={styles.button}
                onClick={handleGenerate}
                disabled={!topic.trim() || loading}
              >
                Generate Blog
              </button>
            </div>
            {error && <div style={{ color: "#ff6b6b", marginTop: 16, textAlign: "center" }}>{error}</div>}
          </div>
        </>
      )}
      {page === "loading" && (
        <div className={styles.loadingCard}>
          <div className={styles.loadingEmoji}>⏳</div>
          <div className={styles.loadingProgress}>{Math.round((step / AGENT_STEPS.length) * 100)}% Completed</div>
          <div className={styles.loadingTitle}>Magic in progress...</div>
          <div className={styles.loadingStep}><span className={styles.loadingStepIcon}>⚠️</span>Working on it! {AGENT_STEPS[step] || "Almost done..."}</div>
        </div>
      )}
      {page === "result" && (
        <>
          {/* <div className={styles.title} style={{ fontSize: "1.5rem", marginBottom: 0,marginBottom: 0,marginTop: 20, color: "#222" }}>Your AI-Generated Blog Post</div> */}
          <div className = {styles.highlight}style={{fontWeight:800, color: "#3b82f6", fontSize: "3rem", marginTop: 75 }}>{topic}</div>
          <BlogMarkdown content={blog} />
          <button
            className={styles.button2}
            style={{ marginTop: 32,marginBottom: 32, color: "#fff" }}
            onClick={() => { setPage("input"); setBlog(""); setTopic(""); }}
          >
            Back to Home
          </button>
        </>
      )}
      </div>
    </>
  );
}

export default App;
