var makeColorRect = (function (color, repeats){
	repeats = repeats || 10;
	
	var lengthC = color.length;
	var empty_space = Array(lengthC + 1).join(" ");
	var additional_spaces = Array(repeats - 2).join(" ");

	var full_row = Array(repeats + 1).join(color + " ");
	var two_words_row = color + " " + Array(repeats - 1).join(empty_space) + additional_spaces + " " + color;

	console.log(full_row);
	console.log(two_words_row);
	console.log(full_row);
}());

