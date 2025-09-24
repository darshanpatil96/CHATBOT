const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const messagesContainer = document.getElementById("messages");

const appendMessage = (text, sender) => {
    const wrapper = document.createElement("div");
    wrapper.classList.add("flex", "items-end", sender === "user" ? "justify-end" : "justify-start");

    const innerWrapper = document.createElement("div");
    innerWrapper.classList.add("flex", "flex-col", "space-y-2", "text-sm", "max-w-xs", "mx-2", "order-2", sender === "user" ? "items-end" : "items-start");

    const bubble = document.createElement("span");
    bubble.innerText = text;
    bubble.classList.add(
        "px-4", "py-2", "rounded-2xl", "inline-block", "shadow-md"
    );

    if (sender === "user") {
        bubble.classList.add("bg-blue-600", "text-white");
    } else {
        bubble.classList.add("bg-gray-600", "text-white");
    }

    innerWrapper.appendChild(bubble);
    wrapper.appendChild(innerWrapper);
    messagesContainer.prepend(wrapper); // keeps newest at bottom
};

// Handle send
const sendMessage = () => {
    const text = userInput.value.trim();
    if (!text) return;

    appendMessage(text, "user");
    userInput.value = "";

    fetch("/get", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
        appendMessage(data.response, "bot");
    })
    .catch(err => console.error("Error:", err));
};

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});
