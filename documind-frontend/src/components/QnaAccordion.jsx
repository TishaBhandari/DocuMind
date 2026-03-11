export default function QnaAccordion({ questions, answers }) {
  return (
    <div className="card p-4 mb-4">
      <h5 className="section-title mb-3">Questions & Answers</h5>

      <div className="accordion" id="qnaAccordion">
        {questions.map((q, idx) => (
          <div className="accordion-item" key={idx}>
            <h2 className="accordion-header">
              <button
                className="accordion-button collapsed"
                data-bs-toggle="collapse"
                data-bs-target={`#q${idx}`}
              >
                Q{idx + 1}. {q}
              </button>
            </h2>
            <div id={`q${idx}`} className="accordion-collapse collapse">
              <div className="accordion-body">{answers[idx]}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}