$(document).ready(function() {
    function summarize(text) {
        $.ajax({
            url: "/test",
            type: "POST",
            data: {
                'text': text
            }
        });
    };

    $("#sum-btn").click(function() {
        var text = $("#text-box").val();
        summarize(text);
    });
});
