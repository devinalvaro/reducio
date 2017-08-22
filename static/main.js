$(document).ready(function() {
    function summarize(text, number) {
        $.ajax({
            url: "/reducio",
            type: "POST",
            data: {
                'text': text,
                'number': number
            },
            success: function(data) {
                $("#summarized-text-box").css('background-color', '#66bb6a');
                $("#summarized-text-box").html(data);
            }
        });
    };

    $("#sum-btn").click(function() {
        var text = $("#text-box").val();
        var number = $("#number-box").val();
        summarize(text, number);
    });
});
