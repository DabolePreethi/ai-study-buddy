const API = "http://127.0.0.1:8000";

async function uploadPDF() {
    const file = document.getElementById("pdfUpload").files[0];
    const formData = new FormData();
    formData.append("file", file);

    await fetch(`${API}/upload-pdf/`, {
        method: "POST",
        body: formData
    });

    alert("PDF Uploaded!");
}

async function askQuestion() {
    const question = document.getElementById("question").value;

    const res = await fetch(`${API}/ask/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question})
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.answer;
}

async function summarize() {
    const text = document.getElementById("text").value;

    const res = await fetch(`${API}/summarize/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.summary;
}

async function generateQuiz() {
    const text = document.getElementById("text").value;

    const res = await fetch(`${API}/quiz/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.quiz;
}

async function generateFlashcards() {
    const text = document.getElementById("text").value;

    const res = await fetch(`${API}/flashcards/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text})
    });

    const data = await res.json();
    document.getElementById("output").innerText = data.flashcards;
}
