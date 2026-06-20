/**
 * api.js — HTTP-клиент для взаимодействия с бэкендом.
 *
 * Каждая функция возвращает Promise с JSON-ответом.
 * При ошибке сети или сервера выбрасывает Error с понятным сообщением.
 */

const API_BASE = "/api";

/**
 * Отправляет сообщение пользователя на /api/chat.
 *
 * @param {string} message — текст сообщения
 * @returns {Promise<{response: string}>} — ответ от агента
 * @throws {Error} — если сервер вернул ошибку или сеть недоступна
 */
export async function sendMessage(message) {
    let res;

    try {
        res = await fetch(`${API_BASE}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
    } catch {
        throw new Error("Не удалось подключиться к серверу. Проверьте соединение.");
    }

    const data = await res.json();

    if (!res.ok) {
        throw new Error(data.error || `Ошибка сервера: ${res.status}`);
    }

    return data;
}
