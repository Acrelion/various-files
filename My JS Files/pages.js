// A book has pages numerated from 1 to N. The total number of digits used to numerate the pages in the books is 1095.
// How many pages the book has?

var digits = 0;
var pageNumber = 1;

while (digits < 1095) {

    digits += (pageNumber.toString().length);

    if (digits !== 1095) {
        pageNumber += 1;
    }
}

console.log("\n"+ pageNumber);