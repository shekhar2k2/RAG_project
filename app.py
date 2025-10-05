#importing essential librarry
import os
from flask import Flask, request, jsonify, render_template
from ingest import txt_frm_pdf, sentence_chunk
from retriever import HybridRetriever
from generator_gemini import generate_answer

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#local run with the help of jinja templating
app = Flask(__name__)
retriever = HybridRetriever()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

#uploading
@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    raw_text = txt_frm_pdf(file.read())
    chunks = sentence_chunk(raw_text, chunk_size=800, chunk_overlap=200)
    for c in chunks:
        c.setdefault("meta", {})
        c["meta"]["source"] = file.filename
    retriever.index_chunks(chunks)

    return jsonify({"message": f"Indexed {len(chunks)} chunks from {file.filename}."})
#askingh
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = retriever.retrieve(query, top_k=5, alpha=0.6)
    contexts = [r["text"] for r in results]
    answer = generate_answer(query, contexts)

    return jsonify({
        "query": query,
        "answer": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
