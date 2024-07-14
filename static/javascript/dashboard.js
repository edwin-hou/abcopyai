var socket = io('http://54.172.23.104/', { path: '/server', autoConnect: false})
console.log(socket)
socket.on('connect', function () {
console.log("a")
socket.emit("get_data", "edwin.s.hou@gmail.com")
socket.on('data', (emails)=>{
    console.log(emails)
    for(let i =0; i< emails.length; i++){
    let email = document.createElement("p");
    email.textContent = JSON.stringify(emails[i])
    document.querySelector("div#data").appendChild(email)
    }

})
})