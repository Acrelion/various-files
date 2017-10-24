/**
         *** Exercise about classes (Classic inheritance)***
* This script creates two classes. Computer and ComputerShop.
* The second class uses the first to create a simple application for
* managing a computer shop. We can add, remove, sell, get the sold count.
*/


var Computer = (function(){
    function getRandomStringViaNumbers() {
        var numbers = [];
        var theString = "";

        for(var i = 0; i < 10; i++) {               // 65 to 122 char code
            numbers.push(Math.floor(Math.random() * (122 - 66 + 1) + 66));
        }
        return String.fromCharCode.apply(theString, numbers);
    }


    function Computer(year, price, isNotebook, hardDiskMemory, freeMemory, operationSystem){

        this.SKU = getRandomStringViaNumbers();
        this.year = year;
        this.price = price;
        this.isNotebook = isNotebook;
        this.hardDiskMemory = hardDiskMemory;
        this.freeMemory = freeMemory;
        this.operationSystem = operationSystem;

    }

    Computer.prototype.changeOperationSystem = function(newOperationSystem) {
        this.operationSystem = newOperationSystem;
    };

    Computer.prototype.useMemory = function(memory) {
        if (this.freeMemory < memory) {
            console.log("Not enough memory!");
        }
        else {
            this.freeMemory -= memory;
        }
    };


    return Computer;

}());


var ComputerShop = (function(){


    function ComputerShop(){
        this.storage = [];
        this.soldComputers = 0;
    }

    Object.defineProperty(ComputerShop.prototype, "storage", {
       get: function() {
           return this._storage;
       },
       set: function(value){
           this._storage = value;
           return this;
       }
    });

    Object.defineProperty(ComputerShop.prototype, "soldComputers", {
        get: function() {
            return this._soldComputers;
        },
        set: function(value) {
            this._soldComputers = value;
            return this;
        }
    });

    ComputerShop.prototype.addToStorage = function(comp){
        this.storage.push(comp);
    };

    ComputerShop.prototype.removeFromStorage = function (givenSKU) {
        for (var i = 0; i < this.storage.length; i++) {
            if (this.storage[i].SKU === givenSKU) {

                this.storage.splice(i, 1);
            }
        }
    };

    ComputerShop.prototype.sell = function(sellSKU) {
        this._soldComputers += 1;
        this.removeFromStorage(sellSKU);
    };

    ComputerShop.prototype.getSoldComputersCount = function(){
        return this._soldComputers;
    };

    ComputerShop.prototype.getComputersInStorageCount = function () {
        return this.storage.length;
    };

    return ComputerShop;

}());

// Testing
var shop = new ComputerShop();
var comp1 = new Computer(2015, 1868, true, 700, 8, "Windows 10");
var comp2 = new Computer(2014, 1200, true, 500, 4, "Windows 8.1");
var comp2SKU = comp2.SKU;

shop.addToStorage(comp1);
shop.addToStorage(comp2);

console.log("The original storage is: " + shop.getComputersInStorageCount());
console.log("Ants ate the second computer");

shop.removeFromStorage(comp2SKU);

console.log("Now we have in storage: " + shop.getComputersInStorageCount() + " computers.");

console.log("\nA customer came and got the remaining one.");
shop.sell(comp1.SKU);

console.log("\n\nNow we have " + shop.getComputersInStorageCount() + " in storage");
console.log("Computers sold today: " + shop.getSoldComputersCount());








