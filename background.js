// 'use strict';

// chrome.runtime.onMessage.addListener(
//     function (request, sender) {
//         console.log("got message");
//         if (request.type == 'info') {
//             var port = chrome.runtime.connectNative("com.youtube_comments")
            
//             port.postMessage(request.value)

//             port.onMessage.addListener(function (message) {
//                 console.log(message);
//             })

//             port.onDisconnect.addListener(function (error) {
//                 console.log(error);
//                 console.log("last error: " + chrome.runtime.lastError.message)
//             })
//         }
//     }
// )