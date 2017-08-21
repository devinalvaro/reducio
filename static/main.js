$(document).ready(function() {
    // Summarize Function //
    function summarize(text) {
        $("#boxes").html(text)
    };

    // Click Events //
    $("#sum-btn").click(function() {
        var text = $("#text-box").val();
        summarize(text);
    });
});
