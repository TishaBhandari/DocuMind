import { useState } from "react";
import { uploadPdf } from "../services/api";

export default function UploadCard({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    try {
      const res = await uploadPdf(file);
      onUploadSuccess(res.data.pdf_id);
    } catch {
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card p-4 mb-5">
      <h5 className="section-title">Upload your PDF</h5>

      <div className="upload-box mb-3">
        <p className="mb-2 fw-medium">Choose a PDF document</p>
        <input
          type="file"
          accept="application/pdf"
          className="form-control"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </div>

      <button
        className="btn btn-primary w-100"
        disabled={!file || loading}
        onClick={handleUpload}
      >
        {loading ? "Uploading…" : "Upload & Process"}
      </button>
    </div>
  );
}