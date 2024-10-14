const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json()); // To handle JSON data

// Store users (for now, just in memory, no database)
let users = [];

// Route to register a new user
app.post('/register', (req, res) => {
    const { username, password } = req.body;
    users.push({ username, password });
    res.json({ message: 'User registered successfully!' });
});

// Route to login a user
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);
    if (user) {
        res.json({ message: 'Login successful!' });
    } else {
        res.json({ message: 'Invalid username or password' });
    }
});

// Start the service on port 3000
app.listen(3000, () => {
    console.log('User service running on port 3000');
});
