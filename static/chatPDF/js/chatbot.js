function ChatBot(historyElement) {
    this.service = new Server();
    this.historyElement = historyElement;
};
ChatBot.prototype = {

    sendMessage(text){
        this.addHistory(text,'user');
        this.service.sendMessage(text).then( (botText) => {
            this.addHistory(botText,'bot');
            console.log(botText)
        });
    },
    addHistory(text, user){
        if (this.historyElement){
            // create the chatMessage to control the user class
            const chatMessageElement = document.createElement('div');
            chatMessageElement.className = `chat-message ${user}`;

            const messageElement = document.createElement('div');
            messageElement.className = 'message-text';
            messageElement.textContent = text;

            chatMessageElement.appendChild(messageElement);
            this.historyElement.appendChild(chatMessageElement);
        }
    }
}


chatbot = new ChatBot(document.querySelector('.chat-history'));
document.querySelector('#sendMessage').addEventListener('click', () => {
    const input = document.querySelector('#inputText');
    this.chatbot.sendMessage(input.value);
    input.value = '';
})