import { useState } from "react";
import "../App.css";

function App() {
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/analyze/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ review })
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="app">
      <h1>Feedback Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Type your feedback..."
        />
        <button type="submit">Analyze</button>
      </form>

      {result && (
        <div className="results">
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Summary:</strong> {result.summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
