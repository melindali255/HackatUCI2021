$(document).on('mouseover mouseout', '#comments', function() {
    let comments = document.querySelectorAll('yt-formatted-string.ytd-comment-renderer');

    console.log("length of comments: " + comments.length);

    for (let i = 0; i < comments.length; i++) {
        if (!comments[i].classList.contains("published-time-text")) {
            comments[i].style["background-color"] = "red";
        }
    }

});
