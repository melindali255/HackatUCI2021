$(document).on('mouseover mouseout', '#comments', function() {

    /* Highlights individual comment texts */
    // let comments = document.querySelectorAll('yt-formatted-string.ytd-comment-renderer');

    // for (let i = 0; i < comments.length; i++) {
    //     if (!comments[i].classList.contains("published-time-text")) {
    //         comments[i].style["background-color"] = "red";
    //     }
    // }

    /* Remove entire comment */
    let comment_threads = document.getElementsByTagName("ytd-comment-thread-renderer");

    // console.log("length of comments threads: " + comment_threads.length);

    for (let i = 0; i < comment_threads.length; i++) {
        let comment = comment_threads[i].querySelector("#content-text");
        if (comment.textContent.includes("Me")) { //Remove comment if text includes the word
            // comment.style["background-color"] = "red";
            comment_threads[i].parentNode.removeChild(comment_threads[i]);
        }
    }
});