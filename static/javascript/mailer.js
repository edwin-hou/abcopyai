//var socket = io.connect('http://' + document.domain + ':' + location.port);
//var socket = io.connect('http://' + document.domain + ':' + location.port, { transports: ['websocket', 'polling'] });
//var socket = io('http://54.172.23.104', { path: '/'})
var socket = io.connect('http://54.172.23.104/')

socket.on('connect', function () {

    document.querySelector('button#login').addEventListener("click",()=>{
        socket.emit('login')
    })
    socket.on("login_url", (url)=>{
        window.open(url, '_blank').focus();
    })
    document.querySelector('button#submit').addEventListener("click",()=>{
    let subject = document.querySelector('input#subject').value
    let content = document.querySelector('textarea#content').value
    let mailing_list = document.querySelector('input#list').value
    socket.emit('mail',{"subject": subject, "content": content, "mailing_list": mailing_list, "url": window.location.host})
    })


})