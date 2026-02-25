import React from "react";
import ReactMarkdown from "react-markdown";
import styles from "./App.module.css";

export default function BlogMarkdown({ content }) {
  return (
    <div className={styles.blogContainer}>
      <ReactMarkdown>{content}</ReactMarkdown>
    </div>
  );
}
