var socket = io.connect()
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


document.querySelector("video").addEventListener('ended', ()=>{
    document.querySelector('video source').src = "brawl_clip" + Math.floor(Math.random() * (9 - 1 + 1) + 1);
})