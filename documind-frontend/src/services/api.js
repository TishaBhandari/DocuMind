import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export const uploadPdf = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return api.post("/upload", formData);
};

export const summarizePdf = (pdfId) => {
  return api.post(`/summarize/${pdfId}`);
};

export const generateQna = (pdfId) => {
  return api.post(`/questions/${pdfId}`);
};

export default api;