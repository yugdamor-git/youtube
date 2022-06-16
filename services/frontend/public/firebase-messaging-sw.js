importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var swVersion="2.0.0";

firebase.initializeApp({
    messagingSenderId: "923550400367",
});
  
const messaging = firebase.messaging();
messaging.setBackgroundMessageHandler();

self.addEventListener('push', (event) => {
    console.log('Received a push message');
    console.log(event.data.json().data.notification);

    const payload = JSON.parse(event.data.json().data.notification)
    console.log(payload["title"]);
    event.waitUntil(
        self.registration.showNotification(payload.title, {
            body: payload.body,
            icon: payload.icon,
            image: payload.image,
            data: payload,
        })
    );

    console.log("current SW version: ",swVersion);
    console.log('latest SW version: ', event.data.json().data.swVersion);
    if(event.data.json().data.swVersion != swVersion){
        console.log("SW Version is different, Updating SW");
        self.registration.update()
    }
});

self.addEventListener('notificationclick', (event) => {
    clients.openWindow(event.notification.data.url);
});