$(document).ready(function (){

    function switch_lamp(t_request, set_status) {
        $.ajax({
            url: "http://" + window.location.href.split("/")[2] + "/api/v1.0/wifi/lamp/" + set_status,
            type: t_request,
            contentType: "application/json; charset=utf-8",
            beforeSend: function (xhr) {
                $("#lamp-status").text("...");
            },
            complete: function (result) {
                var json = JSON.parse(result.responseText)
                $("#lamp-status").text(json.status);
            }
        });
    }

    function desliga() {

    }

    $(".toggle-input").change(function(){
        if(!$(this).is(":checked"))
            switch_lamp("PUT", "on");
        else
            switch_lamp("PUT", "off");
    });
});