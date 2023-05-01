function Server() {
    
}

Server.prototype = {

    async sendMessage(text) {
        const parameter = new FormData();
        parameter.append('text', text);
        return await this.send('POST', '/api/chat/', parameter);
    },
    async sendPDF(file) {
        var parameter = new FormData();
        parameter.append('files', file);
        return await this.send('POST', 'message');
    },
    getCrtfToken() {
        return document.getElementsByName('csrfmiddlewaretoken')[0].value;
    },
    generateTempToken() {
        let token = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        for (let i = 0; i < 32; i++) {
          token += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return token;
    },
    send(method, url, parameter){
        return new Promise((resolve, reject) => {
            let xhr = new XMLHttpRequest();  
            xhr.open(method, url);
            xhr.setRequestHeader('X-CSRFToken', this.getCrtfToken());  
            xhr.onload = function () {
                if (this.status >= 200 && this.status < 300) {
                    resolve(xhr.response);
                } else {
                    reject({
                        status: this.status,
                        statusText: xhr.statusText
                    });
                }
            };
            xhr.onerror = function () {
                reject({
                    status: this.status,
                    statusText: xhr.statusText
                });
            };
            xhr.send(parameter);
        });
    },
}