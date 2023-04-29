function Server() {
    
}

Server.prototype = {

    async sendMessage(text) {
        var parameter = new FormData();
        parameter.append('text', text);
        return await this.send('POST', 'chatBot/executeMessage/');
    },
    async sendPDF(file) {
        var parameter = new FormData();
        parameter.append('files', file);
        return await this.send('POST', 'message');
    },
    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          const cookies = document.cookie.split(";");
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
    },
    send(method, url, parameter){
        const csrftoken = this.getCookie('csrftoken');
        return new Promise(function (resolve, reject) {
            let xhr = new XMLHttpRequest();  
            xhr.open(method, url, true);
            xhr.setRequestHeader('x-csrf-token', csrftoken);    
            xhr.setRequestHeader("Content-type", "application/json");
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
            xhr.send({'teste':'teste'});
        });
    },
}