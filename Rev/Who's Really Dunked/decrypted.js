const crypto = require('crypto');
const readline = require('readline');

// Create an interface to read input from the user
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Initial flag prefix
let flagPrefix = "CM{";

// Function to check user inputs and validate the flag
function check() {
    rl.question('Enter first value: ', (valueOne) => {
        rl.question('Enter second value: ', (valueTwo) => {
            rl.question('Enter third value: ', (valueThree) => {
                rl.close();

                // Initialize flag with the prefix
                let flag = flagPrefix;

                // Append parts to the flag based on input values
                if (valueOne === "News") {
                    flag += "News_";
                }

                if (valueTwo === "Alerts") {
                    flag += "Alerts_";
                }

                if (valueThree === "Incident") {
                    flag += "Incident";
                }

                flag += "}";

                // Check if the computed hash matches the expected hash
                const expectedHash = "805d65570539763df20da6ab7d596676bb3da41a06dae7675718f6c2b755a28d"
                if (hash(flag) === expectedHash) {
                    console.log("Congratulations! The flag is: " + flag);
                } else {
                    console.log("Incorrect flag. Try again.");
                }
            });
        });
    });
}

// Function to compute SHA-256 hash
function hash(input) {
    return crypto.createHash('sha256').update(input).digest('hex');
}

// Start the challenge
check();