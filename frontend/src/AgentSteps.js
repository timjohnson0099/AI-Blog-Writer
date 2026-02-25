import React from "react";
import styles from "./App.module.css";

const AGENT_STEPS = [
  "Researching sources and gathering information...",
  "Extracting and verifying facts, identifying trends...",
  "Structuring and composing the blog post...",
  "Reviewing, formatting, and finalizing..."
];

export default function AgentSteps({ currentStep }) {
  return (
    <div className={styles.agentStep}>
      {AGENT_STEPS[currentStep]}
    </div>
  );
}
