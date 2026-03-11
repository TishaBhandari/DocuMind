import { useState } from "react";
import UploadCard from "../components/UploadCard";
import ActionPanel from "../components/ActionPanel";
import SummaryCard from "../components/SummaryCard";
import QnaAccordion from "../components/QnaAccordion";

export default function Home() {
  const [pdfId, setPdfId] = useState(null);
  const [summary, setSummary] = useState("");
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);

  return (
    <div className="app-container">
      <h2 className="text-center app-title mb-2">
        📘 DocuMind
      </h2>
      <p className="text-center app-subtitle mb-5">
        Upload a PDF and instantly generate study-friendly summaries and questions
      </p>

      <UploadCard onUploadSuccess={setPdfId} />

      {pdfId && (
        <ActionPanel
          pdfId={pdfId}
          onSummary={setSummary}
          onQna={(q, a) => {
            setQuestions(q);
            setAnswers(a);
          }}
        />
      )}

      {summary && <SummaryCard summary={summary} />}

      {questions.length > 0 && (
        <QnaAccordion questions={questions} answers={answers} />
      )}
    </div>
  );
}