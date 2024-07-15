var socket = io.connect({'force new connection': true, transports: ['WebSocket', 'Flash Socket', 'AJAX long-polling']})
console.log(new Date().toLocaleString(), socket)
socket.on('connect', function () {
    console.log(new Date().toLocaleString(), "connected")
    socket.emit("get_data", "edwin.s.hou@gmail.com")
    console.log(new Date().toLocaleString(), "emitted")
    socket.on('data', (emails) => {
        console.log(new Date().toLocaleString(), emails)
        for (let i = 0; i < emails.length; i++) {
            let email = document.createElement("p");
            email.textContent = JSON.stringify(emails[i])
            document.querySelector("div#data").appendChild(email)
        }

    })
})


