// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

// function addNew(name) {
// 	roster.push(name);
// }
// var new_name = prompt("Who's the new student?");
// addNew(new_name);
function addNew() {
	var newName = prompt("What name would you like to add?");
	roster.push(newName)
}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove() {
	var removeName = prompt("Who you want to remove?");
	var pos = roster.indexOf(removeName);
	roster.splice(pos, 1)
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
	console.log(roster);
}

// Start by asking if they want to use the web app
var start = prompt("would you like to start the roster web app? y/n");
var request = "empty";


// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (start === "y") {
	while (request !== "quit") {
		request = prompt("pls select an action: add, remove, display, or quit.")
		if (request === "add") {
			addNew();
		} else if (request === "remove") {
			remove();
		} else if (request === "display") {
			display();
		} else {
			alert("Not recognized.")
		}
	}
}
alert("Thanks for using the app! Pls refresh to start over.")