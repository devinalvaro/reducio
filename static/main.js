$(document).ready(function() {
    function summarize(text) {
        $.ajax({
            url: "/reducio",
            type: "POST",
            data: {
                'text': text
            },
            success: function(data) {
                $("#boxes").html(data);
            }
        });
    };

    $("#sum-btn").click(function() {
        var text = $("#text-box").val();
        summarize(text);
    });
});
