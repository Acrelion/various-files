/**
 * This script has the task of creating a canvas image of a simple house + sky and grass.
 * The function that does the job acepts argument - floors, which stands for how many floors the house will have.
 * NOTE: The calculations are ment to be scalable, but for some canvas sizes there are problems.
 */
var main = (function(){
	var canvas, context, xFloor, yFloor, xWindow, yWindow, xDoor, yDoor;	
	
	canvas = document.createElement("canvas");
	canvas.id = "myCanvas";
	canvas.width  = 700;
	canvas.height = 400;
	canvas.style.border = "1px solid #000";
	context = canvas.getContext("2d");
	
	document.body.appendChild(canvas);
		
	xFloor = canvas.width / 2;							// 200
	yFloor = canvas.height / (canvas.height / 100) ;	// 100
	xWindow = xFloor / 10;
	yWindow = yFloor / 2;
	xDoor = xWindow + (xWindow / 2);
	yDoor = yWindow;
	
	function createFloor(floors){
		var startFloor, startY,  index;
		
		context.save(); // sky
		context.fillStyle = "#659CEF";
		context.fillRect(0, 0, canvas.width, canvas.height * 0.75);
		context.restore();
		
		context.save(); // grass
		context.fillStyle = "#7DBD00";
		context.fillRect(0, canvas.height * 0.75, canvas.width, canvas.height * 0.25);
		context.restore();
		
		startFloor = (canvas.width / 2) - (xFloor / 2 ); // x starting point for the floor
				
		for ( index = 0; index < floors; index++) {
			
			startY = canvas.height - (index * yFloor); // current y starting point for the floor
			
			// set style for the floors, windows, the door and the roof
			context.strokeStyle = "white";
			context.lineWidth = 3;
			
			context.strokeRect( startFloor , startY - yFloor, xFloor, yFloor); // floor
			
			context.strokeRect(  // first window to the left (to wall)
								startFloor + (xWindow / 2),
								(startY - ( yFloor / 2) ) - (yWindow / 2),
								xWindow,
								yWindow
			);
							
			context.strokeRect( // second window to the left
								startFloor + (xWindow * 2),
								(startY - ( yFloor / 2) ) - (yWindow / 2),
								xWindow,
								yWindow
			);
							
			context.strokeRect( // first window to the right
								(startFloor + xFloor) - ( (xWindow * 2) + xWindow ),
								(startY - ( yFloor / 2) ) - (yWindow / 2),
								xWindow,
								yWindow
			);				  	
							
			context.strokeRect( // second window to the right (to wall)
								(startFloor + xFloor) - ( (xWindow + (xWindow / 2) ) ),
								(startY - ( yFloor / 2) ) - (yWindow / 2),
								xWindow,
								yWindow
			);
															
							
			
			if (index === 0) { // draw door
				context.strokeRect( (canvas.width / 2) - (xDoor / 2), canvas.height - yDoor, xDoor, yDoor);
			}
			
			
			// draw roof
			if ( (index + 1) === floors) {
				
				context.beginPath();
				context.moveTo( (startFloor  * 2), (startY - (yFloor * 2) ) ); 
				context.lineTo( startFloor - (xFloor * 0.2), (startY - yFloor) );
				context.lineTo( startFloor + xFloor +  (xFloor * 0.2), (startY - yFloor) );
				context.closePath();
				
			}
						
			context.stroke();
		
		} // end of for loop
				
	} // end of createFloor function
	
	// calling the function to create a building with 2 floors
	createFloor(2);
		
}());