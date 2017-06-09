$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var cmdsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.hostname + ':8443/terminal/');
    $('.commandbtn').prop('disabled', true);
    $('.commandbtn').on('click', function(event) {
    	$('.commandbtn').prop('disabled', true);
    	var msg = {
    		id: $(this).attr("id"),
    	};
    	cmdsock.send(JSON.stringify(msg));
    	return false;
    });
    cmdsock.onmessage = function(message){
    	var data = JSON.parse(message.data);

    	$("#cmdpre").append('<span class="text-success cmdline">' +
    		data.cmdline + '</span><br>');
    	$("#cmdpre").scrollTop( $("#cmdpre")[0].scrollHeight );
    	$(".commandbtn").prop("disabled", data.status);
    };
});
