var login = require('facebook-chat-api');
var hidden = require('./hidden-password.js');

var credentials = require('./credentials.json');
var username = credentials.username;
var password = credentials.password;

var say = require('say');

function run() {
   // FIRST WE READ IN THE PASSWORD

   if (password === undefined) {

      hidden.READ("password : ", function(entered_password) {
         password = entered_password;
         doLogin();

      });

   } else {
      doLogin();
   }

}

// THEN WE LOGIN TO FACEBOOK
/*
 * type: message
 * sender_name: <NAME>
 * sender_id: <ID>
 * participant_names: ALL MEMBERS (EXCEPT SELF)
 * participant_ids: <ID>
 * body: <THE MESSAGE>
 * thread_id: <THREAD_ID>
 * location: <LOCATION DATA>
 */

function doLogin() {

login ( {email: username, password: password}, function (err, api) {

   if (err) return console.error(err);

   api.listen(function (err, message) {

      console.log(message.thread_id);
      console.log(message.sender_name);
      console.log(message.body);
      console.log("");

      say.speak(null, message.sender_name + " ... " + message.body);

   });

});

}


run();
