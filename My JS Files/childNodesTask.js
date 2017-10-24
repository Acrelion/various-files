
/**
 * This module consists of 4 parts - 1. Init IFE, 3 event listeners.
 * The IFE "createNeededItems" selects all the divs in the body. Then it gets the one in the middle.
 * Next, it creates an unordered list and adds 5 items to it.
 * Also, an input field and 3 buttons are added.
 * The first button has an event listener which adds a new item at the given in the input field position.
 * The second button does the opposite. It removes an item.
 * The third button has an event listenr which changes the style of the specified element.
 */
var mainModule = (function(){
	
	var bodyDoc, allDivs, middleDiv, button, remButton, colorButton, inputField, fragment, unorderedList, listItem, i, element, valueOfField, newItem, itemToRemove, itemToColor;

	(function createNeededItems() {
		// select body
		bodyDoc = document.body;
		
		// select the div elements, then the middle one
		allDivs = document.getElementsByTagName("div");
		middleDiv = allDivs[ Math.floor(allDivs.length / 2) + 1 ];
		
		// create buttons and input field
		button = document.createElement("button");
		button.innerHTML = "Add Element";
		
		remButton = document.createElement("button");
		remButton.innerHTML = "Remove Element";
		
		colorButton = document.createElement("button");
		colorButton.innerHTML = "Color Element!!!";
		
		inputField = document.createElement("input");
		inputField.setAttribute("type", "text");
		
		// create UL with 5 elements with content "Item 1"
		// UL's id is set to "myUL"
		fragment = document.createDocumentFragment();
		unorderedList = document.createElement("ul");
		unorderedList.id = "myUL";
		listItem = document.createElement("li");
		
		for (i = 0; i < 5; i++) {
			element = listItem.cloneNode();
			element.innerHTML = "Item " + (i + 1);
			unorderedList.appendChild(element);
		}
		
		
		// append UL to fragment,
		// append field, button and UL to the body
		bodyDoc.insertBefore(inputField, allDivs[0])
		bodyDoc.insertBefore(button, allDivs[0]);
		bodyDoc.insertBefore(remButton, allDivs[0]);
		bodyDoc.insertBefore(colorButton, allDivs[0]);
		
		fragment.appendChild(unorderedList);
		middleDiv.appendChild(fragment);
			
	}()); // end of Init IFE


	// helper function
	function checkFieldValue(valueOfField) {
		if (valueOfField !== "undefined" &&
			isFinite(+valueOfField)      &&
			!(isNaN(valueOfField))       &&
			valueOfField !== "") {
				
				return true;
			}
		else {
			return false;
		}	
	}

	// event listenr for the button ( add new item to the UL at given position)
	button.addEventListener("click", function () {
		
		valueOfField = inputField.value;
		
		
		// check if the value is valid
		if (checkFieldValue(valueOfField)) {
			
			// if the value is 0
			if (+valueOfField === 0) {
				++valueOfField;
			}
			
			// create new element
			newItem = listItem.cloneNode();
			newItem.innerHTML = "New Item :)";
			
			// add the new element to the given position in the UL
			unorderedList.insertBefore( newItem, unorderedList.children[ +valueOfField - 1 ]  );
		}
		
	}, false);
	
	remButton.addEventListener("click", function () {
		valueOfField = inputField.value;
		
		// check if the value is valid
		if (checkFieldValue(valueOfField)) {
			
			// if the value is 0
			if (+valueOfField === 0) {
				++valueOfField;
			}
			
			// get the element to remove
			itemToRemove = unorderedList.children[ +valueOfField - 1 ];
			
			// remove the item via the paren node;
			if (unorderedList.children.length === 0) {
				
			}
			else if (unorderedList.children.length < +valueOfField) {
				valueOfField = unorderedList.children.length - 1;
			}
			else {
				unorderedList.removeChild(itemToRemove);
			}
			
			
			
		}
	}, false);
	
	// event listener for coloring the element at the specified position
	colorButton.addEventListener("click", function () {
		valueOfField = inputField.value;
		
		if ( checkFieldValue(valueOfField) ) {
			
			// if the value is 0
			if (+valueOfField === 0) {
				++valueOfField;
			}
			
			// get the element to color
			itemToColor = unorderedList.children[ +valueOfField - 1 ];
			
			if (unorderedList.children.length === 0) {
				
			}
			else if (unorderedList.children.length < +valueOfField) {
				valueOfField = unorderedList.children.length - 1;
			}
			else {
				itemToColor.style.backgroundColor = "green";
				itemToColor.style.color = "red";
			}			
			
		}
	});
}());