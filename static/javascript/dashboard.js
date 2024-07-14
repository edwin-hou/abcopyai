var socket = io.connect('http://' + document.domain + ':' + location.port, { transports: ['websocket', 'polling'] });

socket.on('connect', function () {
socket.emit("get_data", "edwin.s.hou@gmail.com")
socket.on('data', (emails)=>{
    for(let i =0; i< emails.length; i++){
    let email = document.createElement("p");
    email.textContent = JSON.stringify(emails[i])
    document.querySelector("div#data").appendChild(email)
    }

})
})