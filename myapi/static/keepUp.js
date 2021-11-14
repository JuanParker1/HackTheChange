// const mainFriendList = [];

// //Friend Object
// function Friend(first, last, email, pic) {
//     this.firstName = first;
//     this.lastName = last;
//     this.email = email;
//     this.pic = pic;
//     this.getFirst = function(){
//         return this.first;
//     }
// }

// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

// Create a new list item when clicking on the "Add" button
function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue);

  var myList = document.getElementById("friend-list");
  li.appendChild(t);
  if (inputValue === '') {
    alert("Invalid User");
  } else {
    myList.innerHTML += 
    "<li>"+
    inputValue+
    "<div class='detail'><i><b> Request Sent </i> </div>"+
    "</li>";
  }
  document.getElementById("myInput").value = "";

  var span = document.createElement("SPAN");
  span.className = "close";

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}