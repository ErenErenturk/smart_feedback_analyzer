import { useState } from "react";
import "./App.css";

function App() {
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://localhost:8000/analyze/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ review }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({
        sentiment: "Error",
        summary: "Something went wrong. Please try again.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold underline text-center text-blue-600 mb-6">
        Feedback Analyzer
      </h1>

      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md bg-white shadow-md rounded-lg p-6 space-y-4"
      >
        <textarea
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Type your feedback..."
          className="w-full h-32 p-3 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition"
        >
          Analyze
        </button>
      </form>

      {loading && (
        <div className="flex items-center mt-4 text-blue-600">
          <div className="animate-spin rounded-full h-6 w-6 border-t-2 border-blue-600 border-solid mr-2"></div>
          <span className="font-medium">Analyzing...</span>
        </div>
      )}

      {result && (
        <div className="mt-6 w-full max-w-md bg-white shadow-md rounded-lg p-4">
          <p className="mb-2">
            <strong>Sentiment:</strong>{" "}
            <span className="text-blue-600">{result.sentiment}</span>
          </p>
          <p>
            <strong>Summary:</strong>{" "}
            <span className="text-gray-700">{result.summary}</span>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
