$(document).ready(function() {
    function summarize(text) {
        $.ajax({
            url: "/reducio",
            type: "POST",
            data: {
                'text': text
            }
        });

        var sentences = $.getJSON("../data/sentences.json");
        for (var key in sentences) {
            if (sentences.hasOwnProperty(key)) {
                $("#boxes").append(sentences[key] + "<br />");
            }
        }
    };

    $("#sum-btn").click(function() {
        var text = $("#text-box").val();
        summarize(text);
    });
});
