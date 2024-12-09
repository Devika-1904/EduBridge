document.getElementById('send-message').addEventListener('click', function() {
    let message = document.getElementById('message-input').value;

    if (message.trim() !== "") {
        // Send message via AJAX
        fetch('/send_message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Append new message to the chat box
            let chatBox = document.getElementById('chat-box');
            let newMessage = document.createElement('div');
            newMessage.classList.add('chat-message');
            newMessage.innerHTML = `<strong>You</strong>: <p>${message}</p>`;
            chatBox.appendChild(newMessage);

            // Clear the input
            document.getElementById('message-input').value = '';
            chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to bottom
        })
        .catch(error => console.error('Error sending message:', error));
    }
});
