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
    sendFiles(files){
        this.service.sendFiles(files).then( (data) => {
            console.log(data)
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
document.querySelector('#enviar-arquivo').addEventListener('click', () => {
    const files = document.getElementById('input-arquivos').files;
    this.chatbot.sendFiles(files);
})

chatbot = new ChatBot(document.querySelector('.chat-history'));
document.querySelector('#sendMessage').addEventListener('click', () => {
    const input = document.querySelector('#inputText');
    this.chatbot.sendMessage(input.value);
    input.value = '';
})
