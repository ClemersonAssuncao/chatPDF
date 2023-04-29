document.querySelector('#sendMessage').addEventListener('click', () => {
    const server = new Server();
    server.sendMessage(document.querySelector('#inputText').value).then( (data) => {
        //atualiza retorno -- data
        console.log(data)
    });
})