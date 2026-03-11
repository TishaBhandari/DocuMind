export default function SummaryCard({ summary }) {
  return (
    <div className="card p-4 mb-5">
      <div className="d-flex align-items-center gap-2 mb-3">
        <span className="badge badge-soft">Summary</span>
      </div>
      <p className="summary-text" style={{ whiteSpace: "pre-line" }}>
        {summary}
      </p>
    </div>
  );
}