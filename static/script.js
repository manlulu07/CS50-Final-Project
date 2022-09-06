var serverAddress = location.host;
var connected = false;
var sock;

var infoDiv = document.getElementById("connectionStatusDiv");
var messageDiv = document.getElementById("messageFormDiv");

var addressTBox = document.getElementById('serverAddressTBox');
var connectBtn = document.getElementById('connectBtn');
var messageTBox = document.getElementById('messageTBox');

messageFormDiv.style.visibility = "hidden";
document.onkeydown = handleKeyDown;
document.onkeyup = handleKeyUp;

function disconnect() {
	sock.close();
	infoDiv.innerHTML = "Not connected";
	addressTBox.disabled = false;
	connectBtn.firstChild.data = "Connect to Server";
	messageFormDiv.style.visibility = "hidden";
	connected = false;
}

function connect() {
	if(connected) {
		disconnect();
		return;
	}

	serverAddress = addressTBox.value;
	sock = new WebSocket("ws://" + serverAddress + "/");

	sock.onopen = function(even) {
		connected = true;
		infoDiv.innerHTML = "Connected to: " + serverAddress;
		addressTBox.disabled = true;
		connectBtn.firstChild.data = "Disconnect";
		messageFormDiv.style.visibility = "visible";
	};
}

function sendMessage() {
	if(!connected)
		return;

	sock.send(messageTBox.value);
	messageTBox.value = "";
}

function handleKeyDown(e) {
	if(e.code == "ArrowLeft" || e.code == "ArrowRight" || e.code == "ArrowUp" || e.code == "ArrowDown")
		sock.send(e.code);
}

function handleKeyUp(e) {
	if(e.code == "ArrowLeft" || e.code == "ArrowRight" || e.code == "ArrowUp" || e.code == "ArrowDown")
		sock.send(e.code + "Up");
}