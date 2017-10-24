/**
 * This script creates a simple card game.
 * RULES:
 * 1. Shuffle the deck.
 * 2. Split the deck between the two players.
 * 3. Every round one card is shown. The largers wins.
 * 4. If the cars are the same. Show three cars. The last one is important.
 * 5. When the player's deck is empty, the game is over.
 * 6. Whoever has more cards wins.
 * */

var Card = (function () {

    function Card(rank, suit) {
        this.rank = rank;
        this.suit = suit;
    }

    Card.prototype.getRank = function () {
        return this.rank;
    };

    Card.prototype.compareCards = function (anotherCard) {
        if (Game.value[this.rank] < Game.value[anotherCard.rank]) {
            return true;
        }
        else {
            return false;
        }
    };

    return Card;
}());

var Deck = (function () {

    // helper function for generating random numbers in given range
    function getRandomNumber() {
        return Math.floor(Math.random() * (51 - 0 + 1) + 0);    // 51 is max, 0 is min
    }

    // All hands on deck!!!! ^^
    function Deck() {
        this.fullDeck = this.createDeck();
    }

    Deck.prototype.getCardsInDeck = function(){
        return this.fullDeck;
    };

    Deck.prototype.createDeck = function () {
        // Create deck by two for loops
        var suits = ['C', 'S', 'H', 'D'];
        var ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'];

        var resultDeck = [];

        for (var i = 0; i < suits.length; i++) {

            for (var j = 0; j < ranks.length; j++) {

                resultDeck.push(new Card(ranks[j], suits[i]));

            } // inner loop for iterating through ranks

        }// outer loop for iterating through suits

        return resultDeck;
    };


    Deck.prototype.shuffleDeck = function () {
        // loops though every card in the array and swaps
        // it with another card randomly selected from the array

        for (var i = 0; i < this.fullDeck.length; i++) {
            var randomIndex = getRandomNumber();

            if (randomIndex === i) {
                randomIndex = getRandomNumber();
            }

            var first = this.fullDeck[i];
            var second = this.fullDeck[randomIndex];
            var temp = first;

            //first = second;
            //second = temp;
            this.fullDeck[i] = second;
            this.fullDeck[randomIndex] = temp;

        }

    };

    return Deck;
}());



/** Wrapper*/
var Game = (function () {

    function Game(){
        this.values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10};

        // Create deck
        // Create players

        // Start game
    }

    return Game;
});


////////////////////////////////////////////////////////
//Testing

var shuckMyDeck = new Deck();

shuckMyDeck.shuffleDeck();

console.log(shuckMyDeck);
