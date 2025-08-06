document.addEventListener("DOMContentLoaded", () => {
    const socket = io();
    const messageInput = document.querySelector("#message");
    const messagesContainer = document.querySelector("#messages");

    // Escuta por mensagens recebidas do servidor
    socket.on("message", function (msg) {
        var messageDiv = document.createElement("div");
        messageDiv.classList.add("message");
        messageDiv.innerText = msg;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Rola para baixo automaticamente
    });

    // Envio de mensagens
    function sendMessage(event) {
        var message = messageInput.value.trim();
        if (message !== "") {
            socket.send(message);
            messageInput.value = "";
        }
    }

    // Envio de mensagens ao pressionar o botão
    document.getElementById("sendButton").addEventListener("click", sendMessage);

    // Envio de mensagens ao pressionar "Enter"
    messageInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage(event);
        }
    });
});
