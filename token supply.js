class Token {
    constructor(name, symbol) {
        this.name = name;
        this.symbol = symbol;
        this.totalSupply = 0;
        this.holders = {};
    }

    // Mint new tokens and assign them to an address
    mint(receiver, amount) {
        if (!this.holders[receiver]) {
            this.holders[receiver] = 0;
        }
        this.totalSupply += amount;
        this.holders[receiver] += amount;
    }

    // Transfer tokens from one address to another
    transfer(sender, receiver, amount) {
        if (!this.holders[sender] || this.holders[sender] < amount) {
            return false; // Insufficient balance
        }
        if (!this.holders[receiver]) {
            this.holders[receiver] = 0;
        }
        this.holders[sender] -= amount;
        this.holders[receiver] += amount;
        return true;
    }

    // Check the balance of an address
    getBalance(address) {
        return this.holders[address] || 0;
    }

    // Get the total supply of tokens
    getTotalSupply() {
        return this.totalSupply;
    }
}

// Usage example:

const myToken = new Token("My Token", "MTK");

// Mint tokens for addresses
myToken.mint("Address1", 1000);
myToken.mint("Address2", 500);

// Transfer tokens between addresses
myToken.transfer("Address1", "Address2", 200);

// Check balances
console.log("Address1 Balance:", myToken.getBalance("Address1"));
console.log("Address2 Balance:", myToken.getBalance("Address2"));
console.log("Total Supply:", myToken.getTotalSupply());
