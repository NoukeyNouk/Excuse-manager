/**
 * app.js — основная логика UI.
 *
 * Управляет состояниями формы: idle → loading → success / error.
 */

import { sendMessage } from "./api.js";

// --- DOM Elements ---
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const button = document.getElementById("send-button");
const responseArea = document.getElementById("response-area");
const responseText = document.getElementById("response-text");
const loading = document.getElementById("loading");
const errorMessage = document.getElementById("error-message");

// --- UI State Helpers ---

function setLoading(isLoading) {
    input.disabled = isLoading;
    button.disabled = isLoading;

    if (isLoading) {
        loading.classList.remove("hidden");
        errorMessage.classList.add("hidden");
    } else {
        loading.classList.add("hidden");
    }
}

function showResponse(text) {
    responseText.textContent = text;
    responseArea.classList.remove("hidden");
}

function showError(text) {
    errorMessage.textContent = text;
    errorMessage.classList.remove("hidden");
}

function clearState() {
    errorMessage.classList.add("hidden");
}

// --- Form Handler ---

async function handleSubmit(event) {
    event.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    clearState();
    setLoading(true);

    try {
        const data = await sendMessage(message);
        showResponse(data.response);
        input.value = "";
    } catch (err) {
        showError(err.message);
    } finally {
        setLoading(false);
        input.focus();
    }
}

// --- Event Listeners ---
form.addEventListener("submit", handleSubmit);
