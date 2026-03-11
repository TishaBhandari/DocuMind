import { useState } from "react";
import { summarizePdf, generateQna } from "../services/api";

export default function ActionPanel({ pdfId, onSummary, onQna }) {
  const [loading, setLoading] = useState(false);

  const handleSummary = async () => {
    try {
      setLoading(true);
      const res = await summarizePdf(pdfId);
      onSummary(res.data.summary);
    } finally {
      setLoading(false);
    }
  };

  const handleQna = async () => {
    try {
      setLoading(true);
      const res = await generateQna(pdfId);
      onQna(res.data.questions, res.data.answers);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card p-4 mb-5">
      <h5 className="section-title">What would you like to do?</h5>

      <div className="d-flex flex-wrap gap-3">
        <button
          className="btn btn-primary"
          disabled={loading}
          onClick={handleSummary}
        >
          📄 Generate Summary
        </button>

        <button
          className="btn btn-outline-primary"
          disabled={loading}
          onClick={handleQna}
        >
          ❓ Generate Questions
        </button>
      </div>
    </div>
  );
}