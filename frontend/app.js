document.getElementById('startButton').onclick = function() {
    const username = document.getElementById('username').value;
    const privateKey = document.getElementById('privateKey').value;

    if (username && privateKey) {
        const proof = generateProof(privateKey);
        document.getElementById('message').innerText = `Hello ${username}, your proof is generated.`;
    } else {
        document.getElementById('message').innerText = "Please enter both fields.";
    }
};

function generateProof(privateKey) {
    return btoa(privateKey); // Placeholder encoding for demonstration
}
