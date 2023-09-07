class AefCoinToken {
    constructor() {
        this.totalSupply = 1000000; // Total supply of AEF Coin
        this.tokenSymbol = "AEF"; // Token symbol
        this.tokenName = "AEF Coin"; // Token name
        this.tokenHolders = {}; // Object to store token balances by wallet address
    }

    // Function to initialize a wallet with AEF Coins
    initializeWallet(walletAddress) {
        if (!this.tokenHolders[walletAddress]) {
            this.tokenHolders[walletAddress] = 0;
        }
    }

    // Function to transfer AEF Coins from one wallet to another
    transfer(senderAddress, receiverAddress, amount) {
        if (this.tokenHolders[senderAddress] >= amount) {
            this.tokenHolders[senderAddress] -= amount;
            this.tokenHolders[receiverAddress] += amount;
            return true; // Transfer successful
        }
        return false; // Insufficient balance
    }

    // Function to check the balance of a wallet
    getBalance(walletAddress) {
        return this.tokenHolders[walletAddress] || 0;
    }
}

// Usage example:

const token = new AefCoinToken();

// Initialize wallets
token.initializeWallet("Wallet1");
token.initializeWallet("Wallet2");

// Perform a transfer
if (token.transfer("Wallet1", "Wallet2", 100)) {
    console.log("Transfer successful!");
} else {
    console.log("Transfer failed: Insufficient balance.");
}

// Check wallet balances
console.log("Wallet1 Balance:", token.getBalance("Wallet1"));
console.log("Wallet2 Balance:", token.getBalance("Wallet2"));
