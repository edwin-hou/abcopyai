var socket = io('http://54.172.23.104/')
console.log(socket, new Date().toLocaleString())
socket.on('connect', function () {
console.log("connected", new Date().toLocaleString())
socket.emit("get_data", "edwin.s.hou@gmail.com")
socket.on('data', (emails)=>{
    console.log(emails, new Date().toLocaleString())
    for(let i =0; i< emails.length; i++){
    let email = document.createElement("p");
    email.textContent = JSON.stringify(emails[i])
    document.querySelector("div#data").appendChild(email)
    }

})
})